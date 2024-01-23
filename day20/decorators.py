def another(*arg):
    print(4545453)


def decorator_test(func):
    # return another
    def wrapper(name, version):
        # print("Before function execution")
        n = f"My favorite language is {name}."
        v = f"Latest version is 😁😁"
        result = func(n, v)
        # print("After function execution")
        return result
    return wrapper


@decorator_test
def greet(name, version):
    print(name, version)
    # print(f"Hello, {name}!")
    pass


greet("Python", version="3.12")
