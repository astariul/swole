from swole import Application, Ajax
from swole.widgets import Input, Button, Markdown


a = Input()
b = Input()
m = Markdown("Result : ")


def addition(a, b):
    m.content = "Result : {}".format(a + b)


aj = Ajax(addition, [a, b])


app = Application()
app.pages['/'].add(a)
app.pages['/'].add(b)
app.pages['/'].add(Button("Compute", onclick=aj))
app.pages['/'].add(m)


if __name__ == "__main__":
    app.serve()
