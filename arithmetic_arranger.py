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
    
    # Next create a list of num_1 and num_2 
    num1 = []
    num2 = []
    
    
  
  
  
  
