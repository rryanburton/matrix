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
    # final = [(x[r] + y[r]) for r in range(len(x))]
    # return final
    final = [[x[r][s] + y[r][s]  for r in range(len(x[0]))] for s in range(len(x))]
    return final
def vector_sub(x, y):
    final = [(x[r] - y[r]) for r in range(len(x))]
    return final

def vector_sum(*something):
    sum = []
    # sum = [[something[row][col][othr] for col in range(len(something[0]))] for row in range(len(something)for othr in range(len(something)]
    print(list(zip(*something)))



def dot():
    pass
def vector_multiply():
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

def vector_mean():
    pass

def magnitude():
    pass
