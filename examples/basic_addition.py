from swole import Application
from swole.widgets import Input, Button, Markdown


if __name__ == "__main__":
    app = Application()
    app.pages['/'].add(Input())
    app.pages['/'].add(Input())
    app.pages['/'].add(Button("Compute"))
    app.pages['/'].add(Markdown("Result : "))
    app.serve()