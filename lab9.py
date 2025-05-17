import math
def phi(x):
    return (math.log(x))**2
def simple_iteration(x0, tol=1e-5, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_next = phi(x)
        if abs(x_next - x) < tol:
            return x_next
        x = x_next
    return x
root = simple_iteration(0.5)
print("Root:", root)
