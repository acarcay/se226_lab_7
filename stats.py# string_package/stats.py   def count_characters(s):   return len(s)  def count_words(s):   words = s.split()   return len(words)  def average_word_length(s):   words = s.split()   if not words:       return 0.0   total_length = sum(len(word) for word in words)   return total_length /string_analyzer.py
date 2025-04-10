# math_utils.py


def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    return "Error: Division by zero is not allowed."
  try:
    result = x / y
    return result
  except ZeroDivisionError:
      return "Error: Division by zero occurred."


def power(x, y):
  return x ** y

def mod(x, y):
  if y == 0:
      return "Error: Modulo by zero is not allowed."
  try:
      result = x % y
      return result
  except ZeroDivisionError:
      return "Error: Modulo by zero occurred."

# Test cases when running the module directly
if __name__ == "__main__":
  print("--- Testing math_utils.py ---")
  print(f"add(10, 5) = {add(10, 5)}")          # Expected: 15
  print(f"subtract(10, 5) = {subtract(10, 5)}")  # Expected: 5
  print(f"multiply(10, 5) = {multiply(10, 5)}")  # Expected: 50
  print(f"divide(10, 5) = {divide(10, 5)}")      # Expected: 2.0
  print(f"divide(10, 0) = {divide(10, 0)}")      # Expected: Error message
  print(f"power(2, 3) = {power(2, 3)}")          # Expected: 8
  print(f"power(5, 0) = {power(5, 0)}")          # Expected: 1
  print(f"mod(10, 3) = {mod(10, 3)}")           # Expected: 1
  print(f"mod(10, 0) = {mod(10, 0)}")           # Expected: Error message
  print("--- End of math_utils.py tests ---")
