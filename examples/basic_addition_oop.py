from swole import Application, Ajax, Page
from swole.widgets import Input, Button, Markdown


i_a = Input(label="First number")
i_b = Input(label="Second number")
m = Markdown("Result : ")


def addition(a, b):
    res = a + b
    m.set("Result : {}".format(res))
    if res == 42:
        i_a.set(42)
        i_b.set(42)


aj = Ajax(addition, [i_a, i_b])

p = Page()
p.add(i_a)
p.add(i_b)
p.add(Button("Compute", onclick=aj))
p.add(m)

# Alternative syntax
# with Page():
#     i_a = Input(label="First number")
#     i_b = Input(label="Second number")
#     m = Markdown("Result : ")

#     def addition(a, b):
#         res = a + b
#         m.set("Result : {}".format(res))
#         if res == 42:
#             i_a.set(42)
#             i_b.set(42)


#     aj = Ajax(addition, [i_a, i_b])
#     Button("Compute", onclick=aj)


if __name__ == "__main__":
    Application().serve()
