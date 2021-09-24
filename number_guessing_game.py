#--------------------guess_the_hidden_no._game----------------------------
import random
n=random.randint(0,100)
print("guess the hidden number(hint: number < 100)")
print("total guesses you have:9")
guess = 9
while(True):
      g = int(input("your guess:"))
      if(g==n):
            print("VICTORY")
            break
      elif(guess==1):
            print("GAME OVER")
            break
      elif (g<n) :
            print("hidden number is bigger then this number")
            guess -= 1
            print("guesses left", guess)
      else:
            print("hidden number is smaller then this number")
            guess -= 1
            print("guesses left", guess)
print("the hidden number is :", n)
#-------------------------------end --------------------------------