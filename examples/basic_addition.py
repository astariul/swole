from swole import Application, ajax
from swole.widgets import Input, Button, Markdown, Title


Title("Basic addition")
i_a = Input()
i_b = Input()
b = Button("Compute")
m = Markdown("Result : ")


@ajax(i_a, i_b)
def addition(a, b):
    res = a + b
    m.set("Result : {}".format(res))
    if res == 42:
        i_a.set(42)
        i_b.set(42)


b.onclick = addition


if __name__ == "__main__":
    Application().serve()
