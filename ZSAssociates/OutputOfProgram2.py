def MainProgram(iterable, x):
    sample = tuple(iterable)
    n = len(sample)
    if not n and x:
        return
    indices = [1] * x
    yield tuple(sample[i] for i in indices)
    while True:
        for i in reversed(range(x)):
            if indices[i] != n-1:
                break
            else:
                return
        indices[i:] = [indices[i] + 1] * (x-i)
        yield tuple(sample[i] for i in indices)

a = MainProgram('PYTHON', 3)
print (next(a))

def MainProg(f):
    m = {}
    def InnerProg(num):
        if num not in m:
            m[num] = f(num)
        return m[num]
    return InnerProg

@MainProg
def Call(num):
    if num == 0:
        return 1
    else:
        return num**2*Call(num-1)
    
print (Call(3))