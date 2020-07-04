import random

def main():
  print("Keep it logically awesome.")
  # reading the file and its contents into an array
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  # generating a random number and then printing a line at that index in quites 
  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  main()
