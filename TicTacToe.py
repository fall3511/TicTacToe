<<<<<<< HEAD
import random


def main_menu():
        print("TIC TAC TOE")
        print()
        #Board
        a=[1,2,3,4,5,6,7,8,9]
        print(" ",a[0]," | ",a[1]," | ",a[2]," ")
        print("-----------------")
        print(" ",a[3]," | ",a[4]," | ",a[5]," ")
        print("-----------------")
        print(" ",a[6]," | ",a[7]," | ",a[8]," ")
        print()

        #MAIN MENU 
        print("___MAIN MENU___")
        print()
        print("SinglePlayer mode")
        print()
        print("Multiplayer mode")
        print()
        print("Tournament")
        print()
        print("For SinglePlayer mode enter 1")
        print()
        print("For Multiplayer mode enter 2")
        print()
        print("For Tournament mode enter 3")
        print()
        x=int(input("Enter number: "))
        print()
        #SinglePlayer mode
        if x==1:
                print("You have entered SinglePlayer mode")
                print()
                singleplayer()
        #Multiplayer mode
        elif x==2:
                print("You entered Multiplayer mode")
                print()
                multiplayer()
        #Tournament
        elif x==3:  
                Tournament()
def singleplayer():
        PL=str(input("Enter your name: "))
        C='Computer'
        print()
        print(PL,"vs",C)
        print()

        P11='X'
        P22='O'

        a=[1,2,3,4,5,6,7,8,9]
        print(" ",a[0]," | ",a[1]," | ",a[2]," ")
        print("-----------------")
        print(" ",a[3]," | ",a[4]," | ",a[5]," ")
        print("-----------------")
        print(" ",a[6]," | ",a[7]," | ",a[8]," ")
        print()

        toss=0

        if toss==0:
            print(C,"won the toss")
        else:
            print(PL,"won the toss")

        print()

        if toss==0:
            a[4]=P22
            print(" ",a[0]," | ",a[1]," | ",a[2]," ")
            print("-----------------")
            print(" ",a[3]," | ",a[4]," | ",a[5]," ")
            print("-----------------")
            print(" ",a[6]," | ",a[7]," | ",a[8]," ")
            print()

            for turns in range(9):
                k=int(input("Enter index location: "))
                if k==a[0]:
                    k=P11
                    a[0]=k 

                elif k==a[1]:
                    k=P11
                    a[1]=k
                      
                elif k==a[2]:
                    k=P11
                    a[2]=k      

                elif k==a[3]:
                    k=P11
                    a[3]=k
                  
                elif k==a[4]:
                    k=P11
                    a[4]=k
                 
                elif k==a[5]:
                    k=P11
                    a[5]=k
                            
                elif k==a[6]:
                    k=P11
                    a[6]=k

                elif k==a[7]:
                    k=P11
                    a[7]=k

                elif k==a[8]:
                    k=P11
                    a[8]=k
                    
                print(" ",a[0]," | ",a[1]," | ",a[2]," ")
                print("-----------------")
                print(" ",a[3]," | ",a[4]," | ",a[5]," ")
                print("-----------------")
                print(" ",a[6]," | ",a[7]," | ",a[8]," ")
                print()

                if turns==0:
                    if a[0]==k:
                        a[2]=P22
                        value='a0'

                    elif a[1]==k:
                        a[0]=P22
                        value='a1'

                    elif a[2]==k:
                        a[0]=P22
                        value='a2'

                    elif a[3]==k:             
                        a[0]=P22
                        value='a3'

                    elif a[5]==k:
                        a[2]=P22
                        value='a4'
                        
                    elif a[6]==k:
                        a[0]=P22
                        value='a5'
                        
                    elif a[7]==k:
                        a[6]=P22
                        value='a6'

                    elif a[8]==k:
                        a[6]=P22
                        value='a7' 
                           
                    print(" ",a[0]," | ",a[1]," | ",a[2]," ")
                    print("-----------------")
                    print(" ",a[3]," | ",a[4]," | ",a[5]," ")
                    print("-----------------")
                    print(" ",a[6]," | ",a[7]," | ",a[8]," ")
                    print()


                if turns==1:
                    if a[6]==k and value=='a0':
                        a[3]=P22
                        value='a0'
                    if not(a[6]==k) and value=='a0':
                        a[6]=P22 

                    if a[8]==k and value=='a1':
                        a[6]=P22  
                        value='a1'
                    if not(a[8]==k) and value=='a1':
                        a[8]=P22
                        
                    if a[8]==k and value=='a2':
                        a[5]=P22
                        value='a2'
                    if not(a[8]==k) and value=='a2':
                        a[8]=P22

                    if a[8]==k and value=='a3':             
                        a[2]=P22
                        value='a3'
                    if not(a[8]==k) and value=='a3':
                        a[8]=P22

                    if a[6]==k and value=='a4':
                        a[0]=P22
                        value='a4'
                    if not(a[6]==k) and value=='a4':
                        a[6]=P22
                        
                    if a[8]==k and value=='a5':
                        a[7]=P22
                        value='a5'
                    if not(a[8]==k) and value=='a5':
                        a[8]=P22
                        
                    if a[2]==k and value=='a6':
                        a[0]=P22
                        value='a6'
                    if not(a[2]==k) and value=='a6':
                        a[2]=P22

                    if a[2]==k and value=='a7':
                        a[5]=P22
                        value='a7'
                    if not(a[2]==k) and value=='a7':
                        a[2]=P22
                    
                    print(" ",a[0]," | ",a[1]," | ",a[2]," ")
                    print("-----------------")
                    print(" ",a[3]," | ",a[4]," | ",a[5]," ")
                    print("-----------------")
                    print(" ",a[6]," | ",a[7]," | ",a[8]," ")
                    print()

                    if a[0]==a[1]==a[2]==P22 or a[0]==a[4]==a[8]==P22 or a[0]==a[3]==a[6]==P22 or a[1]==a[4]==a[7]==P22 or \
                       a[2]==a[5]==a[8]==P22 or a[2]==a[4]==a[6]==P22 or a[3]==a[4]==a[5]==P22 or a[6]==a[7]==a[8]==P22:
                        print("Computer WON THE GAME")
                        break
                        print()
                
                if turns==2:
                    if a[5]==k and value=='a0':
                        a[1]=P22
                        value='a0'
                    if not(a[5]==k) and value=='a0':
                        a[5]=P22 

                    if a[2]==k and value=='a1':
                        a[3]=P22  
                        value='a1'
                    elif a[3]==k and value=='a1':
                        a[2]=P22  
                        value='a1'
                    elif not(a[3]==k and a[2]==k) and value=='a1':
                        a[2]=P22
                        
                    if a[3]==k and value=='a2':
                        a[7]=P22
                        value='a2'
                    if not(a[3]==k) and value=='a2':
                        a[3]=P22

                    if a[1]==k and value=='a3':             
                        a[6]=P22
                        value='a3'
                    elif a[6]==k and value=='a3':             
                        a[1]=P22
                        value='a3'   
                    elif not(a[1]==k and a[6]==k) and value=='a3':
                        a[1]=P22
                    
                    if a[1]==k and value=='a4':
                        a[8]=P22
                        value='a4'
                    elif a[8]==k and value=='a4':
                        a[1]=P22
                        value='a4'
                    elif not(a[1]==k and a[8]==k) and value=='a4':
                        a[8]=P22
                        
                    if a[1]==k and value=='a5':
                        a[5]=P22
                        value='a5'
                    if not(a[1]==k) and value=='a5':
                        a[1]=P22
                        
                    if a[3]==k and value=='a6':
                        a[8]=P22
                        value='a6'
                    elif a[8]==k and value=='a6':
                        a[3]=P22
                        value='a6'
                    elif not(a[3]==k and a[8]==k) and value=='a6':
                        a[3]=P22

                    if a[3]==k and value=='a7':
                        a[1]=P22
                        value='a7'
                    if not(a[3]==k) and value=='a7':
                        a[3]=P22
                    
                    print(" ",a[0]," | ",a[1]," | ",a[2]," ")
                    print("-----------------")
                    print(" ",a[3]," | ",a[4]," | ",a[5]," ")
                    print("-----------------")
                    print(" ",a[6]," | ",a[7]," | ",a[8]," ")
                    print()

                    if a[0]==a[1]==a[2]==P22 or a[0]==a[4]==a[8]==P22 or a[0]==a[3]==a[6]==P22 or a[1]==a[4]==a[7]==P22 or \
                       a[2]==a[5]==a[8]==P22 or a[2]==a[4]==a[6]==P22 or a[3]==a[4]==a[5]==P22 or a[6]==a[7]==a[8]==P22:
                        print("Computer WON THE GAME")
                        break
                        print()

                if turns==3:
                    if a[7]==k and value=='a0':
                        a[8]=P22
                    if a[8]==k and value=='a0':
                        a[7]=P22
                        

                    if a[1]==k and value=='a2':
                        a[6]=P22
                    if a[6]==k and value=='a2':
                        a[1]=P22

                    if a[3]==k and value=='a5':
                        a[2]=P22
                    if a[2]==k and value=='a5':
                        a[3]=P22
                      
                    if a[0]==k and value=='a7':
                        a[7]=P22
                    if a[7]==k and value=='a7':
                        a[0]=P22
                    
                    print(" ",a[0]," | ",a[1]," | ",a[2]," ")
                    print("-----------------")
                    print(" ",a[3]," | ",a[4]," | ",a[5]," ")
                    print("-----------------")
                    print(" ",a[6]," | ",a[7]," | ",a[8]," ")
                    print()

                    if a[0]==a[1]==a[2]==P22 or a[0]==a[4]==a[8]==P22 or a[0]==a[3]==a[6]==P22 or a[1]==a[4]==a[7]==P22 or \
                       a[2]==a[5]==a[8]==P22 or a[2]==a[4]==a[6]==P22 or a[3]==a[4]==a[5]==P22 or a[6]==a[7]==a[8]==P22:
                        print("Computer WON THE GAME")
                        break
                        print()
                
                    if not(a[0]==a[1]==a[2]==P22 or a[0]==a[4]==a[8]==P22 or a[0]==a[3]==a[6]==P22 or a[1]==a[4]==a[7]==P22 or \
                           a[2]==a[5]==a[8]==P22 or a[2]==a[4]==a[6]==P22 or a[3]==a[4]==a[5]==P22 or a[6]==a[7]==a[8]==P22 or \
                           a[0]==a[1]==a[2]==P11 or a[0]==a[4]==a[8]==P11 or a[0]==a[3]==a[6]==P11 or a[1]==a[4]==a[7]==P11 or \
                           a[2]==a[5]==a[8]==P11 or a[2]==a[4]==a[6]==P11 or a[3]==a[4]==a[5]==P11 or a[6]==a[7]==a[8]==P11):
                        print("It's a DRAW")
                        break
                        print()

        
                
                
