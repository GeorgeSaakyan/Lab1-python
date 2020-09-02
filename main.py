# Author: George Saakyan gxs5416@psu.edu
# Collaborator: Christian Torres ckt5298@psu.edu
# Collaborator: Manan Patel mxp5787@psu.edu

temperature = float(input("Enter temperature: "))
unit = input("Enter unit in F/f or C/c: ")
fahrenheit = (temperature * 9/5) + 32
celsius = ((temperature - 32) * 5/9)

if unit == "c" or unit == "C":
  print(f"{temperature}° in Celsius is equivalent to {fahrenheit}° Fahrenheit.")
elif unit == "f" or unit == "F":
  print(f"{temperature}° in Fahrenheit is equivalent to {celsius}° Celsius.")
else:
  print(f"Invalid unit({unit}).")