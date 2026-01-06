def test(a, b, *args, c, d=10, **kwargs):
    print(a, b, args, c, d, kwargs)

def force_keyword_arguments(a, b, *, c, d):
    print(a, b, c, d)


test(1, 2, 3, 4, c=12)

force_keyword_arguments(1, 2, 12, 12)