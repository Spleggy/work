try:
  print("Please enter first number")
  first_num = int(input())
  
  print("Please enter second number")
  second_num = int(input())
  
  answer = first_num / second_num
  print("Answer is", answer)

except ZeroDivisionError:
  print("Cannot divide by 0!")

except ValueError:
  print("Please enter whole numbers!")
  
except Exception:
  print("Something went wrong!")