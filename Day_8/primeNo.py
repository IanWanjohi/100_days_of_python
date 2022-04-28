#Write your code below this line 👇

def prime_checker(number):

  is_prime = True
  
  for i in range(2, number - 1):
    div = number % i
    
    if div == 0:
      is_prime = False
  

  if is_prime == True:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

#Write your code above this line 👆

    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
