import parallelize

def cube(x):
    return x*x*x

print parallelize.map(cube, [500, 9999, 123454321], 3)
