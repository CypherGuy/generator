import random
import string

def generating():
  amount = int(input('Amount of nitro codes to generate: '))
  filename = input('Name of file: ')
  option = input('Show codes on screen?')
  nitrochoice = int(input("1 for Classic, 2 for Boost"))
  
  if nitrochoice == 2:
    codenum = 19
  else:
    codenum = 16

  if option.lower() == 'yes':
    value = 1
    counter = 1
    while value <= amount:
      code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=codenum))
      f = open(f'{filename}.txt', "a+")
      f.write(f'{code}\n')
      f.close()
      value += 1
      counter += 1
      print(f'{counter - 1}) {code}') 
      if counter == 69420:
        print("\n\nBelow is the golden code!\n\n")

  elif option.lower() == 'no':
    value = 1
    while value <= amount:
      code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
      f = open(f'{filename}.txt', "a+")
      f.write(f'{code}\n')
      f.close()
      value += 1
    print(f"Finished! {amount} codes produced.")
    
  else:
    print("Yes or no only next time.")
    print("\n")
    generating()

generating()
