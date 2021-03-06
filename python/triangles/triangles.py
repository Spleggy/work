import math
def validate(first, second, third):
  valid = 0
  if ((first >= second) and (first >= third) and ((second + third) > first)):
    valid = 1
  elif ((second >= first) and (second >= third) and ((first + third) > second)):
    valid = 1
  elif ((third >= second) and (third >= first) and ((second + first) > third)):
    valid = 1
  else:
    valid = 0
  return valid
  
def identify(first, second, third):
  valid = validate(first, second, third)
  triangle = ""
  if (valid == 1):
    if ((first == second) and (second == third)):
      triangle = "equilateral"
      print("This triangle is", triangle)
    elif ((first == second) or (first == third) or (second == third)):
      triangle = "isosceles"
      print("This triangle is", triangle)
    elif((first != second) or (first != third) or (second != third)):
      triangle = "scalene"
      print("This triangle is", triangle)
  else:
    print("Not a valid triangle!")
  return triangle

def calcPerimeter(first, second, third):
  valid = validate(first, second, third)
  if (valid == 1):
    perimeter = first + second + third
    print("\nPerimeter is", perimeter)
  else:
    print("\nTriangle not valid!")
    perimeter = first + second + third
  return perimeter

def calcArea(first, second, third):
  answer = 0
  triangle = identify(first, second, third)
  
  if ((triangle == "isosceles")):
    if (second == third):
      base = first
      height = math.sqrt(((second) ** 2) - ((0.5 * base) ** 2))
      answer = 0.5 * base * height
    elif (first == third):
      base = second
      height = math.sqrt(((first) ** 2) - ((0.5 * base) ** 2))
      answer = 0.5 * base * height
    else:
      base = third
      height = math.sqrt(((second) ** 2) - ((0.5 * base) ** 2))
      answer = 0.5 * base * height
  
  if (triangle == "equilateral"):
    answer = ((first ** 2) * math.sqrt(3)) / 4
  
  if (triangle == "scalene"):
    s = (first + second + third) / 2
    answer = math.sqrt(s * (s - first) * (s - second) * (s - third))
    
  print("Area is", round(answer, 2))
  return answer
    
def draw(first, second, third):
  perimeter = calcPerimeter(first, second, third)  
  valid = validate(first, second, third)
  
  if ((perimeter.is_integer) and (valid == 1)):
    perimeter = int(perimeter)
    print("")
    for count in range(perimeter):
      print(" " * (perimeter - count - 1) + "* " * (count + 1))
  
def run():
  #Ask user for each side of a triangle
  print("What is the size of the first side?")
  
  #Read users response
  firstSide = float(input())
  
  print("What is the size of the second side?")
  secondSide = float(input())
  
  print("What is the size of the third size?")
  thirdSide = float(input())
  
  #Ask user which option they want
  print("""What option do you want?
  1) Validate 
  2) Identify 
  3) Calculate Perimeter 
  4) Calculate Area 
  5) Draw equilateral triangle with side of perimeter of given sides (rounds to nearest whole number)""")
  
  #Read users response
  choice = int(input())
  
  if (choice == 1):
    valid = validate(firstSide, secondSide, thirdSide)
    if (valid == 1):
      print("Valid")
    else:
      print("Not Valid")
  elif (choice == 2):
    identify(firstSide, secondSide, thirdSide)
  elif (choice == 3):
    calcPerimeter(firstSide, secondSide, thirdSide)
  elif (choice == 4):
    calcArea(firstSide, secondSide, thirdSide)
  elif (choice == 5):
    draw(firstSide, secondSide, thirdSide)  
  else:
    print("That is not a valid choice!")
    
run()


