def arithmetic_arranger(problems):
  
  # Starting by creating list of all the acceptable operators
  operators = []
  
  if len(problems) > 5:
    return "Error: Too many problems."
 
  for problem in range(len(problems)):
    if "+" in problems[problem]:
      operators.append("+")
     elif "-" in problems[problem]:
      operators.append("-")
     else:
      return "Error: Operator must be + or -."
    
    # append first and second num in diff var
    num1 = []
    num2 = []
    
    # Next operate based on num1[i] +/- num2[i]
    # How to show the calculation the way questions want ????
    # Print result
    
    
  
  
  
  
