import matplotlib.pyplot as plt
import random
def add_tip(total, tip_percent):
    ''' Return the total amount including tip'''
    tip = tip_percent*total
    return total + tip
def hyp_length(leg_a, leg_b):
    ''' Return length of hypotenuse'''
    hyp_length = ((leg_a*leg_a)+(leg_b*leg_b))**.5
    return hyp_length

import math
def area_of_circle(r):
    """Function that defines an area of a circle"""
    a = r**2 * math.pi
    return a

print area_of_circle(1)

def getLetterGrade(score):
    score = round(score)
    if  score >= 90: return "A"
    if  90 < score >= 80: return "B"
    if  80 > score >= 70: return "C"
    if  70 > score >= 60: return "D"
    if  60 > score: return "F"

def circ_of_circle(r):
    return(2*3.14)*r
    
def Largest_numb(X,Y,Z):
    if X>=Y and X>=Z:
            print(X)
    if Y>X and Y>=Z:
            print(Y)
    if Z>X and Z>Y:
            print(Z)

def grade():
    score = int(input('insert score: '))
    
    if (score)>=90 and (score)<=100:
        print 'A'
    if (score)>=80 and (score)<90:
        print 'B'
    if (score)>=70 and (score)<80:
        print 'C'
    if (score)>=60 and (score)<70:
        print 'D'
    if (score)<=50 and (score)<60:
        print 'F'
        
def randomLetter():
    name = input("insert name: ")
    print (random.choice(name))
   
def how_eligible():
      essay=str(input("Insert submission here:  "))
      score = 0
      if '?' in essay:
          score=score+1
      if '"' in essay:
          score=score+1
      if ',' in essay:
          score=score+1
      if '!' in essay:
          score=score+1
      print (score) 
    
rollHistory = []
def dicegame():
    x= random.randint(1,6)
    y= random.randint(1,6)
    z= random.randint(1,6)
    
    a = (x,y,z)
    print a
    
    if x==y or y==z or z==x:
        print "you lose "
    else:
        print "you win"
    rollHistory.append(a)
    print rollHistory
    
def roll_hundred_pair():
    rolls = []
    for i in range(100):
        a = random.randint(1,6)
        b = random.randint(1,6)
        c = a+b
        rolls.append(c)
    plt.hist(rolls)
    plt.show()
    
            
def dice(number_of_dice):
    final_sum = 0
    for i in range(0,number_of_dice):
        final_sum += random.randint(1,6)
    return final_sum
import random
def goguess():
    tries = 1
    n = random.randint(1, 10)
    guess = int(raw_input("Enter an integer from 1 to 10: "))
    while n != "guess":
        tries += 1
        if guess < n:
            
            guess = int(raw_input("guess is low, Enter an integer from 1 to 10: "))
        elif guess > n:
       
            guess = int(raw_input("guess is high, Enter an integer from 1 to 10: "))
    
    print "it took you {} tries to guess the answer".format(tries)