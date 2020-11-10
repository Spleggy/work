import functions

#Ask user to enter a word
print("Please enter a word:")

#Read users response
word = str(input())

#Ask user to choose one of the options
print("""Please select one of the options from the list:
  1) Before
  2) After
  3) Both
  4) Grid
  """)
  
#Read user response
choice = int(input())

#Decide what function to use based on the choice
if (choice == 1):
  functions.before(word)
elif (choice == 2):
  functions.after(word)
elif (choice == 3):
  functions.both(word)
elif (choice == 4):
  #Ask user how big they want the grid
  print("How big do you want the grid?")
  
  #Read users response
  grid_size = int(input())
  
  functions.grid(word, grid_size)
else:
  print("That is an invalid choice!")