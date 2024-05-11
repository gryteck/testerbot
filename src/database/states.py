class State:
    def __get__(self, instance, owner):
        return f'{owner.__name__}.{self.name}'

    def __set_name__(self, owner, name):
        self.name = name


class States:
    start = State()