def multiplayer():
    P1=str(input("Enter name of player 1: "))
    print()
    P2=str(input("Enter name of player 2: "))
    print()

    toss=random.randint(0,1)
    if toss==0:
        print(P1,"won the toss")    
        print()
    else:
        print(P2,"won the toss")
        print()
    print()
    s='x'
    t='o'

    print(P1,"Symbol is",s)
    print()
    print(P2,"Symbol is",t)
    print()

    P11=s
    P22=t

    a=[1,2,3,4,5,6,7,8,9]
    print(" ",a[0]," | ",a[1]," | ",a[2]," ")
    print("-----------------")
    print(" ",a[3]," | ",a[4]," | ",a[5]," ")
    print("-----------------")
    print(" ",a[6]," | ",a[7]," | ",a[8]," ")
    print() 
    if toss==0:
        k=int(input("Enter index location: "))

        if k==a[0]:
            k=P11
            a[0]=k  

        elif k==a[1]:
            k=P11
            a[1]=k
      
        elif k==a[2]:
            k=P11
            a[2]=k      

        elif k==a[3]:
            k=P11
            a[3]=k

        elif k==a[4]:
            k=P11
            a[4]=k

        elif k==a[5]:
            k=P11
            a[5]=k
            
        elif k==a[6]:
            k=P11
            a[6]=k

        elif k==a[7]:
            k=P11
            a[7]=k
        
        elif k==a[8]:
            k=P11
            a[8]=k

        print(" ",a[0]," | ",a[1]," | ",a[2]," ")
        print("-----------------")
        print(" ",a[3]," | ",a[4]," | ",a[5]," ")
        print("-----------------")
        print(" ",a[6]," | ",a[7]," | ",a[8]," ")
        print() 
        
    if toss==1:
        l=int(input("Enter index location: "))

        if l==a[0]:
            l=P22
            a[0]=l
      
        elif l==a[1]:
            l=P22
            a[1]=l
             
        elif l==a[2]:
            l=P22
            a[2]=l
     
        elif l==a[3]:
            l=P22
            a[3]=l
          
        elif l==a[4]:
            l=P22
            a[4]=l
      
        elif l==a[5]:
            l=P22
            a[5]=l

        elif l==a[6]:
            l=P22
            a[6]=l

        elif l==a[7]:
            l=P22
            a[7]=l

        elif l==a[8]:
            l=P22
            a[8]=l  

        print(" ",a[0]," | ",a[1]," | ",a[2]," ")
        print("-----------------")
        print(" ",a[3]," | ",a[4]," | ",a[5]," ")
        print("-----------------")
        print(" ",a[6]," | ",a[7]," | ",a[8]," ")
        print()

    for i in range(4):

        if toss==1:
            
            k=int(input("Enter index location: "))

            if k==a[0]:
                k=P11
                a[0]=k  

            elif k==a[1]:
                k=P11
                a[1]=k
          
            elif k==a[2]:
                k=P11
                a[2]=k      

            elif k==a[3]:
                k=P11
                a[3]=k
      
            elif k==a[4]:
                k=P11
                a[4]=k
     
            elif k==a[5]:
                k=P11
                a[5]=k
                
            elif k==a[6]:
                k=P11
                a[6]=k
       
            elif k==a[7]:
                k=P11
                a[7]=k
            
            elif k==a[8]:
                k=P11
                a[8]=k

            print(" ",a[0]," | ",a[1]," | ",a[2]," ")
            print("-----------------")
            print(" ",a[3]," | ",a[4]," | ",a[5]," ")
            print("-----------------")
            print(" ",a[6]," | ",a[7]," | ",a[8]," ")
            print() 

            if a[0]==a[1]==a[2]==P11 or a[0]==a[4]==a[8]==P11 or a[0]==a[3]==a[6]==P11 or a[1]==a[4]==a[7]==P11 or \
               a[2]==a[5]==a[8]==P11 or a[2]==a[4]==a[6]==P11 or a[3]==a[4]==a[5]==P11 or a[6]==a[7]==a[8]==P11:
                print(P1,"WON THE GAME")
                break
                print()

            l=int(input("Enter index location: "))

            if l==a[0]:
                l=P22
                a[0]=l
          
            elif l==a[1]:
                l=P22
                a[1]=l
                 
            elif l==a[2]:
                l=P22
                a[2]=l
         
            elif l==a[3]:
                l=P22
                a[3]=l
              
            elif l==a[4]:
                l=P22
                a[4]=l
          
            elif l==a[5]:
                l=P22
                a[5]=l

            elif l==a[6]:
                l=P22
                a[6]=l

            elif l==a[7]:
                l=P22
                a[7]=l

            elif l==a[8]:
                l=P22
                a[8]=l  

            print(" ",a[0]," | ",a[1]," | ",a[2]," ")
            print("-----------------")
            print(" ",a[3]," | ",a[4]," | ",a[5]," ")
            print("-----------------")
            print(" ",a[6]," | ",a[7]," | ",a[8]," ")
            print()

            if a[0]==a[1]==a[2]==P22 or a[0]==a[4]==a[8]==P22 or a[0]==a[3]==a[6]==P22 or a[1]==a[4]==a[7]==P22 or \
               a[2]==a[5]==a[8]==P22 or a[2]==a[4]==a[6]==P22 or a[3]==a[4]==a[5]==P22 or a[6]==a[7]==a[8]==P22:
                print(P2,"WON THE GAME")
                break
                print()
        if toss==0:
            l=int(input("Enter index location: "))

            if l==a[0]:
                l=P22
                a[0]=l
          
            elif l==a[1]:
                l=P22
                a[1]=l
                 
            elif l==a[2]:
                l=P22
                a[2]=l
         
            elif l==a[3]:
                l=P22
                a[3]=l
              
            elif l==a[4]:
                l=P22
                a[4]=l
          
            elif l==a[5]:
                l=P22
                a[5]=l

            elif l==a[6]:
                l=P22
                a[6]=l

            elif l==a[7]:
                l=P22
                a[7]=l

            elif l==a[8]:
                l=P22
                a[8]=l  

            print(" ",a[0]," | ",a[1]," | ",a[2]," ")
            print("-----------------")
            print(" ",a[3]," | ",a[4]," | ",a[5]," ")
            print("-----------------")
            print(" ",a[6]," | ",a[7]," | ",a[8]," ")
            print()

            if a[0]==a[1]==a[2]==P22 or a[0]==a[4]==a[8]==P22 or a[0]==a[3]==a[6]==P22 or a[1]==a[4]==a[7]==P22 or \
               a[2]==a[5]==a[8]==P22 or a[2]==a[4]==a[6]==P22 or a[3]==a[4]==a[5]==P22 or a[6]==a[7]==a[8]==P22:
                print(P2,"WON THE GAME")
                break
                print()
            k=int(input("Enter index location: "))

            if k==a[0]:
                k=P11
                a[0]=k  

            elif k==a[1]:
                k=P11
                a[1]=k
          
            elif k==a[2]:
                k=P11
                a[2]=k      

            elif k==a[3]:
                k=P11
                a[3]=k
      
            elif k==a[4]:
                k=P11
                a[4]=k
     
            elif k==a[5]:
                k=P11
                a[5]=k
                
            elif k==a[6]:
                k=P11
                a[6]=k
       
            elif k==a[7]:
                k=P11
                a[7]=k
            
            elif k==a[8]:
                k=P11
                a[8]=k

            print(" ",a[0]," | ",a[1]," | ",a[2]," ")
            print("-----------------")
            print(" ",a[3]," | ",a[4]," | ",a[5]," ")
            print("-----------------")
            print(" ",a[6]," | ",a[7]," | ",a[8]," ")
            print() 

            if a[0]==a[1]==a[2]==P11 or a[0]==a[4]==a[8]==P11 or a[0]==a[3]==a[6]==P11 or a[1]==a[4]==a[7]==P11 or \
               a[2]==a[5]==a[8]==P11 or a[2]==a[4]==a[6]==P11 or a[3]==a[4]==a[5]==P11 or a[6]==a[7]==a[8]==P11:
                print(P1,"WON THE GAME")
                break

    if not(a[0]==a[1]==a[2]==P22 or a[0]==a[4]==a[8]==P22 or a[0]==a[3]==a[6]==P22 or a[1]==a[4]==a[7]==P22 or \
           a[2]==a[5]==a[8]==P22 or a[2]==a[4]==a[6]==P22 or a[3]==a[4]==a[5]==P22 or a[6]==a[7]==a[8]==P22 or \
           a[0]==a[1]==a[2]==P11 or a[0]==a[4]==a[8]==P11 or a[0]==a[3]==a[6]==P11 or a[1]==a[4]==a[7]==P11 or \
           a[2]==a[5]==a[8]==P11 or a[2]==a[4]==a[6]==P11 or a[3]==a[4]==a[5]==P11 or a[6]==a[7]==a[8]==P11):
        print("It's a DRAW")
        print()
        
