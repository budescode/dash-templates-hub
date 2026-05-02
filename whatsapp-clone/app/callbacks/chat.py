import json
from datetime import datetime, timezone
from dash import Input, Output, State, html, no_update, ALL, ctx
import dash_bootstrap_components as dbc
import requests as req


BASE_URL = 'http://localhost:8050'


def get_initials(name):
    """Return display initials. For phone numbers, show last 2 digits."""
    if not name:
        return '?'
    cleaned = name.lstrip('+').replace(' ', '').replace('-', '')
    if cleaned.isdigit():
        return name[-2:]  # last 2 digits of phone
    words = name.split()
    return ''.join(w[0].upper() for w in words[:2])


def format_time(iso_str):
    try:
        dt = datetime.fromisoformat(iso_str.replace('Z', '+00:00'))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        now = datetime.now(timezone.utc)
        diff = now - dt
        if diff.days == 0:
            return dt.strftime('%H:%M')
        elif diff.days == 1:
            return 'Yesterday'
        elif diff.days < 7:
            return dt.strftime('%A')
        else:
            return dt.strftime('%d/%m/%Y')
    except Exception:
        return ''


def make_message_bubble(msg, current_user_id):
    is_mine = msg['sender_id'] == current_user_id
    bubble_style = {
        'maxWidth': '65%',
        'padding': '8px 12px',
        'borderRadius': '8px',
        'marginBottom': '4px',
        'position': 'relative',
        'wordBreak': 'break-word',
        'fontSize': '14px',
        'lineHeight': '1.5',
    }
    if is_mine:
        bubble_style.update({
            'background': '#005c4b',
            'color': '#e9edef',
            'borderTopRightRadius': '0',
        })
    else:
        bubble_style.update({
            'background': '#202c33',
            'color': '#e9edef',
            'borderTopLeftRadius': '0',
        })

    content = 'This message was deleted' if msg.get('is_deleted') else msg['content']
    content_style = {
        'fontStyle': 'italic' if msg.get('is_deleted') else 'normal',
        'color': '#8696a0' if msg.get('is_deleted') else '#e9edef',
    }

    return html.Div([
        html.Div([
            # Sender name for groups
            html.Div(
                msg.get('sender_name', ''),
                style={
                    'color': msg.get('sender_color', '#25D366'),
                    'fontSize': '12px',
                    'fontWeight': '600',
                    'marginBottom': '2px',
                },
            ) if not is_mine and msg.get('sender_name') else html.Div(),
            html.Div(content, style=content_style),
            html.Div(
                format_time(msg['created_at']),
                style={
                    'fontSize': '11px', 'color': '#8696a0',
                    'textAlign': 'right', 'marginTop': '4px',
                },
            ),
        ], style=bubble_style),
    ], style={
        'display': 'flex',
        'justifyContent': 'flex-end' if is_mine else 'flex-start',
        'marginBottom': '2px',
    })


