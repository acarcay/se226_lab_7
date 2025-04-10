# calculator.py

import math_utils 

def run_calculator():
  print("Simple Calculator")
  print("Operations: +, -, *, /, ^ (power), % (mod)")

  operations = {
      '+': math_utils.add,
      '-': math_utils.subtract,
      '*': math_utils.multiply,
      '/': math_utils.divide,
      '^': math_utils.power,
      '%': math_utils.mod
  }

  try:
      num1_str = input("Enter the first number: ")
      num2_str = input("Enter the second number: ")
      op_symbol = input("Enter the operator (+, -, *, /, ^, %): ")

      num1 = float(num1_str)
      num2 = float(num2_str)

      if op_symbol in operations:
          calculation_function = operations[op_symbol]
          result = calculation_function(num1, num2)
          print(f"Result: {num1} {op_symbol} {num2} = {result}")
      else:
          print("Error: Invalid operator entered.")

  except ValueError:
      print("Error: Invalid input. Please enter valid numbers.")
  except Exception as e:
      print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
  print("--- Running calculator.py as main script ---")
  run_calculator()
  print("\n--- Testing calculator.py with direct calls (if needed) ---")
  print("Calculator script finished.")
