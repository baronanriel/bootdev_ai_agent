import sys
from pkg.calculator import Calculator

if __name__ == "__main__":
    expression = " ".join(sys.argv[1:])
    calculator = Calculator()
    result = calculator.evaluate(expression)
    print(result)