def Tournament():
        print("You entered Tournament")
        print()
        print("What type of Tournament you wanna play!")
        print()
        print("(1)BEST OUT OF 3","  ","(2)INFINITE MANY GAMES")
        print()
        print("For (1) enter 1")
        print()
        print("For (2) enter 2")
        print()
        r=int(input("Enter number for Games: "))

        if r==1:
                print("BEST OUT OF 3 GAME STARTED")
                for i in range(3):
                        multiplayer()
                
        elif r==2:
                print("INFINITE MANY GAMES STARTED")
                for i in range(100):
                        multiplayer()
                        print()
                        print("If you wanna EXIT TOURNAMENT enter 1 Otherwise enter 2")
                        r1=int(input("Enter 1 to EXIT or Enter 2 to CONTINUE Playing: "))
                        if r1==1:
                                break
                        print()
                        
def main():
        retry='Y'
        while retry=='y' or retry=='Y':
                print("Enter m to go to MAIN MENU")
                print()
                print("Enter e to EXIT the GAME")
                print()
                h=str(input("Enter what you wanna do: "))
                if h=='m':
                        main_menu()
                elif h=='e':
                        exit()
                        break
                else:
                        print("Invalid")
                        print()
                retry=input("Enter y to PLAY AGAIN or e to EXIT: ")
                print()
        exit()
