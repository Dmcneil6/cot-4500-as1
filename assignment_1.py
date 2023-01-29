binary = "010000000111111010111001"

#decimal from binary
decimal = int(binary,2)
print("{:.5f}".format(decimal))
print("\n")

#Three digit-chopping
print('%.3f'% decimal)
print("\n")

#Three digit-rounding
print(round(decimal,3))
print("\n")

#absolute error and Relative error
rounded_value=round(decimal,3)
absolute_error= decimal - rounded_value
relative_error=(absolute_error/decimal)*100
print("Absolute error:",absolute_error)
print("\n")
print("Relative error:",relative_error)
print("\n")
import math

def ratio_test(x):
    # Initialize variables
    k = 1  
    a_k = ((-1)**k * x**k) / k**3
    ratio = math.inf
    
    # Loop until the ratio is less than 1
    while ratio > 1:
        k += 1
        a_k_1 = ((-1)**k * x**k) / k**3
        ratio = abs(a_k_1 / a_k)
        a_k = a_k_1
    
    # Return the minimum number of terms
    return k

print(ratio_test(1))
print("\n")

# Define the function to be solved
def f(x):
    return x**3 + 4*x**2 - 10

# Define the derivative of the function
def f_prime(x):
    return 3*x**2 + 8*x

# Define the Newton-Raphson method function
def newton_raphson(x_0, tol):
    # Initialize the current approximation
    x_n = x_0 - f(x_0)/f_prime(x_0)
    # Initialize the iteration count
    iterations = 0
    # Keep iterating until the tolerance is met
    while abs(f(x_n)) > tol:
        # Update the approximation
        x_n = x_n - f(x_n)/f_prime(x_n)
        # Increment the iteration count
        iterations += 1
    # Return the root and the number of iterations
    return x_n, iterations

# Set the initial guess and tolerance
x_0 = -4
tol = 1e-4
# Find the root and the number of iterations
root, iterations = newton_raphson(x_0, tol)
# Print the number of iterations
print("Number of iterations:", iterations)

