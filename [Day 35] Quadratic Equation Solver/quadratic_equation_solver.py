import cmath

def quadratic_equation_solver(a,b,c):
    discriminant = b**2 - 4*a*c
    solution_1 = (-b - cmath.sqrt(discriminant)) / (2*a)
    solution_2 = (-b + cmath.sqrt(discriminant)) / (2*a)
    return [solution_1,solution_2]

def main():
    print(quadratic_equation_solver(12,3,6))

if __name__ == "__main__":
    main()