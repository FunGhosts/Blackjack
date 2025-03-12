import random
deck_type=  ["Hearts", "Spades", "Clubs", "Diamonds"]
deck_value= ["Ace","2","3","4","5","6","7","8","9","Jack","Queen","King" ]

def pull(a,val):
    if a > 1:
        global card1_value
        card1_value= random.randint(0,11)
        card1_type= random.randint(0,3) 
        card1= deck_value[card1_value ] + " of " + deck_type [card1_type ] 
        card1_value = card1_value + 1
        if card1_value>10:
            card1_value=10
        elif card1_value==1 and val<10:
          card1_value= 11
        return card1,card1_value


def check(a,dealer):
    global status
    if a>21 or (a<dealer and dealer<21):
          status= "lose"
    elif a<=21 and a>dealer:
        status= "win"
    elif dealer>21:
         status= "win"
    return status

def bidding_level(bid):
     if bid> 0 and bid<100:
          return "Low level bid"
     elif bid> 100 and bid<500:
          return "middle level bid"
     elif bid>500:
          return "high level bid"
     
def bidding(bid,pocket,start,win):
     global pot 
     pot = 0
     bid = int(bid)
     pot= pot+bid
     pocket = pocket - bid
     if start == 'n' and win == 1:
          pocket = pocket + (pot*2)
          pot = 0
     return pocket


print(pull(2,0)[0])

cards=[]
pocket= int(input("How much would you like to have on the table? (buy in is 10,000)"))


start=input("Ready?")
count = 2 
first= True
end= False
val = 0
win = 0
bid= 0 
while start == "yes" or "y" and end==False:
    bid=input("What is your starting bid?")
    pocket = bidding(bid,pocket,start,win)
    if first== True:
         dealer= pull(2,val)[1]
         cards.append(pull(2,val)[0])
         val =val + card1_value
         print(card1_value)
         print(val)
    cards.append(pull(2,val)[0])
    val =val + card1_value
    print(val)

    dealer= dealer + pull(2,val)[1]
    print(dealer)
    print(cards)
    print(val)
    print(pot)
    check(val, dealer)

    for i in range(count, count + 1) :
            if check(val,dealer)== "lose" and first== False:
                print("lose")
            elif check(val,dealer)== "win" and first== False:
                 win = 1
                 print("you win", pot*2)
                 pocket= pocket + pot*2
            first=False
            print("The pot is: ", pot)
            print("you have", pocket)
            another = input("Would you like another card?")
            if another == "y":
                 print(check(val,dealer))
                 break
            elif another == "n" :
                 print(check(val,dealer))
                 end=True
                 start= "n"
                 count= -1
                 break
            elif another == "fold":
               end= True 
               count= -1
               fold = True
               print("folded")
               start= "n"
               break
            if win == 1:
               pocket= bidding(bid, pocket, start, win)
               
print("you have ",pocket)