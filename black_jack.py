import random
deck_type=  ["Hearts", "Spades", "Clubs", "Diamonds"]
deck_value= ["Ace","2","3","4","5","6","7","8","9","Jack","Queen","King" ]

def pull(a):
    if a > 1:
        card1_value= random.randint(0,11)
        card1_type= random.randint(0,3)
        card1= deck_value[card1_value ] + " of " + deck_type [card1_type ] 
        if card1_value>10:
            card1_value=10
        return card1,card1_value

def check(a,dealer):
    if a>=21 or (a<dealer and dealer<21):
          return False
    elif a<21 and a>dealer:
        return True
    elif dealer>21:
         return True

def bidding_level(bid):
     if bid> 0 and bid<100:
          return "Low level bid"
     elif bid> 100 and bid<500:
          return "middle level bid"
     elif bid>500:
          return "high level bid"

print(pull(2)[0])

cards=[]

start=input("Ready?")
count = 2 
first= True
end= False
val = 0
bid= 0 
while start == "yes" or "y" and end==False:
    bid=input("What is your starting bid?")
    if first== True:
         dealer= pull(2)[1]
         cards.append(pull(2)[0])
         val =val + pull(2)[1]
    cards.append(pull(2)[0])
    dealer= dealer + pull(2)[1]
    print(dealer)
    print(cards)
    

    for i in range(count):
            if check(val,dealer)== False and first== False:
                print("lose")
            elif check(val,dealer)== True and first== False:
                 print("win")
            first=False
            another = input("Would you like another card?")
            if another == "y":
                 print(check(val,dealer))
                 break
            elif another == "n":
                 print(check(val,dealer))
                 end=True
                 break
            count= count + 1 
    print()
    