import random

def main():
  print("Keep it logically awesome.")
  # reading the file and its contents into an array
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  # generating a random number and then printing a line at that index in quites 
  last = random.randint(0, 33)
  for i in range(0, last):
    print(quotes[i].rstrip("\n"))
  # just opena file in append mode and add the line read from the user

if __name__== "__main__":
  main()
