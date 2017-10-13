import turtle #mod imports for turtle and random
import random

def ran(): 
    words = ["army", "laser", "ghost","family", "space", "python", "athens", "cake", "play", "dragon", "note", "video", "solar", "angel", "soda", "thones", "wolf", "iphone", "lander", "drone"]
    ran = int(random.uniform(0,20)) #The random number caller, selects word from lisst
    rw = words[ran] #This assigns the random number called from ran and applies it to words list index
    return rw # returns that word for later use
    
def screenlayout(rw): #This creates the screen, noose & unline lines
    screen = turtle.Screen() # creates screen layout
    #x = abs(screen.window_width()/2) Taken out of final code
    screen.setup(1000, 700) #Sets screen size work place
    screen.title("CSCI Hangman, by: Corey Carter") # Adds cool top banner message
    wline = turtle.Turtle() #These two generates the noose and underline turtles
    noose = turtle.Turtle()
    wline.speed(0) 
    noose.speed(0)
    
    wline.penup()
    noose.penup()
    
    wline.hideturtle()
    wline.goto(-225, -200)

    noose.hideturtle() # Creates noose
    noose.goto(100, 0)
    noose.pendown()
    noose.left(90)
    noose.forward(250)
    noose.left(90)
    noose.forward(150)

    #print(rw) #DISPLAYS THE RANDOMLY GENERATED WORD ON TERMINAL, USED FOR TESTING OR FOR EASIER GRADING!!!
    
    for i in range(len(rw)): #A for loop that creates enough lines based off of word length
        wline.pendown()
        #wline.forward(x/len(rw)) Taken out but it originally evenly distributed lines across screen size, hard to line up words. Took it out.
        wline.forward(50)
        wline.penup()
        #wline.forward(x/len(rw))
        wline.forward(50)

def parts(i): #Use to create head, body, arms and legs
    screen = turtle.Screen()
    head = turtle.Turtle()
    body = turtle.Turtle()
    legs = turtle.Turtle()
    head.speed(0)
    body.speed(0)
    legs.speed(0)
    legs.hideturtle()
    body.hideturtle()
    head.hideturtle()
    head.penup()
    body.penup()
    legs.penup()
    head.goto(-50, 150)
    body.goto(-50, 100)
    legs.goto(-50, 0)
    if i >= 1:
        if i == 1: #Head
            head.pendown()
            head.circle(50)
            head.penup()
        elif i == 2: #Body
            body.pendown()
            body.right(90)
            body.forward(100)
            body.left(90)
            body.goto(-50,150)
            body.penup()
        elif i == 3: #Right arm
            body.pendown()
            body.right(45)
            body.forward(75)
            body.penup()
            body.goto(-50,150)
            body.left(45)
        elif i == 4: #left arm
            body.pendown()
            body.left(225)
            body.forward(75)
            body.penup()
            body.goto(-50,150)
            body.right(45)
        elif i == 5: #Right leg
            legs.pendown()
            legs.right(45)
            legs.forward(75)
            legs.penup()
            legs.goto(-50, -100)
        elif i == 6: #left leg
            legs.pendown()
            legs.left(225)
            legs.forward(75)
            legs.penup()
            legs.goto(-50, -100)

def lose(): #If you lose
    lost = int(random.uniform(1,4)) #picks random number and choose a you lose image
    if lost == 1:
        lost = r"lost1.gif" #assigns image to variable
    elif lost == 2:
        lost = r"lost2.gif"
    elif lost == 3:
        lost = r"lost3.gif"
    turtle.addshape(lost) #Adds image to turtle environment
    turtle.shape(lost) #displays it
    l = turtle.Turtle()
    l.penup()
    l.hideturtle()
    l.goto(-120, -300)
    l.pendown()
    l.write("Sorry, you lose!", font=(20))

def win(): #If you win
    win = int(random.uniform(1,4)) #picks random number and choose a you win image
    if win == 1:
        tigerblood = r"win1.gif"
    elif win == 2:
        tigerblood = r"win2.gif"
    elif win == 3:
        tigerblood = r"win3.gif"
    turtle.addshape(tigerblood)
    turtle.shape(tigerblood)
    w = turtle.Turtle()
    w.penup()
    w.hideturtle()
    w.goto(-120, -300)
    w.pendown()
    w.write("Congratulations!!!", font=(20))

def replay(): #Used for after the endgame
    con = turtle.textinput("Want to play more!", "Would you like to continue? Y or N: ")
    if con == 'y' or con == 'Y' or len(con) > 1: #If you choose yes after game is over, it clears the screen, resets turtle object and reactivates hangman
        turtle.clearscreen()
        turtle.resetscreen()
        hangman()
    elif con == 'n' or con == '' or con == 'N':
        turtle.bye() #Kills turtle window

            
def hangman():
    rw = ran()#assigns word
    screenlayout(rw) # generates word lines & nooses.
    i = 0 #Accumulator loops
    #x = abs(turtle.window_width()/2)
    write = turtle.Turtle()
    write.hideturtle()
    write.penup()
    letter = '' #Creates null variable for strings
    while i < 6:
        text = turtle.textinput("Hangman", "Enter a lower-case letter: ") #input for guess
        if text in rw and len(text) == 1: #if the guessed string is in word and the guess is only 1 letter 
            if text not in letter: #If it isn't, then I add that string to the empty null variable, letter
                write.goto(-200, -200)
                letter += text
                p = rw.index(text) #This finds the position in the oringal string
                for u in range(p): #This writes it to the correct position
                    #write.forward((x/len(rw))*2)
                    write.forward(50)
                    write.forward(50)
                write.write(text, False, align="left", font=(10)) #This writes the string to the screen
                if len(letter) == len(rw): #If the letter equals the orignal length, you win. it activates win func
                    win()
                    i = 6 # kills the while loop after you win
            else:
                i += 1 #If the guessed string is already on the screen, it adds to 'i' and adds to a limb through parts func
                parts(i)
                if i == 6:
                    lose()
        elif text not in rw or text == '' or len(text) < 1: #If guessed string is not in oringal word it adds 1 to 'i' and add a limb
            i += 1
            parts(i)
            if i == 6:
                lose()
    replay() #starts the replay func
    
hangman() #this autostarts the file with opened
