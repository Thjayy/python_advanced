a = 25
name = "Boburjon"


def func():
    name = "Javoxir"
    def inner_function():
        prefix = "Google"
        nonlocal name
        print(prefix, name)
        name = "Azizbek"
    inner_function()

func()
print(name)