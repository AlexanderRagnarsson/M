try:
    int(1.1)
except TypeError:
    a = {1:'1'}
    print(a[0])
except KeyError:
    print('hi')