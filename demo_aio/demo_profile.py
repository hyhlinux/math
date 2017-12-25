# from cProfile import Profile
from vprof import runner
import math

# cProfile.run("main()", filename="my.profile")


def foo():
    return foo1()


def foo1():
    return foo2()


def foo2():
    return foo3()


def foo3():
    return foo4()


def foo4():
    return "this call tree seems ugly, but it always happen"


def bar():
    ret = 0
    for i in xrange(10000):
        ret += i * i + math.sqrt(i)
    return ret


def main():
    for i in range(10):
        if i % 2 == 0:
            print(bar())
        else:
            print(foo())

if __name__ == '__main__':
    main()
    # runner.run(foo, 'cmhp')
    # prof = Profile()
    # prof.runcall(main)
    # prof.print_stats()
    # prof.dump_stats('test.prof')  # dump profile result to test.prof
    # code for profile