def exit():
    print("You EXIT the game")
    print()


main()
=======
import random


def main_menu():
        print("TIC TAC TOE")
        print()
        #Board
        a=[1,2,3,4,5,6,7,8,9]
        print(" ",a[0]," | ",a[1]," | ",a[2]," ")
        print("-----------------")
        print(" ",a[3]," | ",a[4]," | ",a[5]," ")
        print("-----------------")
        print(" ",a[6]," | ",a[7]," | ",a[8]," ")
        print()

        #MAIN MENU 
        print("___MAIN MENU___")
        print()
        print("SinglePlayer mode")
        print()
        print("Multiplayer mode")
        print()
        print("Tournament")
        print()
        print("For SinglePlayer mode enter 1")
        print()
        print("For Multiplayer mode enter 2")
        print()
        print("For Tournament mode enter 3")
        print()
        x=int(input("Enter number: "))
        print()
        #SinglePlayer mode
        if x==1:
                print("You have entered SinglePlayer mode")
                print()
                singleplayer()
        #Multiplayer mode
        elif x==2:
                print("You entered Multiplayer mode")
                print()
                multiplayer()
        #Tournament
        elif x==3:  
                Tournament()
def singleplayer():
        PL=str(input("Enter your name: "))
        C='Computer'
        print()
        print(PL,"vs",C)
        print()

        P11='X'
        P22='O'

        a=[1,2,3,4,5,6,7,8,9]
        print(" ",a[0]," | ",a[1]," | ",a[2]," ")
        print("-----------------")
        print(" ",a[3]," | ",a[4]," | ",a[5]," ")
        print("-----------------")
        print(" ",a[6]," | ",a[7]," | ",a[8]," ")
        print()

        toss=0

        if toss==0:
            print(C,"won the toss")
        else:
            print(PL,"won the toss")

        print()

        if toss==0:
            a[4]=P22
            print(" ",a[0]," | ",a[1]," | ",a[2]," ")
            print("-----------------")
            print(" ",a[3]," | ",a[4]," | ",a[5]," ")
            print("-----------------")
            print(" ",a[6]," | ",a[7]," | ",a[8]," ")
            print()

            for turns in range(9):
                k=int(input("Enter index location: "))
                if k==a[0]:
                    k=P11
                    a[0]=k 

                elif k==a[1]:
                    k=P11
                    a[1]=k
                      
                elif k==a[2]:
                    k=P11
                    a[2]=k      

                elif k==a[3]:
                    k=P11
                    a[3]=k
                  
                elif k==a[4]:
                    k=P11
                    a[4]=k
                 
                elif k==a[5]:
                    k=P11
                    a[5]=k
                            
                elif k==a[6]:
                    k=P11
                    a[6]=k

                elif k==a[7]:
                    k=P11
                    a[7]=k

                elif k==a[8]:
                    k=P11
                    a[8]=k
                    
                print(" ",a[0]," | ",a[1]," | ",a[2]," ")
                print("-----------------")
                print(" ",a[3]," | ",a[4]," | ",a[5]," ")
                print("-----------------")
                print(" ",a[6]," | ",a[7]," | ",a[8]," ")
                print()

                if turns==0:
                    if a[0]==k:
                        a[2]=P22
                        value='a0'

                    elif a[1]==k:
                        a[0]=P22
                        value='a1'

                    elif a[2]==k:
                        a[0]=P22
                        value='a2'

                    elif a[3]==k:             
                        a[0]=P22
                        value='a3'

                    elif a[5]==k:
                        a[2]=P22
                        value='a4'
                        
                    elif a[6]==k:
                        a[0]=P22
                        value='a5'
                        
                    elif a[7]==k:
                        a[6]=P22
                        value='a6'

                    elif a[8]==k:
                        a[6]=P22
                        value='a7' 
                           
                    print(" ",a[0]," | ",a[1]," | ",a[2]," ")
                    print("-----------------")
                    print(" ",a[3]," | ",a[4]," | ",a[5]," ")
                    print("-----------------")
                    print(" ",a[6]," | ",a[7]," | ",a[8]," ")
                    print()


                if turns==1:
                    if a[6]==k and value=='a0':
                        a[3]=P22
                        value='a0'
                    if not(a[6]==k) and value=='a0':
                        a[6]=P22 

                    if a[8]==k and value=='a1':
                        a[6]=P22  
                        value='a1'
                    if not(a[8]==k) and value=='a1':
                        a[8]=P22
                        
                    if a[8]==k and value=='a2':
                        a[5]=P22
                        value='a2'
                    if not(a[8]==k) and value=='a2':
                        a[8]=P22

                    if a[8]==k and value=='a3':             
                        a[2]=P22
                        value='a3'
                    if not(a[8]==k) and value=='a3':
                        a[8]=P22

                    if a[6]==k and value=='a4':
                        a[0]=P22
                        value='a4'
                    if not(a[6]==k) and value=='a4':
                        a[6]=P22
                        
                    if a[8]==k and value=='a5':
                        a[7]=P22
                        value='a5'
                    if not(a[8]==k) and value=='a5':
                        a[8]=P22
                        
                    if a[2]==k and value=='a6':
                        a[0]=P22
                        value='a6'
                    if not(a[2]==k) and value=='a6':
                        a[2]=P22

                    if a[2]==k and value=='a7':
                        a[5]=P22
                        value='a7'
                    if not(a[2]==k) and value=='a7':
                        a[2]=P22
                    
                    print(" ",a[0]," | ",a[1]," | ",a[2]," ")
                    print("-----------------")
                    print(" ",a[3]," | ",a[4]," | ",a[5]," ")
                    print("-----------------")
                    print(" ",a[6]," | ",a[7]," | ",a[8]," ")
                    print()

                    if a[0]==a[1]==a[2]==P22 or a[0]==a[4]==a[8]==P22 or a[0]==a[3]==a[6]==P22 or a[1]==a[4]==a[7]==P22 or \
                       a[2]==a[5]==a[8]==P22 or a[2]==a[4]==a[6]==P22 or a[3]==a[4]==a[5]==P22 or a[6]==a[7]==a[8]==P22:
                        print("Computer WON THE GAME")
                        break
                        print()
                
                if turns==2:
                    if a[5]==k and value=='a0':
                        a[1]=P22
                        value='a0'
                    if not(a[5]==k) and value=='a0':
                        a[5]=P22 

                    if a[2]==k and value=='a1':
                        a[3]=P22  
                        value='a1'
                    elif a[3]==k and value=='a1':
                        a[2]=P22  
                        value='a1'
                    elif not(a[3]==k and a[2]==k) and value=='a1':
                        a[2]=P22
                        
                    if a[3]==k and value=='a2':
                        a[7]=P22
                        value='a2'
                    if not(a[3]==k) and value=='a2':
                        a[3]=P22

                    if a[1]==k and value=='a3':             
                        a[6]=P22
                        value='a3'
                    elif a[6]==k and value=='a3':             
                        a[1]=P22
                        value='a3'   
                    elif not(a[1]==k and a[6]==k) and value=='a3':
                        a[1]=P22
                    
                    if a[1]==k and value=='a4':
                        a[8]=P22
                        value='a4'
                    elif a[8]==k and value=='a4':
                        a[1]=P22
                        value='a4'
                    elif not(a[1]==k and a[8]==k) and value=='a4':
                        a[8]=P22
                        
                    if a[1]==k and value=='a5':
                        a[5]=P22
                        value='a5'
                    if not(a[1]==k) and value=='a5':
                        a[1]=P22
                        
                    if a[3]==k and value=='a6':
                        a[8]=P22
                        value='a6'
                    elif a[8]==k and value=='a6':
                        a[3]=P22
                        value='a6'
                    elif not(a[3]==k and a[8]==k) and value=='a6':
                        a[3]=P22

                    if a[3]==k and value=='a7':
                        a[1]=P22
                        value='a7'
                    if not(a[3]==k) and value=='a7':
                        a[3]=P22
                    
                    print(" ",a[0]," | ",a[1]," | ",a[2]," ")
                    print("-----------------")
                    print(" ",a[3]," | ",a[4]," | ",a[5]," ")
                    print("-----------------")
                    print(" ",a[6]," | ",a[7]," | ",a[8]," ")
                    print()

                    if a[0]==a[1]==a[2]==P22 or a[0]==a[4]==a[8]==P22 or a[0]==a[3]==a[6]==P22 or a[1]==a[4]==a[7]==P22 or \
                       a[2]==a[5]==a[8]==P22 or a[2]==a[4]==a[6]==P22 or a[3]==a[4]==a[5]==P22 or a[6]==a[7]==a[8]==P22:
                        print("Computer WON THE GAME")
                        break
                        print()

                if turns==3:
                    if a[7]==k and value=='a0':
                        a[8]=P22
                    if a[8]==k and value=='a0':
                        a[7]=P22
                        

                    if a[1]==k and value=='a2':
                        a[6]=P22
                    if a[6]==k and value=='a2':
                        a[1]=P22

                    if a[3]==k and value=='a5':
                        a[2]=P22
                    if a[2]==k and value=='a5':
                        a[3]=P22
                      
                    if a[0]==k and value=='a7':
                        a[7]=P22
                    if a[7]==k and value=='a7':
                        a[0]=P22
                    
                    print(" ",a[0]," | ",a[1]," | ",a[2]," ")
                    print("-----------------")
                    print(" ",a[3]," | ",a[4]," | ",a[5]," ")
                    print("-----------------")
                    print(" ",a[6]," | ",a[7]," | ",a[8]," ")
                    print()

                    if a[0]==a[1]==a[2]==P22 or a[0]==a[4]==a[8]==P22 or a[0]==a[3]==a[6]==P22 or a[1]==a[4]==a[7]==P22 or \
                       a[2]==a[5]==a[8]==P22 or a[2]==a[4]==a[6]==P22 or a[3]==a[4]==a[5]==P22 or a[6]==a[7]==a[8]==P22:
                        print("Computer WON THE GAME")
                        break
                        print()
                
                    if not(a[0]==a[1]==a[2]==P22 or a[0]==a[4]==a[8]==P22 or a[0]==a[3]==a[6]==P22 or a[1]==a[4]==a[7]==P22 or \
                           a[2]==a[5]==a[8]==P22 or a[2]==a[4]==a[6]==P22 or a[3]==a[4]==a[5]==P22 or a[6]==a[7]==a[8]==P22 or \
                           a[0]==a[1]==a[2]==P11 or a[0]==a[4]==a[8]==P11 or a[0]==a[3]==a[6]==P11 or a[1]==a[4]==a[7]==P11 or \
                           a[2]==a[5]==a[8]==P11 or a[2]==a[4]==a[6]==P11 or a[3]==a[4]==a[5]==P11 or a[6]==a[7]==a[8]==P11):
                        print("It's a DRAW")
                        break
                        print()

        
                
                
