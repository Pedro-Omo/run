def callref(x=10, y=20, *args, **kwargs):
    print(x)
    print(y)
    print(*args)
    print(**kwargs)
callref(10, 20, 25, 30, 40, 45)