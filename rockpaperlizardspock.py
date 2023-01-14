import random

# helper functions

def name_to_number(name):
    # Input:'name' string - one of rock, Spock, paper, lizard, scissors
    # Output: integer in the range 0 to 4, corresponding to input 'name' string
    
    if  name=='rock':
        number=0
    elif name=='Spock' or name=='spock':
        number=1
    elif name=='paper':
        number=2
    elif name=='lizard':
        number=3
    elif name=='scissors':
        number=4
    else:
        print("Oops! That's not choice!")
        print(".....try one of rock, Spock, paper, lizard, scissors.")
        number=100
        
    return number    


def number_to_name(number):
    # Input: integer in the range 0 to 4, corresponding to output 'name' string
    # Output:'name' string - one of rock, Spock, paper, lizard, scissors
    
    if  number==0:
        name='rock'
    elif number==1:
        name='Spock'
    elif number==2:
        name='paper'
    elif number==3:
        name='lizard'
    elif number==4:
        name='scissors'
    else:
        print("Oops! That number isn't an integer in the range 0 to 4!")
        name="name error"
    return name 

    

def rpsls(player_choice): 
    # Input:'name' string indicating player choice out of rock, Spock, paper, lizard, scissors
    # Output: none returned, text printed
    

    print("Player chooses " + player_choice)  

    player_number=name_to_number(player_choice) 
    
    if player_number<100:						
        comp_number=random.randrange(0, 5)      
        comp_choice=number_to_name(comp_number) 
    
        print("Computer chooses " + comp_choice) 
    
        winner_looser=(player_number-comp_number+2)%5-2  

        if winner_looser>0:  
            print("Player wins!")
        elif winner_looser<0:
            print("Computer wins!")
        elif winner_looser==0:
            print("Player and Computer tie!")
        else:
            print("Error!")
        
    return()

#main

toplay=True
while toplay:
	print("")
	player_choice = input("Choose paper, rock, lizard, scissors or Spock:")
	rpsls(player_choice)
	print("")
	player_cont = input("Carry on playing? [y/n]") 
	if player_cont == 'n' or player_cont == 'N':
		toplay=False 
	



