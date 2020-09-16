from swole import Application, Ajax
from swole.widgets import Input, Button, Markdown


i_a = Input()
i_b = Input()
m = Markdown("Result : ")


def addition(a, b):
    res = a + b
    m.set("Result : {}".format(res))
    if res == 42:
        i_a.set(42)
        i_b.set(42)


aj = Ajax(addition, [i_a, i_b])


app = Application()
app.pages['/'].add(i_a)
app.pages['/'].add(i_b)
app.pages['/'].add(Button("Compute", onclick=aj))
app.pages['/'].add(m)


if __name__ == "__main__":
    app.serve()
