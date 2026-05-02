from dash import html, dcc
import dash_bootstrap_components as dbc


def get_chat_layout():
    return html.Div([
        # LEFT SIDEBAR
        html.Div([
            # Header
            html.Div([
                html.Div([
                    html.Div(
                        id='my-profile-btn',
                        n_clicks=0,
                        style={
                            'width': '40px', 'height': '40px', 'borderRadius': '50%',
                            'display': 'flex', 'alignItems': 'center',
                            'justifyContent': 'center', 'fontSize': '16px',
                            'fontWeight': '600', 'color': '#fff',
                            'background': '#25D366', 'cursor': 'pointer',
                        },
                    ),
                    html.Div(
                        id='my-name-display',
                        style={
                            'color': '#e9edef', 'fontSize': '16px',
                            'fontWeight': '600', 'marginLeft': '10px',
                        },
                    ),
                ], style={'display': 'flex', 'alignItems': 'center'}),
                html.Div([
                    html.I(
                        className='fas fa-users',
                        id='new-group-btn',
                        style={
                            'color': '#8696a0', 'fontSize': '20px',
                            'cursor': 'pointer', 'margin': '0 10px',
                        },
                        title='New Group',
                        n_clicks=0,
                    ),
                    html.I(
                        className='fas fa-comment-dots',
                        id='new-chat-btn',
                        style={
                            'color': '#8696a0', 'fontSize': '20px',
                            'cursor': 'pointer', 'margin': '0 10px',
                        },
                        title='New Chat',
                        n_clicks=0,
                    ),
                    html.I(
                        className='fas fa-ellipsis-v',
                        id='menu-btn',
                        style={
                            'color': '#8696a0', 'fontSize': '20px',
                            'cursor': 'pointer', 'margin': '0 10px',
                        },
                        n_clicks=0,
                    ),
                ], style={'display': 'flex', 'alignItems': 'center'}),
            ], style={
                'display': 'flex', 'justifyContent': 'space-between',
                'alignItems': 'center', 'padding': '10px 16px',
                'background': '#202c33', 'height': '60px',
            }),

            # Search
            html.Div([
                html.Div([
                    html.I(
                        className='fas fa-search',
                        style={'color': '#8696a0', 'marginRight': '10px'},
                    ),
                    dbc.Input(
                        id='search-input',
                        placeholder='Search or start new chat',
                        style={
                            'background': 'transparent', 'border': 'none',
                            'color': '#e9edef', 'fontSize': '14px',
                            'outline': 'none',
                        },
                        debounce=False,
                    ),
                ], style={
                    'display': 'flex', 'alignItems': 'center',
                    'background': '#2a3942', 'borderRadius': '8px',
                    'padding': '8px 12px', 'flex': '1',
                }),
            ], style={'padding': '8px 12px', 'background': '#111b21'}),

            # Search results
            html.Div(id='search-results', style={'display': 'none'}),

            # Conversations list
            html.Div(
                id='conversations-list',
                style={
                    'overflowY': 'auto', 'flex': '1',
                    'background': '#111b21',
                },
            ),

        ], style={
            'width': '420px', 'minWidth': '300px', 'display': 'flex',
            'flexDirection': 'column', 'borderRight': '1px solid #2a3942',
            'height': '100vh', 'background': '#111b21',
        }, id='sidebar'),

        # RIGHT CHAT AREA
        html.Div([
            # Welcome screen (shown when no conversation selected)
            html.Div([
                html.Div([
                    html.I(
                        className='fab fa-whatsapp',
                        style={
                            'fontSize': '80px', 'color': '#25D366',
                            'marginBottom': '20px', 'display': 'block',
                        },
                    ),
                    html.H3(
                        'WhatsApp Web',
                        style={'color': '#e9edef', 'fontWeight': '300'},
                    ),
                    html.P(
                        'Send and receive messages without keeping your phone online.',
                        style={
                            'color': '#8696a0', 'textAlign': 'center',
                            'maxWidth': '400px',
                        },
                    ),
                ], style={'textAlign': 'center'}),
            ], id='welcome-screen', style={
                'display': 'flex', 'alignItems': 'center',
                'justifyContent': 'center', 'height': '100%',
                'flexDirection': 'column', 'background': '#222e35',
            }),

            # Chat area (shown when conversation selected)
            html.Div([
                # Chat header
                html.Div([
                    html.Div(
                        id='chat-avatar',
                        style={
                            'width': '40px', 'height': '40px', 'borderRadius': '50%',
                            'display': 'flex', 'alignItems': 'center',
                            'justifyContent': 'center', 'fontSize': '16px',
                            'color': '#fff', 'fontWeight': '600', 'cursor': 'pointer',
                        },
                    ),
                    html.Div([
                        html.Div(
                            id='chat-contact-name',
                            style={
                                'color': '#e9edef', 'fontWeight': '600',
                                'fontSize': '16px',
                            },
                        ),
                        html.Div(
                            id='chat-contact-status',
                            style={'color': '#8696a0', 'fontSize': '12px'},
                        ),
                    ], style={'marginLeft': '12px', 'flex': '1'}),
                    html.Div([
                        html.I(
                            className='fas fa-search',
                            style={
                                'color': '#8696a0', 'fontSize': '20px',
                                'margin': '0 8px', 'cursor': 'pointer',
                            },
                        ),
                        html.I(
                            className='fas fa-ellipsis-v',
                            id='chat-menu-btn',
                            style={
                                'color': '#8696a0', 'fontSize': '20px',
                                'margin': '0 8px', 'cursor': 'pointer',
                            },
                            n_clicks=0,
                        ),
                    ]),
                ], style={
                    'display': 'flex', 'alignItems': 'center',
                    'padding': '10px 16px', 'background': '#202c33',
                    'height': '60px',
                }, id='chat-header'),

                # Messages area
                html.Div(
                    html.Div(
                        id='messages-container',
                        style={'padding': '20px 10%'},
                    ),
                    id='messages-scroll',
                    style={
                        'flex': '1', 'overflowY': 'auto',
                        'background': '#0b141a',
                        'backgroundImage': (
                            'radial-gradient(ellipse at 50% 50%, '
                            '#0d2137 0%, #0b141a 100%)'
                        ),
                    },
                ),

                # Typing indicator
                html.Div(
                    id='typing-indicator',
                    style={
                        'padding': '4px 20px', 'background': '#0b141a',
                        'color': '#25D366', 'fontSize': '13px',
                        'fontStyle': 'italic', 'minHeight': '24px',
                    },
                ),

                # Message input
                html.Div([
                    html.Div([
                        html.I(
                            className='fas fa-smile',
                            style={
                                'color': '#8696a0', 'fontSize': '24px',
                                'cursor': 'pointer', 'padding': '0 8px',
                            },
                        ),
                    ]),
                    dbc.Textarea(
                        id='message-input',
                        placeholder='Type a message',
                        style={
                            'flex': '1', 'background': '#2a3942',
                            'border': 'none', 'color': '#e9edef',
                            'fontSize': '15px', 'padding': '10px 12px',
                            'resize': 'none', 'maxHeight': '150px',
                            'minHeight': '48px', 'borderRadius': '8px',
                            'outline': 'none',
                        },
                        rows=1,
                        n_submit=0,
                        debounce=False,
                    ),
                    html.Div([
                        dbc.Button(
                            html.I(className='fas fa-paper-plane'),
                            id='send-btn',
                            n_clicks=0,
                            style={
                                'background': '#25D366', 'border': 'none',
                                'borderRadius': '50%', 'width': '48px',
                                'height': '48px', 'display': 'flex',
                                'alignItems': 'center', 'justifyContent': 'center',
                                'marginLeft': '8px', 'color': '#fff',
                                'fontSize': '16px',
                            },
                        ),
                    ]),
                ], style={
                    'display': 'flex', 'alignItems': 'center',
                    'padding': '8px 16px', 'background': '#202c33',
                    'gap': '8px',
                }),

            ], id='chat-area', style={
                'display': 'none', 'flexDirection': 'column',
                'flex': '1', 'height': '100vh',
            }),

        ], style={
            'flex': '1', 'display': 'flex',
            'height': '100vh', 'background': '#222e35',
        }),

        # Profile modal
        dbc.Modal([
            dbc.ModalHeader(
                dbc.ModalTitle("Profile"),
                style={'background': '#202c33', 'color': '#e9edef', 'border': 'none'},
            ),
            dbc.ModalBody([
                html.Div([
                    html.Div(
                        id='profile-avatar-display',
                        style={
                            'width': '100px', 'height': '100px', 'borderRadius': '50%',
                            'display': 'flex', 'alignItems': 'center',
                            'justifyContent': 'center', 'fontSize': '40px',
                            'color': '#fff', 'margin': '0 auto 20px',
                        },
                    ),
                    dbc.Label('Your Name', style={'color': '#8696a0', 'fontSize': '12px'}),
                    dbc.Input(
                        id='profile-name-input',
                        style={
                            'background': '#2a3942',
                            'border': '1px solid #3b4a54',
                            'color': '#e9edef',
                            'marginBottom': '15px',
                        },
                    ),
                    dbc.Label('About', style={'color': '#8696a0', 'fontSize': '12px'}),
                    dbc.Input(
                        id='profile-about-input',
                        style={
                            'background': '#2a3942',
                            'border': '1px solid #3b4a54',
                            'color': '#e9edef',
                            'marginBottom': '15px',
                        },
                    ),
                    dbc.Label('Phone', style={'color': '#8696a0', 'fontSize': '12px'}),
                    html.P(id='profile-phone-display', style={'color': '#e9edef'}),
                ]),
            ], style={'background': '#1f2c34'}),
            dbc.ModalFooter([
                dbc.Button(
                    'Save',
                    id='save-profile-btn',
                    style={'background': '#25D366', 'border': 'none'},
                    n_clicks=0,
                ),
                dbc.Button(
                    'Logout',
                    id='logout-btn',
                    color='danger',
                    style={'marginLeft': '10px'},
                    n_clicks=0,
                ),
            ], style={'background': '#202c33', 'border': 'none'}),
        ], id='profile-modal', is_open=False),

        # New Chat modal
        dbc.Modal([
            dbc.ModalHeader(
                dbc.ModalTitle("New Chat"),
                style={'background': '#202c33', 'color': '#e9edef', 'border': 'none'},
            ),
            dbc.ModalBody([
                dbc.Input(
                    id='new-chat-search',
                    placeholder='Search by phone or name...',
                    style={
                        'background': '#2a3942',
                        'border': '1px solid #3b4a54',
                        'color': '#e9edef',
                        'marginBottom': '10px',
                    },
                    debounce=False,
                    autofocus=True,
                ),
                html.Div(id='new-chat-results'),
            ], style={'background': '#1f2c34'}),
            dbc.ModalFooter(style={'background': '#202c33', 'border': 'none'}),
        ], id='new-chat-modal', is_open=False),

        # New Group modal
        dbc.Modal([
            dbc.ModalHeader(
                dbc.ModalTitle("New Group"),
                style={'background': '#202c33', 'color': '#e9edef', 'border': 'none'},
            ),
            dbc.ModalBody([
                dbc.Input(
                    id='group-name-input',
                    placeholder='Group name...',
                    style={
                        'background': '#2a3942',
                        'border': '1px solid #3b4a54',
                        'color': '#e9edef',
                        'marginBottom': '10px',
                    },
                ),
                dbc.Input(
                    id='group-search-input',
                    placeholder='Search members by phone or name...',
                    style={
                        'background': '#2a3942',
                        'border': '1px solid #3b4a54',
                        'color': '#e9edef',
                        'marginBottom': '10px',
                    },
                    debounce=False,
                ),
                html.Div(id='group-search-results'),
                html.Div(id='selected-members-display', style={'marginTop': '10px'}),
                dcc.Store(id='selected-members-store', data=[]),
            ], style={'background': '#1f2c34'}),
            dbc.ModalFooter([
                dbc.Button(
                    'Create Group',
                    id='create-group-btn',
                    style={'background': '#25D366', 'border': 'none'},
                    n_clicks=0,
                ),
            ], style={'background': '#202c33', 'border': 'none'}),
        ], id='new-group-modal', is_open=False),

    ], style={
        'display': 'flex', 'height': '100vh',
        'overflow': 'hidden', 'background': '#0b141a',
    })