def multiplayer():
    P1=str(input("Enter name of player 1: "))
    print()
    P2=str(input("Enter name of player 2: "))
    print()

    toss=random.randint(0,1)
    if toss==0:
        print(P1,"won the toss")    
        print()
    else:
        print(P2,"won the toss")
        print()
    print()
    s='x'
    t='o'

    print(P1,"Symbol is",s)
    print()
    print(P2,"Symbol is",t)
    print()

    P11=s
    P22=t

    a=[1,2,3,4,5,6,7,8,9]
    print(" ",a[0]," | ",a[1]," | ",a[2]," ")
    print("-----------------")
    print(" ",a[3]," | ",a[4]," | ",a[5]," ")
    print("-----------------")
    print(" ",a[6]," | ",a[7]," | ",a[8]," ")
    print() 
    if toss==0:
        k=int(input("Enter index location: "))

        if k==a[0]:
            k=P11
            a[0]=k  

        elif k==a[1]:
            k=P11
            a[1]=k
      
        elif k==a[2]:
            k=P11
            a[2]=k      

        elif k==a[3]:
            k=P11
            a[3]=k

        elif k==a[4]:
            k=P11
            a[4]=k

        elif k==a[5]:
            k=P11
            a[5]=k
            
        elif k==a[6]:
            k=P11
            a[6]=k

        elif k==a[7]:
            k=P11
            a[7]=k
        
        elif k==a[8]:
            k=P11
            a[8]=k

        print(" ",a[0]," | ",a[1]," | ",a[2]," ")
        print("-----------------")
        print(" ",a[3]," | ",a[4]," | ",a[5]," ")
        print("-----------------")
        print(" ",a[6]," | ",a[7]," | ",a[8]," ")
        print() 
        
    if toss==1:
        l=int(input("Enter index location: "))

        if l==a[0]:
            l=P22
            a[0]=l
      
        elif l==a[1]:
            l=P22
            a[1]=l
             
        elif l==a[2]:
            l=P22
            a[2]=l
     
        elif l==a[3]:
            l=P22
            a[3]=l
          
        elif l==a[4]:
            l=P22
            a[4]=l
      
        elif l==a[5]:
            l=P22
            a[5]=l

        elif l==a[6]:
            l=P22
            a[6]=l

        elif l==a[7]:
            l=P22
            a[7]=l

        elif l==a[8]:
            l=P22
            a[8]=l  

        print(" ",a[0]," | ",a[1]," | ",a[2]," ")
        print("-----------------")
        print(" ",a[3]," | ",a[4]," | ",a[5]," ")
        print("-----------------")
        print(" ",a[6]," | ",a[7]," | ",a[8]," ")
        print()

    for i in range(4):

        if toss==1:
            
            k=int(input("Enter index location: "))

            if k==a[0]:
                k=P11
                a[0]=k  

            elif k==a[1]:
                k=P11
                a[1]=k
          
            elif k==a[2]:
                k=P11
                a[2]=k      

            elif k==a[3]:
                k=P11
                a[3]=k
      
            elif k==a[4]:
                k=P11
                a[4]=k
     
            elif k==a[5]:
                k=P11
                a[5]=k
                
            elif k==a[6]:
                k=P11
                a[6]=k
       
            elif k==a[7]:
                k=P11
                a[7]=k
            
            elif k==a[8]:
                k=P11
                a[8]=k

            print(" ",a[0]," | ",a[1]," | ",a[2]," ")
            print("-----------------")
            print(" ",a[3]," | ",a[4]," | ",a[5]," ")
            print("-----------------")
            print(" ",a[6]," | ",a[7]," | ",a[8]," ")
            print() 

            if a[0]==a[1]==a[2]==P11 or a[0]==a[4]==a[8]==P11 or a[0]==a[3]==a[6]==P11 or a[1]==a[4]==a[7]==P11 or \
               a[2]==a[5]==a[8]==P11 or a[2]==a[4]==a[6]==P11 or a[3]==a[4]==a[5]==P11 or a[6]==a[7]==a[8]==P11:
                print(P1,"WON THE GAME")
                break
                print()

            l=int(input("Enter index location: "))

            if l==a[0]:
                l=P22
                a[0]=l
          
            elif l==a[1]:
                l=P22
                a[1]=l
                 
            elif l==a[2]:
                l=P22
                a[2]=l
         
            elif l==a[3]:
                l=P22
                a[3]=l
              
            elif l==a[4]:
                l=P22
                a[4]=l
          
            elif l==a[5]:
                l=P22
                a[5]=l

            elif l==a[6]:
                l=P22
                a[6]=l

            elif l==a[7]:
                l=P22
                a[7]=l

            elif l==a[8]:
                l=P22
                a[8]=l  

            print(" ",a[0]," | ",a[1]," | ",a[2]," ")
            print("-----------------")
            print(" ",a[3]," | ",a[4]," | ",a[5]," ")
            print("-----------------")
            print(" ",a[6]," | ",a[7]," | ",a[8]," ")
            print()

            if a[0]==a[1]==a[2]==P22 or a[0]==a[4]==a[8]==P22 or a[0]==a[3]==a[6]==P22 or a[1]==a[4]==a[7]==P22 or \
               a[2]==a[5]==a[8]==P22 or a[2]==a[4]==a[6]==P22 or a[3]==a[4]==a[5]==P22 or a[6]==a[7]==a[8]==P22:
                print(P2,"WON THE GAME")
                break
                print()
        if toss==0:
            l=int(input("Enter index location: "))

            if l==a[0]:
                l=P22
                a[0]=l
          
            elif l==a[1]:
                l=P22
                a[1]=l
                 
            elif l==a[2]:
                l=P22
                a[2]=l
         
            elif l==a[3]:
                l=P22
                a[3]=l
              
            elif l==a[4]:
                l=P22
                a[4]=l
          
            elif l==a[5]:
                l=P22
                a[5]=l

            elif l==a[6]:
                l=P22
                a[6]=l

            elif l==a[7]:
                l=P22
                a[7]=l

            elif l==a[8]:
                l=P22
                a[8]=l  

            print(" ",a[0]," | ",a[1]," | ",a[2]," ")
            print("-----------------")
            print(" ",a[3]," | ",a[4]," | ",a[5]," ")
            print("-----------------")
            print(" ",a[6]," | ",a[7]," | ",a[8]," ")
            print()

            if a[0]==a[1]==a[2]==P22 or a[0]==a[4]==a[8]==P22 or a[0]==a[3]==a[6]==P22 or a[1]==a[4]==a[7]==P22 or \
               a[2]==a[5]==a[8]==P22 or a[2]==a[4]==a[6]==P22 or a[3]==a[4]==a[5]==P22 or a[6]==a[7]==a[8]==P22:
                print(P2,"WON THE GAME")
                break
                print()
            k=int(input("Enter index location: "))

            if k==a[0]:
                k=P11
                a[0]=k  

            elif k==a[1]:
                k=P11
                a[1]=k
          
            elif k==a[2]:
                k=P11
                a[2]=k      

            elif k==a[3]:
                k=P11
                a[3]=k
      
            elif k==a[4]:
                k=P11
                a[4]=k
     
            elif k==a[5]:
                k=P11
                a[5]=k
                
            elif k==a[6]:
                k=P11
                a[6]=k
       
            elif k==a[7]:
                k=P11
                a[7]=k
            
            elif k==a[8]:
                k=P11
                a[8]=k

            print(" ",a[0]," | ",a[1]," | ",a[2]," ")
            print("-----------------")
            print(" ",a[3]," | ",a[4]," | ",a[5]," ")
            print("-----------------")
            print(" ",a[6]," | ",a[7]," | ",a[8]," ")
            print() 

            if a[0]==a[1]==a[2]==P11 or a[0]==a[4]==a[8]==P11 or a[0]==a[3]==a[6]==P11 or a[1]==a[4]==a[7]==P11 or \
               a[2]==a[5]==a[8]==P11 or a[2]==a[4]==a[6]==P11 or a[3]==a[4]==a[5]==P11 or a[6]==a[7]==a[8]==P11:
                print(P1,"WON THE GAME")
                break

    if not(a[0]==a[1]==a[2]==P22 or a[0]==a[4]==a[8]==P22 or a[0]==a[3]==a[6]==P22 or a[1]==a[4]==a[7]==P22 or \
           a[2]==a[5]==a[8]==P22 or a[2]==a[4]==a[6]==P22 or a[3]==a[4]==a[5]==P22 or a[6]==a[7]==a[8]==P22 or \
           a[0]==a[1]==a[2]==P11 or a[0]==a[4]==a[8]==P11 or a[0]==a[3]==a[6]==P11 or a[1]==a[4]==a[7]==P11 or \
           a[2]==a[5]==a[8]==P11 or a[2]==a[4]==a[6]==P11 or a[3]==a[4]==a[5]==P11 or a[6]==a[7]==a[8]==P11):
        print("It's a DRAW")
        print()
        
