"""
ALL about send, yield DONT get confused again
When you first call next, the generator function actually starts
At first next(), the execution is at
jump = yield index (So here it yields index, 0)

At second next(),the other part gets called,
JUMP IS None
index += 1
yield index (So here it yields index 1)

At third iterator.send(2),
Execution had stopped at yield index of previous run.
As, jump = yield index (jump becomes 2 here, whatever you send it is the LHS of yield index)
index +=jump, index += 2
Then we yield index again , thus  yielding 3.
"""

def jumping_range(upto):
    index = 0
    while index < upto:
        print("INTO")
        jump = yield index
        print("JUMP IS {}".format(jump))
        if jump is None:
            jump = 1
        index += jump


if __name__ == "__main__":
    iterator = jumping_range(10)
    print(next(iterator))
    print(next(iterator))
    print(iterator.send(2))
    print(next(iterator))
