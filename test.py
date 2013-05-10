import parallelize

def cube(x):
    return x*x*x

def small(x):
    if x < 1000:
        return x

args = [5, 494945884, 438584859505, 9494954] * 100

#print parallelize.map(cube, args, 3)
print parallelize.filter(small, args)