def Tournament():
        print("You entered Tournament")
        print()
        print("What type of Tournament you wanna play!")
        print()
        print("(1)BEST OUT OF 3","  ","(2)INFINITE MANY GAMES")
        print()
        print("For (1) enter 1")
        print()
        print("For (2) enter 2")
        print()
        r=int(input("Enter number for Games: "))

        if r==1:
                print("BEST OUT OF 3 GAME STARTED")
                for i in range(3):
                        multiplayer()
                
        elif r==2:
                print("INFINITE MANY GAMES STARTED")
                for i in range(100):
                        multiplayer()
                        print()
                        print("If you wanna EXIT TOURNAMENT enter 1 Otherwise enter 2")
                        r1=int(input("Enter 1 to EXIT or Enter 2 to CONTINUE Playing: "))
                        if r1==1:
                                break
                        print()
                        
def main():
        retry='Y'
        while retry=='y' or retry=='Y':
                print("Enter m to go to MAIN MENU")
                print()
                print("Enter e to EXIT the GAME")
                print()
                h=str(input("Enter what you wanna do: "))
                if h=='m':
                        main_menu()
                elif h=='e':
                        exit()
                        break
                else:
                        print("Invalid")
                        print()
                retry=input("Enter y to PLAY AGAIN or e to EXIT: ")
                print()
        exit()
def exit():
    print("You EXIT the game")
    print()


main()
>>>>>>> 4b4295cf193a0fab08da6f7df7fb9b917323ded6
