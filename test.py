import parallelize

def cube(x):
    return x*x*x

args = [9345945, 494945884, 438584859505, 9494954] * 1000000

print parallelize.map(cube, args, 3)
