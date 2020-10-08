def decorators(*args, **kwargs):
    print(args, kwargs)

    def inner(func):
        return func

    return inner  # this is the fun_obj mentioned in the above content


@decorators('admin')
def greet():
    """
         function implementation
    """
    print('hello')


greet()

