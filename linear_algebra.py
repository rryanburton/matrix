import math

class ShapeException(Exception):
    print("sorry those don't work together")

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

def vector_sum(*args):
    final = [sum(x) for x in zip(*args)]
    return final



def dot():
    pass
def vector_multiply():
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

def vector_mean():
    pass

def magnitude(x):
    final = math.sqrt(sum([x[i]**2 for i in range(len(x))]))
    return final
