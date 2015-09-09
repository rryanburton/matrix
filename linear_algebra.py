class ShapeException(Exception):
    pass

def shape(vector):
    return (len(vector), )

# def vector_add(x, y):
#     final = []
#     a = x[0] + y[0]
#     final.append(a)
#
#     b = x[1] + y[1]
#     final.append(b)
#
#     c = x[2] + y[2]
#     final.append(c)
#     return final

# def vector_add(x, y):
#     final = [(x + y) for item in zip(x, y) ]

def vector_add(x, y):
    final = [(x[r] + y[r]) for r in range(len(x))]
    return final

def vector_sub(x, y):
    final = [(x[r] - y[r]) for r in range(len(x))]
    return final

def vector_sum(*something):

    print(list(zip(*something)))


def dot():
    pass
def vector_multiply():
    pass
def vector_mean():
    pass

def magnitude():
    pass
