from swole import Application
from swole.widgets import Input, Button, Markdown


Input()
Input(wide=False)
Input(placeholder="placeholder", wide=False)

Button("Button")
Button("Button", primary=True)

Markdown("Short Markdown")
Markdown("Super Super Super Super Super Super Super Super Super Super Super Super Super Super Super Super Super "
         "Super Super Long Markdown")


if __name__ == "__main__":
    Application().serve()
