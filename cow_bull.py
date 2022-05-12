import random
name=input("Enter ur name-: ")
print("WELCOME",name)
l1 = [1, 2, 3, 4, 5, 6,7,8,9,0]
l2=random.sample(l1,5)
print(l2)
cow=[]
bull=[]
def cowbull():
    for i in range(1,11):
        num=int(input("guess a number-: "))
        pos=int(input("enter postion of ur number-: "))
        if num in l2:
            num_pos=l2.index(num)
            if pos==num_pos:
                bull.insert(num_pos,num)
                print("BULL:",bull)
            else:
                cow.append(num)
                print("COW:",cow)            
        else:
            print("u r number not in secret list")
        if i ==10:
            print("Finish")
            break
    if bull==l2:
        print("HURRAH! YOU ARE WINNER")
        play=input("DO YOU WANT TO PLAY AGAIN 'yes' OR 'no'")
        if play=='yes':
            cowbull()
        if play=='no':
            print("THANK FOR PLAY THIS GAME")
cowbull()