def make_conversation_item(conv, is_active=False):
    name = conv.get('name', 'Unknown')
    initials = get_initials(name)
    bg = conv.get('avatar_color', '#25D366')
    last_msg = conv.get('last_message', '')
    last_time = format_time(conv.get('last_message_time', ''))
    unread = conv.get('unread_count', 0)
    is_online = conv.get('is_online', False)

    return html.Div([
        # Avatar
        html.Div([
            html.Div(
                initials,
                style={
                    'width': '50px', 'height': '50px', 'borderRadius': '50%',
                    'background': bg, 'color': '#fff', 'display': 'flex',
                    'alignItems': 'center', 'justifyContent': 'center',
                    'fontSize': '18px', 'fontWeight': '600', 'flexShrink': '0',
                },
            ),
            # Online dot
            html.Div(style={
                'position': 'absolute', 'bottom': '0', 'right': '0',
                'width': '14px', 'height': '14px', 'borderRadius': '50%',
                'background': '#25D366', 'border': '2px solid #111b21',
            }) if is_online else html.Div(),
        ], style={'position': 'relative', 'marginRight': '12px', 'flexShrink': '0'}),

        # Content
        html.Div([
            html.Div([
                html.Div(
                    name,
                    style={
                        'color': '#e9edef', 'fontWeight': '500',
                        'fontSize': '15px', 'flex': '1',
                        'overflow': 'hidden', 'textOverflow': 'ellipsis',
                        'whiteSpace': 'nowrap',
                    },
                ),
                html.Div(
                    last_time,
                    style={'color': '#8696a0', 'fontSize': '12px', 'flexShrink': '0'},
                ),
            ], style={
                'display': 'flex', 'justifyContent': 'space-between',
                'alignItems': 'center', 'marginBottom': '4px',
            }),
            html.Div([
                html.Div(
                    (last_msg[:50] + ('...' if len(last_msg) > 50 else ''))
                    if last_msg else '',
                    style={
                        'color': '#8696a0', 'fontSize': '13px', 'flex': '1',
                        'overflow': 'hidden', 'textOverflow': 'ellipsis',
                        'whiteSpace': 'nowrap',
                    },
                ),
                html.Div(
                    str(unread),
                    style={
                        'background': '#25D366', 'color': '#fff',
                        'borderRadius': '50%', 'width': '20px', 'height': '20px',
                        'display': 'flex', 'alignItems': 'center',
                        'justifyContent': 'center', 'fontSize': '11px',
                        'flexShrink': '0',
                    },
                ) if unread > 0 else html.Div(),
            ], style={
                'display': 'flex', 'justifyContent': 'space-between',
                'alignItems': 'center',
            }),
        ], style={'flex': '1', 'overflow': 'hidden', 'minWidth': '0'}),

    ], id={'type': 'conv-item', 'index': conv['id']}, n_clicks=0, style={
        'display': 'flex', 'alignItems': 'center', 'padding': '12px 16px',
        'cursor': 'pointer', 'borderBottom': '1px solid #1e2c35',
        'background': '#2a3942' if is_active else 'transparent',
    })


