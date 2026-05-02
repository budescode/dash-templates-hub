from dash import Input, Output, State, html, no_update
import requests as req


BASE_URL = 'http://localhost:8050'


def register_auth_callbacks(app):

    @app.callback(
        Output('page-content', 'children'),
        Input('url', 'pathname'),
        Input('session-store', 'data'),
    )
    def route_page(pathname, session_data):
        from ..layouts.auth import get_auth_layout
        from ..layouts.chat import get_chat_layout
        if session_data is not None and isinstance(session_data, dict) and session_data.get('token'):
            # Validate the token is still alive in Redis
            try:
                resp = req.get(
                    f'{BASE_URL}/api/auth/me',
                    headers={'X-Session-Token': session_data['token']},
                    timeout=3,
                )
                if resp.status_code == 200:
                    return get_chat_layout()
            except Exception:
                pass
            # Token invalid/expired — show login
            return get_auth_layout()
        return get_auth_layout()

    @app.callback(
        Output('otp-step', 'style'),
        Output('phone-step', 'style'),
        Output('phone-error', 'children'),
        Output('otp-sent-to', 'children'),
        Output('otp-dev-hint', 'children'),
        Output('otp-dev-hint', 'style'),
        Input('send-otp-btn', 'n_clicks'),
        State('phone-input', 'value'),
        prevent_initial_call=True,
    )
    def send_otp(n_clicks, phone):
        if not phone:
            return (
                no_update, no_update,
                'Please enter your phone number',
                no_update, no_update, no_update,
            )

        phone = phone.strip().replace(' ', '').replace('-', '')
        try:
            resp = req.post(
                f'{BASE_URL}/api/auth/send-otp',
                json={'phone_number': phone},
                timeout=10,
            )
            data = resp.json()
            if data.get('success'):
                hint_style = {
                    'background': '#1a3026',
                    'border': '1px solid #25D366',
                    'borderRadius': '8px',
                    'padding': '12px 16px',
                    'marginBottom': '16px',
                    'display': 'block',
                    'textAlign': 'center',
                }
                hint_children = ''
                if data.get('dev_code'):
                    hint_children = html.Div([
                        html.Div(
                            'Dev Mode OTP',
                            style={'color': '#8696a0', 'fontSize': '11px',
                                   'textTransform': 'uppercase', 'letterSpacing': '1px',
                                   'marginBottom': '4px'},
                        ),
                        html.Div(
                            data['dev_code'],
                            style={
                                'color': '#25D366',
                                'fontSize': '32px',
                                'fontWeight': '800',
                                'letterSpacing': '12px',
                                'fontFamily': 'monospace',
                            },
                        ),
                    ])
                return (
                    {'display': 'block'},
                    {'display': 'none'},
                    '',
                    f'We sent a code to +{phone}',
                    hint_children,
                    hint_style,
                )
            else:
                return (
                    no_update, no_update,
                    data.get('message', 'Failed to send OTP'),
                    no_update, no_update, {'display': 'none'},
                )
        except Exception as e:
            return (
                no_update, no_update,
                f'Error: {str(e)}',
                no_update, no_update, {'display': 'none'},
            )

    @app.callback(
        Output('session-store', 'data'),
        Output('otp-error', 'children'),
        Output('url', 'href'),
        Input('verify-otp-btn', 'n_clicks'),
        Input('otp-input', 'n_submit'),
        State('phone-input', 'value'),
        State('otp-input', 'value'),
        prevent_initial_call=True,
    )
    def verify_otp(n_clicks, n_submit, phone, code):
        code = (code or '').strip()
        if len(code) != 6 or not code.isdigit():
            return (
                no_update,
                'Please enter the complete 6-digit code',
                no_update,
            )

        phone = (phone or '').strip().replace(' ', '').replace('-', '')

        try:
            resp = req.post(
                f'{BASE_URL}/api/auth/verify-otp',
                json={'phone_number': phone, 'code': code},
                timeout=10,
            )
            data = resp.json()
            if data.get('success'):
                session_data = {'token': data['token'], 'user': data['user']}
                return session_data, '', '/'
            else:
                return no_update, data.get('message', 'Invalid OTP'), no_update
        except Exception as e:
            return no_update, f'Error: {str(e)}', no_update

    @app.callback(
        Output('phone-step', 'style', allow_duplicate=True),
        Output('otp-step', 'style', allow_duplicate=True),
        Input('back-to-phone', 'n_clicks'),
        prevent_initial_call=True,
    )
    def back_to_phone(n_clicks):
        return {'display': 'block'}, {'display': 'none'}
