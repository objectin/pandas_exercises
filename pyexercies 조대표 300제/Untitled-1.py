def f(**kwargs, *args):
    print(kwargs)
    print(args)

print(f(index='0', 0))