def register_chat_callbacks(app):

    # Initialize user data from session + detect expired sessions
    @app.callback(
        Output('current-user-store', 'data'),
        Output('my-profile-btn', 'children'),
        Output('my-profile-btn', 'style'),
        Output('my-name-display', 'children'),
        Output('session-store', 'data', allow_duplicate=True),
        Output('url', 'href', allow_duplicate=True),
        Input('poll-interval', 'n_intervals'),
        State('session-store', 'data'),
        State('current-user-store', 'data'),
        prevent_initial_call=True,
    )
    def update_user_data(n, session_data, current_user):
        no_change = (no_update, no_update, no_update, no_update, no_update, no_update)
        if not session_data or not session_data.get('token'):
            return no_change

        token = session_data['token']
        try:
            resp = req.get(
                f'{BASE_URL}/api/auth/me',
                headers={'X-Session-Token': token},
                timeout=5,
            )
            if resp.status_code == 401:
                # Session expired — clear store and redirect to login
                return no_update, no_update, no_update, no_update, {}, '/'
            if resp.status_code != 200:
                return no_change
            user = resp.json().get('user', {})
            name = user.get('name', user.get('phone_number', '?'))
            initials = get_initials(name)
            avatar_style = {
                'width': '40px', 'height': '40px', 'borderRadius': '50%',
                'display': 'flex', 'alignItems': 'center',
                'justifyContent': 'center', 'fontSize': '16px',
                'fontWeight': '600', 'color': '#fff',
                'background': user.get('avatar_color', '#25D366'),
                'cursor': 'pointer',
            }
            return user, initials, avatar_style, name, no_update, no_update
        except Exception:
            return no_change

    # Fetch and display conversations
    @app.callback(
        Output('conversations-store', 'data'),
        Output('conversations-list', 'children'),
        Input('poll-interval', 'n_intervals'),
        State('session-store', 'data'),
        State('active-conversation-store', 'data'),
        prevent_initial_call=True,
    )
    def fetch_conversations(n, session_data, active_conv):
        if not session_data or not session_data.get('token'):
            return no_update, no_update
        token = session_data['token']
        try:
            resp = req.get(
                f'{BASE_URL}/api/messages/conversations',
                headers={'X-Session-Token': token},
                timeout=5,
            )
            if resp.status_code != 200:
                return no_update, no_update
            convs = resp.json().get('conversations', [])
            active_id = active_conv.get('id') if active_conv else None
            items = [make_conversation_item(c, c['id'] == active_id) for c in convs]
            if not items:
                items = [html.Div(
                    'No conversations yet. Start a new chat!',
                    style={
                        'color': '#8696a0', 'textAlign': 'center',
                        'padding': '40px 20px', 'fontSize': '14px',
                    },
                )]
            return convs, items
        except Exception:
            return no_update, no_update

    # Open conversation when clicked
    @app.callback(
        Output('active-conversation-store', 'data'),
        Output('messages-store', 'data'),
        Output('last-message-id-store', 'data'),
        Output('welcome-screen', 'style'),
        Output('chat-area', 'style'),
        Output('chat-contact-name', 'children'),
        Output('chat-contact-status', 'children'),
        Output('chat-avatar', 'children'),
        Output('chat-avatar', 'style'),
        Input({'type': 'conv-item', 'index': ALL}, 'n_clicks'),
        State('session-store', 'data'),
        State('conversations-store', 'data'),
        prevent_initial_call=True,
    )
    def open_conversation(n_clicks_list, session_data, convs):
        if not any(n_clicks_list) or not session_data:
            return [no_update] * 9

        triggered = ctx.triggered_id
        if not triggered or not isinstance(triggered, dict):
            return [no_update] * 9

        conv_id = triggered['index']
        token = session_data['token']

        # Find conv info
        conv_info = next((c for c in (convs or []) if c['id'] == conv_id), None)

        # Fetch messages
        try:
            resp = req.get(
                f'{BASE_URL}/api/messages/conversations/{conv_id}/messages',
                headers={'X-Session-Token': token},
                timeout=10,
            )
            messages = resp.json().get('messages', [])
        except Exception:
            messages = []

        last_id = messages[-1]['id'] if messages else 0

        name = conv_info.get('name', 'Unknown') if conv_info else 'Unknown'
        is_online = conv_info.get('is_online', False) if conv_info else False
        bg_color = conv_info.get('avatar_color', '#25D366') if conv_info else '#25D366'
        initials = get_initials(name)

        avatar_style = {
            'width': '40px', 'height': '40px', 'borderRadius': '50%',
            'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center',
            'fontSize': '16px', 'color': '#fff', 'fontWeight': '600',
            'background': bg_color, 'cursor': 'pointer',
        }

        status_text = 'online' if is_online else 'last seen recently'

        return (
            {'id': conv_id, 'name': name, 'avatar_color': bg_color},
            messages,
            last_id,
            {'display': 'none'},
            {'display': 'flex', 'flexDirection': 'column', 'flex': '1', 'height': '100vh'},
            name,
            status_text,
            initials,
            avatar_style,
        )

    # Render messages
    @app.callback(
        Output('messages-container', 'children'),
        Input('messages-store', 'data'),
        State('session-store', 'data'),
        prevent_initial_call=True,
    )
    def render_messages(messages, session_data):
        if not messages or not session_data:
            return []
        user = session_data.get('user', {})
        user_id = user.get('id')

        bubbles = []
        prev_date = None
        for msg in messages:
            try:
                msg_date = datetime.fromisoformat(
                    msg['created_at'].replace('Z', '+00:00')
                ).strftime('%B %d, %Y')
            except Exception:
                msg_date = ''

            if msg_date != prev_date:
                bubbles.append(html.Div(
                    msg_date,
                    style={
                        'textAlign': 'center', 'color': '#8696a0',
                        'fontSize': '12px', 'background': '#1f2c34',
                        'display': 'inline-block', 'padding': '4px 12px',
                        'borderRadius': '8px',
                        'margin': '10px auto', 'width': 'fit-content',
                    },
                ))
                prev_date = msg_date
            bubbles.append(make_message_bubble(msg, user_id))

        return bubbles

    # Poll for new messages
    @app.callback(
        Output('messages-store', 'data', allow_duplicate=True),
        Output('last-message-id-store', 'data', allow_duplicate=True),
        Output('typing-indicator', 'children'),
        Input('poll-interval', 'n_intervals'),
        State('session-store', 'data'),
        State('active-conversation-store', 'data'),
        State('last-message-id-store', 'data'),
        State('messages-store', 'data'),
        prevent_initial_call=True,
    )
    def poll_messages(n, session_data, active_conv, last_id, current_messages):
        if not session_data or not active_conv:
            return no_update, no_update, ''

        token = session_data['token']
        conv_id = active_conv['id']

        typing_text = ''
        try:
            t_resp = req.get(
                f'{BASE_URL}/api/messages/conversations/{conv_id}/typing',
                headers={'X-Session-Token': token},
                timeout=3,
            )
            typing_users = t_resp.json().get('typing_users', [])
            if typing_users:
                names = ', '.join(typing_users[:2])
                typing_text = (
                    f'{names} {"is" if len(typing_users) == 1 else "are"} typing...'
                )
        except Exception:
            pass

        if not last_id:
            return no_update, no_update, typing_text

        try:
            resp = req.get(
                f'{BASE_URL}/api/messages/conversations/{conv_id}/messages'
                f'?since_id={last_id}',
                headers={'X-Session-Token': token},
                timeout=5,
            )
            new_msgs = resp.json().get('messages', [])
            if new_msgs:
                merged = list(current_messages or []) + new_msgs
                new_last_id = new_msgs[-1]['id']
                return merged, new_last_id, typing_text
        except Exception:
            pass

        return no_update, no_update, typing_text

    # Send message
    @app.callback(
        Output('message-input', 'value'),
        Output('messages-store', 'data', allow_duplicate=True),
        Output('last-message-id-store', 'data', allow_duplicate=True),
        Input('send-btn', 'n_clicks'),
        State('message-input', 'value'),
        State('session-store', 'data'),
        State('active-conversation-store', 'data'),
        State('messages-store', 'data'),
        prevent_initial_call=True,
    )
    def send_message(n_clicks, content, session_data, active_conv, current_messages):
        if (
            not n_clicks
            or not content
            or not content.strip()
            or not session_data
            or not active_conv
        ):
            return no_update, no_update, no_update

        token = session_data['token']
        conv_id = active_conv['id']

        try:
            resp = req.post(
                f'{BASE_URL}/api/messages/conversations/{conv_id}/messages',
                json={'content': content.strip()},
                headers={'X-Session-Token': token},
                timeout=10,
            )
            data = resp.json()
            if data.get('success'):
                new_msg = data['message']
                msgs = list(current_messages or []) + [new_msg]
                return '', msgs, new_msg['id']
        except Exception:
            pass

        return no_update, no_update, no_update

    # Typing status (fire-and-forget, dummy output required by Dash)
    @app.callback(
        Output('typing-send-dummy', 'children'),
        Input('message-input', 'value'),
        State('session-store', 'data'),
        State('active-conversation-store', 'data'),
        prevent_initial_call=True,
    )
    def send_typing_status(value, session_data, active_conv):
        if not session_data or not active_conv:
            return no_update
        token = session_data['token']
        conv_id = active_conv['id']
        is_typing = bool(value and value.strip())
        try:
            req.post(
                f'{BASE_URL}/api/messages/conversations/{conv_id}/typing',
                json={'is_typing': is_typing},
                headers={'X-Session-Token': token},
                timeout=2,
            )
        except Exception:
            pass
        return no_update

    # Profile modal
    @app.callback(
        Output('profile-modal', 'is_open'),
        Output('profile-name-input', 'value'),
        Output('profile-about-input', 'value'),
        Output('profile-phone-display', 'children'),
        Output('profile-avatar-display', 'children'),
        Output('profile-avatar-display', 'style'),
        Input('my-profile-btn', 'n_clicks'),
        Input('save-profile-btn', 'n_clicks'),
        Input('logout-btn', 'n_clicks'),
        State('profile-modal', 'is_open'),
        State('session-store', 'data'),
        State('profile-name-input', 'value'),
        State('profile-about-input', 'value'),
        prevent_initial_call=True,
    )
    def handle_profile_modal(
        open_clicks, save_clicks, logout_clicks,
        is_open, session_data, name, about,
    ):
        trig = ctx.triggered_id
        if not session_data:
            return False, no_update, no_update, no_update, no_update, no_update

        token = session_data['token']
        user = session_data.get('user', {})

        if trig == 'logout-btn':
            try:
                req.post(
                    f'{BASE_URL}/api/auth/logout',
                    headers={'X-Session-Token': token},
                )
            except Exception:
                pass
            return False, no_update, no_update, no_update, no_update, no_update

        if trig == 'save-profile-btn':
            try:
                req.post(
                    f'{BASE_URL}/api/auth/update-profile',
                    json={'name': name, 'about': about},
                    headers={'X-Session-Token': token},
                )
            except Exception:
                pass
            return False, no_update, no_update, no_update, no_update, no_update

        if trig == 'my-profile-btn':
            u_name = user.get('name', '')
            u_about = user.get('about', '')
            u_phone = user.get('phone_number', '')
            u_color = user.get('avatar_color', '#25D366')
            initials = get_initials(u_name)
            avatar_style = {
                'width': '100px', 'height': '100px', 'borderRadius': '50%',
                'display': 'flex', 'alignItems': 'center',
                'justifyContent': 'center',
                'fontSize': '22px' if len(initials) > 1 else '40px',
                'fontWeight': '700',
                'color': '#fff', 'margin': '0 auto 20px',
                'background': u_color,
            }
            return True, u_name, u_about, u_phone, initials, avatar_style

        return no_update, no_update, no_update, no_update, no_update, no_update

    # Logout redirect
    @app.callback(
        Output('session-store', 'data', allow_duplicate=True),
        Output('url', 'href', allow_duplicate=True),
        Input('logout-btn', 'n_clicks'),
        State('session-store', 'data'),
        prevent_initial_call=True,
    )
    def do_logout(n_clicks, session_data):
        if n_clicks and n_clicks > 0:
            if session_data and session_data.get('token'):
                try:
                    req.post(
                        f'{BASE_URL}/api/auth/logout',
                        headers={'X-Session-Token': session_data['token']},
                    )
                except Exception:
                    pass
            return {}, '/'
        return no_update, no_update

    # New chat modal toggle
    @app.callback(
        Output('new-chat-modal', 'is_open'),
        Input('new-chat-btn', 'n_clicks'),
        State('new-chat-modal', 'is_open'),
        prevent_initial_call=True,
    )
    def toggle_new_chat(n, is_open):
        return not is_open

    # New group modal toggle
    @app.callback(
        Output('new-group-modal', 'is_open'),
        Input('new-group-btn', 'n_clicks'),
        State('new-group-modal', 'is_open'),
        prevent_initial_call=True,
    )
    def toggle_new_group(n, is_open):
        return not is_open

    # Search users for new chat
    @app.callback(
        Output('new-chat-results', 'children'),
        Input('new-chat-search', 'value'),
        State('session-store', 'data'),
        prevent_initial_call=True,
    )
    def search_users_for_chat(query, session_data):
        if not query or len(query) < 2 or not session_data:
            return []
        token = session_data['token']
        try:
            resp = req.get(
                f'{BASE_URL}/api/auth/users/search?q={query}',
                headers={'X-Session-Token': token},
                timeout=5,
            )
            users = resp.json().get('users', [])
            items = []
            for u in users:
                name = u.get('name', u.get('phone_number'))
                initials = get_initials(name)
                items.append(html.Div([
                    html.Div(
                        initials,
                        style={
                            'width': '40px', 'height': '40px', 'borderRadius': '50%',
                            'background': u.get('avatar_color', '#25D366'),
                            'color': '#fff', 'display': 'flex',
                            'alignItems': 'center', 'justifyContent': 'center',
                            'fontWeight': '600', 'marginRight': '12px',
                            'flexShrink': '0',
                        },
                    ),
                    html.Div([
                        html.Div(name, style={'color': '#e9edef', 'fontSize': '14px'}),
                        html.Div(
                            u.get('phone_number'),
                            style={'color': '#8696a0', 'fontSize': '12px'},
                        ),
                    ]),
                ], id={'type': 'start-chat-user', 'index': u['id']}, n_clicks=0,
                   style={
                    'display': 'flex', 'alignItems': 'center', 'padding': '10px',
                    'cursor': 'pointer', 'borderBottom': '1px solid #2a3942',
                    'borderRadius': '4px',
                }))
            return items if items else [
                html.Div([
                    html.P('No users found', style={'color': '#8696a0', 'margin': '0 0 4px'}),
                    html.P('Make sure the other person has already signed up.',
                           style={'color': '#4a5a63', 'fontSize': '12px', 'margin': '0'}),
                ], style={'padding': '12px'})
            ]
        except Exception as e:
            return [html.P(f'Error: {str(e)}', style={'color': '#ff6b6b'})]

    # Start new chat with user
    @app.callback(
        Output('new-chat-modal', 'is_open', allow_duplicate=True),
        Output('active-conversation-store', 'data', allow_duplicate=True),
        Input({'type': 'start-chat-user', 'index': ALL}, 'n_clicks'),
        State('session-store', 'data'),
        prevent_initial_call=True,
    )
    def start_new_chat(n_clicks_list, session_data):
        if not any(n_clicks_list) or not session_data:
            return no_update, no_update
        triggered = ctx.triggered_id
        if not triggered:
            return no_update, no_update

        user_id = triggered['index']
        token = session_data['token']
        try:
            resp = req.post(
                f'{BASE_URL}/api/messages/conversations',
                json={'user_id': user_id},
                headers={'X-Session-Token': token},
                timeout=10,
            )
            data = resp.json()
            if data.get('success'):
                return False, {'id': data['conversation_id']}
        except Exception:
            pass
        return no_update, no_update

    # Group member search
    @app.callback(
        Output('group-search-results', 'children'),
        Input('group-search-input', 'value'),
        State('session-store', 'data'),
        State('selected-members-store', 'data'),
        prevent_initial_call=True,
    )
    def search_group_members(query, session_data, selected):
        if not query or len(query) < 2 or not session_data:
            return []
        token = session_data['token']
        selected_ids = [m['id'] for m in (selected or [])]
        try:
            resp = req.get(
                f'{BASE_URL}/api/auth/users/search?q={query}',
                headers={'X-Session-Token': token},
                timeout=5,
            )
            users = resp.json().get('users', [])
            items = []
            for u in users:
                if u['id'] in selected_ids:
                    continue
                name = u.get('name', u.get('phone_number'))
                initials = get_initials(name)
                member_payload = json.dumps({
                    'id': u['id'],
                    'name': name,
                    'color': u.get('avatar_color', '#25D366'),
                })
                items.append(html.Div([
                    html.Div(
                        initials,
                        style={
                            'width': '36px', 'height': '36px', 'borderRadius': '50%',
                            'background': u.get('avatar_color', '#25D366'),
                            'color': '#fff', 'display': 'flex',
                            'alignItems': 'center', 'justifyContent': 'center',
                            'fontWeight': '600', 'marginRight': '10px',
                            'flexShrink': '0',
                        },
                    ),
                    html.Div(
                        name,
                        style={'color': '#e9edef', 'fontSize': '14px', 'flex': '1'},
                    ),
                    html.I(
                        className='fas fa-plus-circle',
                        style={'color': '#25D366', 'fontSize': '18px'},
                    ),
                ], id={'type': 'add-group-member', 'index': member_payload},
                   n_clicks=0, style={
                    'display': 'flex', 'alignItems': 'center', 'padding': '8px',
                    'cursor': 'pointer', 'borderBottom': '1px solid #2a3942',
                }))
            return items
        except Exception:
            return []

    # Add group member
    @app.callback(
        Output('selected-members-store', 'data'),
        Output('selected-members-display', 'children'),
        Input({'type': 'add-group-member', 'index': ALL}, 'n_clicks'),
        State('selected-members-store', 'data'),
        prevent_initial_call=True,
    )
    def add_group_member(n_clicks_list, selected):
        if not any(n_clicks_list):
            return no_update, no_update
        triggered = ctx.triggered_id
        if not triggered:
            return no_update, no_update

        member_data = json.loads(triggered['index'])
        selected = list(selected or [])
        if not any(m['id'] == member_data['id'] for m in selected):
            selected.append(member_data)

        chips = [html.Div([
            html.Div(
                ''.join(w[0].upper() for w in m['name'].split()[:2]),
                style={
                    'width': '30px', 'height': '30px', 'borderRadius': '50%',
                    'background': m.get('color', '#25D366'), 'color': '#fff',
                    'display': 'flex', 'alignItems': 'center',
                    'justifyContent': 'center', 'fontSize': '12px',
                    'fontWeight': '600', 'marginRight': '6px',
                },
            ),
            html.Span(m['name'], style={'color': '#e9edef', 'fontSize': '13px'}),
        ], style={
            'display': 'flex', 'alignItems': 'center',
            'background': '#2a3942', 'padding': '4px 10px',
            'borderRadius': '20px', 'margin': '4px',
        }) for m in selected]

        return selected, html.Div(chips, style={'display': 'flex', 'flexWrap': 'wrap'})

    # Create group
    @app.callback(
        Output('new-group-modal', 'is_open', allow_duplicate=True),
        Output('active-conversation-store', 'data', allow_duplicate=True),
        Input('create-group-btn', 'n_clicks'),
        State('group-name-input', 'value'),
        State('selected-members-store', 'data'),
        State('session-store', 'data'),
        prevent_initial_call=True,
    )
    def create_group(n_clicks, group_name, members, session_data):
        if not n_clicks or not group_name or not members or not session_data:
            return no_update, no_update
        token = session_data['token']
        member_ids = [m['id'] for m in members]
        try:
            resp = req.post(
                f'{BASE_URL}/api/messages/conversations',
                json={'group_name': group_name, 'member_ids': member_ids},
                headers={'X-Session-Token': token},
                timeout=10,
            )
            data = resp.json()
            if data.get('success'):
                return False, {'id': data['conversation_id'], 'name': group_name}
        except Exception:
            pass
        return no_update, no_update

    # Sidebar search — filter conversations or find new users
    @app.callback(
        Output('search-results', 'children'),
        Output('search-results', 'style'),
        Input('search-input', 'value'),
        State('session-store', 'data'),
        State('conversations-store', 'data'),
        prevent_initial_call=True,
    )
    def sidebar_search(query, session_data, convs):
        if not query or len(query) < 1:
            return [], {'display': 'none'}
        if not session_data:
            return [], {'display': 'none'}

        token = session_data['token']
        q = query.lower()

        matched_convs = [c for c in (convs or []) if q in c.get('name', '').lower()]
        items = [make_conversation_item(c) for c in matched_convs]

        if len(query) >= 2:
            try:
                resp = req.get(
                    f'{BASE_URL}/api/auth/users/search?q={query}',
                    headers={'X-Session-Token': token},
                    timeout=5,
                )
                users = resp.json().get('users', [])
                existing_ids = {
                    c.get('other_user', {}).get('id') for c in (convs or [])
                    if c.get('other_user')
                }
                for u in users:
                    if u['id'] in existing_ids:
                        continue
                    name = u.get('name', u.get('phone_number', ''))
                    initials = get_initials(name)
                    items.append(html.Div([
                        html.Div([
                            html.Div(initials, style={
                                'width': '50px', 'height': '50px', 'borderRadius': '50%',
                                'background': u.get('avatar_color', '#25D366'), 'color': '#fff',
                                'display': 'flex', 'alignItems': 'center',
                                'justifyContent': 'center', 'fontSize': '18px',
                                'fontWeight': '600', 'flexShrink': '0',
                            }),
                        ], style={'position': 'relative', 'marginRight': '12px', 'flexShrink': '0'}),
                        html.Div([
                            html.Div([
                                html.Div(name, style={
                                    'color': '#e9edef', 'fontWeight': '500', 'fontSize': '15px', 'flex': '1',
                                }),
                                dbc.Badge('New', color='success', style={'fontSize': '10px'}),
                            ], style={'display': 'flex', 'justifyContent': 'space-between',
                                      'alignItems': 'center', 'marginBottom': '4px'}),
                            html.Div(u.get('phone_number', ''), style={'color': '#8696a0', 'fontSize': '13px'}),
                        ], style={'flex': '1', 'overflow': 'hidden', 'minWidth': '0'}),
                    ], id={'type': 'start-chat-user', 'index': u['id']}, n_clicks=0, style={
                        'display': 'flex', 'alignItems': 'center', 'padding': '12px 16px',
                        'cursor': 'pointer', 'borderBottom': '1px solid #1e2c35',
                    }))
            except Exception:
                pass

        if not items:
            items = [html.Div('No results', style={
                'color': '#8696a0', 'textAlign': 'center', 'padding': '20px', 'fontSize': '14px',
            })]

        return items, {
            'background': '#111b21', 'overflowY': 'auto',
            'maxHeight': '60vh', 'borderBottom': '1px solid #2a3942',
        }
