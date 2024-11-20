def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__

        for i, (arg, expected_type) in enumerate(annotations.items()):
            if i < len(args):
                if not isinstance(args[i], expected_type):
                    raise TypeError(f"Несоответствие типа аргумента {arg} должно быть: {expected_type}, а не: {type(args[i])}.")

        for arg, expected_type in kwargs.items():
            if arg in annotations and not isinstance(kwargs[arg], annotations[arg]):
                raise TypeError(f"Несоответствие типа аргумента {arg} должно быть: {annotations[arg]}, а не: {type(kwargs[arg])}.")

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# print(sum_two(1, 2))
# print(sum_two(1, 2.4))
