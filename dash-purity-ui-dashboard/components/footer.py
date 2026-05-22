from dash import html


def create_footer():
    return html.Footer(
        className="app-footer",
        children=[
            html.Span([
                "© 2025 ",
                html.A("budescode", href="https://github.com/budescode", target="_blank", rel="noopener noreferrer", className="footer-link"),
                ". Dash implementation, all rights reserved.",
            ]),
            html.Span(
                className="footer-right",
                children=[
                    "Built with ",
                    html.I(className="fa-solid fa-heart", style={"color": "#fc8181", "fontSize": "11px"}),
                    " by ",
                    html.A("Omonbude Emma", href="https://github.com/budescode", target="_blank", rel="noopener noreferrer", className="footer-link"),
                    html.Span(" · ", style={"margin": "0 4px", "opacity": "0.4"}),
                    html.A(html.I(className="fa-brands fa-github"), href="https://github.com/budescode", target="_blank", rel="noopener noreferrer", className="footer-icon-link", title="GitHub"),
                    html.A(html.I(className="fa-brands fa-linkedin"), href="https://www.linkedin.com/in/budescode", target="_blank", rel="noopener noreferrer", className="footer-icon-link", title="LinkedIn"),
                    html.Span(" · ", style={"margin": "0 4px", "opacity": "0.4"}),
                    "Design by ",
                    html.A("Creative Tim & Simmmple", href="https://www.figma.com/community/file/1020707462188017225", target="_blank", rel="noopener noreferrer", className="footer-link"),
                ],
            ),
        ],
    )
