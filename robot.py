

# TODO: Decompose into functions
from os import close

'''
The move() calls the other def functions that have numbers as parameters.
The name I would use for the def move() would be run_game_moves()
'''
def move():
    
    size = 10
    degrees = 90
    length = 20
    width = 10
    c_degrees = 1
    c_length = 1
    number = 20
    
    move_square(size,degrees)
    move_rectangle(length,width,degrees)
    move_circle(c_length,c_degrees)
    move_square_dancing(length,degrees)
    Crop_circles(length, c_length,c_degrees)
              
'''
Created a def funtions that have a code of block with moving in a square sequance.
'''
def move_square(size,degrees):
    
    print("Moving in a square of size "+str(size))
    for i in range(4):
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")
        
        
'''
Created a def funtions that have a code of block with moving in a rectangle sequance
'''        
def move_rectangle(length,width,degrees):
   
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")
        
        
'''
Created a def funtions that have a code of block with moving in a circle sequance
'''        
def move_circle(degrees,length):
    
    print("Moving in a circle")
    for i in range(360):
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        
'''
Created a def funtions that have a code of block with moving in a 
square dancing sequance
'''        
def move_square_dancing(length,degrees):
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        print("* Move Forward "+str(length))
        move_square(length,degrees)
        
'''
Created a def funtions that have a code of block with moving in a 
crop circles sequance
'''    
def Crop_circles(number,length,degrees):
    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward "+str(number))
        move_circle(length,degrees)
        
        
def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
