#Create a function to display the word with a line before it with equal length to the word
def before(word):
  #Get the length of the word
  length = len(word)
  
  #Display the line and the word
  print("*" * length, word)

#Create a function to display the word with a line after it with equal length to the word
def after(word):
  #Get the length of the word
  length = len(word)
  
  #Display the word and the line
  print(word, "*" * length)
  
#Create a function to display the word with a line before and after it with equal length to the word
def both(word):
  #Get the length of the word
  length = len(word)
  
  #Display the word with the 2 lines either side of equal length to the word
  print("*" * length, word, "*" * length)
  
#Create a function to display the word with a line before and after it with equal length to the word in a grid of a specified size
def grid(word, grid_size):
  #Get the length of the word
  length = len(word)
  
  #Set the column counter to 0
  column_count = 0
  
  #Display the grid of the word with the lines of equal length either side
  while (column_count < grid_size):
    print("")
    column_count += 1
    count = 0
    while (count < grid_size):
      print("*" * length, word, "*" * length, "", end = "")
      count += 1