from reactpy import component, html
from .models import get_users


@component
def hello_world(recipient: str):
    def test(event):
        print(get_users())
        print(event)
    return html.div(html.button({"on_click": test}, "Test"))
