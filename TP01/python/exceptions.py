class MyException(Exception):
    pass


def g():
    print("g: start")
    raise MyException("some message")
    print("g: end")


def f():
    print("f: start")
    g()
    print("f: end")


def main():
    print("main: start")
    try:
        f()
    except MyException as e:
        print("Exception e was raised with message:", e)
    print("main: end")


main()
