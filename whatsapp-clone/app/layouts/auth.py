from dash import html, dcc
import dash_bootstrap_components as dbc


def get_auth_layout(mode='login'):
    return html.Div([
        html.Div([
            html.Div([
                # Logo/Header
                html.Div([
                    html.Div(
                        html.I(className='fab fa-whatsapp', style={'color': '#25D366', 'fontSize': '60px'}),
                        style={'marginBottom': '10px'},
                    ),
                    html.H2(
                        'WhatsApp Clone',
                        style={'color': '#fff', 'fontWeight': '300', 'marginBottom': '5px'},
                    ),
                    html.P(
                        'Fast, Simple & Secure',
                        style={'color': '#8696a0', 'marginBottom': '30px'},
                    ),
                ], style={'textAlign': 'center'}),

                # Phone step
                html.Div([
                    html.H5(
                        'Enter your phone number',
                        style={
                            'color': '#e9edef', 'marginBottom': '15px',
                            'textAlign': 'center',
                        },
                    ),
                    html.P(
                        'WhatsApp Clone will send you an OTP to verify your number',
                        style={
                            'color': '#8696a0', 'textAlign': 'center',
                            'fontSize': '13px', 'marginBottom': '20px',
                        },
                    ),
                    dbc.InputGroup([
                        dbc.InputGroupText(
                            '+',
                            style={
                                'background': '#2a3942',
                                'border': '1px solid #3b4a54',
                                'color': '#d1d7db',
                            },
                        ),
                        dbc.Input(
                            id='phone-input',
                            placeholder='Phone number (e.g. 2348012345678)',
                            type='text',
                            style={
                                'background': '#2a3942',
                                'border': '1px solid #3b4a54',
                                'color': '#e9edef',
                                'fontSize': '15px',
                            },
                            n_submit=0,
                        ),
                    ], style={'marginBottom': '15px'}),
                    dbc.Button(
                        'NEXT',
                        id='send-otp-btn',
                        color='success',
                        style={
                            'width': '100%',
                            'background': '#25D366',
                            'border': 'none',
                            'borderRadius': '24px',
                            'height': '48px',
                            'fontSize': '15px',
                            'fontWeight': '600',
                            'letterSpacing': '1px',
                        },
                        n_clicks=0,
                    ),
                    html.Div(
                        id='phone-error',
                        style={
                            'color': '#ff6b6b', 'textAlign': 'center',
                            'marginTop': '10px', 'fontSize': '13px',
                        },
                    ),
                ], id='phone-step', style={}),

                # OTP step
                html.Div([
                    html.H5(
                        'Verify your number',
                        style={
                            'color': '#e9edef', 'marginBottom': '15px',
                            'textAlign': 'center',
                        },
                    ),
                    html.P(
                        id='otp-sent-to',
                        style={
                            'color': '#8696a0', 'textAlign': 'center',
                            'fontSize': '13px', 'marginBottom': '10px',
                        },
                    ),
                    html.Div(
                        id='otp-dev-hint',
                        style={
                            'background': '#1a3026',
                            'border': '1px solid #25D366',
                            'borderRadius': '8px',
                            'padding': '10px 14px',
                            'marginBottom': '16px',
                            'display': 'none',
                            'textAlign': 'center',
                        },
                    ),
                    # Single 6-digit OTP input (reliable across all browsers)
                    dbc.Input(
                        id='otp-input',
                        placeholder='Enter 6-digit code',
                        type='text',
                        maxLength=6,
                        inputMode='numeric',
                        pattern='[0-9]*',
                        style={
                            'textAlign': 'center', 'fontSize': '28px',
                            'letterSpacing': '10px', 'fontWeight': '700',
                            'background': '#2a3942', 'border': '1px solid #3b4a54',
                            'color': '#e9edef', 'borderRadius': '8px',
                            'height': '60px', 'marginBottom': '20px',
                        },
                        n_submit=0,
                        debounce=False,
                        autofocus=True,
                    ),
                    dbc.Button(
                        'VERIFY',
                        id='verify-otp-btn',
                        color='success',
                        style={
                            'width': '100%',
                            'background': '#25D366',
                            'border': 'none',
                            'borderRadius': '24px',
                            'height': '48px',
                            'fontSize': '15px',
                            'fontWeight': '600',
                            'letterSpacing': '1px',
                        },
                        n_clicks=0,
                    ),
                    html.Div(
                        id='otp-error',
                        style={
                            'color': '#ff6b6b', 'textAlign': 'center',
                            'marginTop': '10px', 'fontSize': '13px',
                        },
                    ),
                    html.Br(),
                    html.A(
                        'Change number',
                        id='back-to-phone',
                        href='#',
                        style={
                            'color': '#25D366', 'textAlign': 'center',
                            'display': 'block', 'fontSize': '13px',
                        },
                    ),
                ], id='otp-step', style={'display': 'none'}),

            ], style={
                'background': '#1f2c34',
                'borderRadius': '16px',
                'padding': '40px',
                'width': '380px',
                'boxShadow': '0 8px 32px rgba(0,0,0,0.5)',
            }),
        ], style={
            'display': 'flex', 'justifyContent': 'center',
            'alignItems': 'center', 'height': '100vh',
        }),
    ], style={'background': '#0b141a', 'height': '100vh'})
