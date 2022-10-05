xpos = 200 # this is a variable for the x axis of the ball
ypos = 200 # this is a variable for the y axis of the ball
xvol = 0 # this variable allows the program to adjust the speed of which the x axis moves
yvol = 0 # this variable allows the program to adjust the speed of which the x axis moves
back1 = 28 # this a variable to allow the table to change colors
back2 = 162# this a variable to allow the table to change colors
back3 = 53# this a variable to allow the table to change colors
def table():# the table function draws the table in the sketch window when the program runs
     fill(98,65,30)
     rect(0,360,800,800)
     rect(0,0,800,40)
     rect(0,0,40,800)
     rect(760,0,50,800)
     fill(0,0,0)
     circle(770,35,50)
     circle(30,35,50)
     circle(30,365,50)
     circle(770,365,50)
     circle(400,35,50)
     circle(400,365,50)
def queue():# the queue function draws a queue that follows the x and y parameters of the mouse so it can move using the mouse
     fill(170,111,38)
     rect (mouseX,mouseY,200,10)

def ball(): # the ball funvtion draws and fills the ball using the variables definied at the beginning so the ball can move positions at different speeds
    global xpos,ypos,xvol,yvol
    fill(56,195,232)
    circle(xpos,ypos,20)

def setup(): # def setup is a onetime function to set up anything in the program I don't want running in a loop, in this case it's just the size of the sketch window
    size(800,400)


def draw(): # def draw is the loop I used to create the rest of the components of the game
    global table, queue, xpos,ypos,xvol,yvol,back1,back2,back3 # making the variables and functions global allows me to use them in the def draw loop  
    background (back1,back2,back3) #this sets the background color of the table, using the variables I am able to change the color later in the code
    table() # this draws the table
    queue() # this draws the queue
    ball() # this draws the ball
    xpos+=xvol # this line basically declares that in the def draw loop, the x position of the ball equals the x position + the x velocity allowing me to change the speed of which the ball moves
    ypos+=yvol # this line does the same thing but for the y axis
    xvol/=1.007 # these two equations creates a small amount of drag so the ball gradually slows down 
    yvol/=1.007
    if xpos - 12 <=  mouseX and xpos >= mouseX - 12 and ypos <= mouseY + 12 and ypos >= mouseY - 12: # the next six if staments divide the queue into four quadrants and two edges, basically telling the program the depending on which quadrant/edge the queue the ball will move in the respective direction
       xvol+=-1 # this if statement controls the left edge
    elif xpos + 10 >=  mouseX + 200 and xpos <= mouseX + 210 and ypos <= mouseY + 10 and ypos >= mouseY - 10:
        xvol+=1 # this if statement controls the right edge
    elif xpos - 10 <=  mouseX + 100 and xpos >= mouseX and ypos + 10 <= mouseY + 5 and ypos >= mouseY - 12:
        xvol+=-1 # this if statement controls the top left quadrant
        yvol+=-0.5
    elif xpos - 10 <=  mouseX + 100 and xpos >= mouseX and ypos - 2 <= mouseY + 20 and ypos >= mouseY + 5:
        xvol+=-1 #this if statement controls the bottom left quadrant
        yvol+=0.5
    elif xpos - 10  >=  mouseX + 120 and xpos <= mouseX + 200 and ypos + 7 <= mouseY + 5 and ypos >= mouseY - 10:
        xvol+=1 # this controls the top right quadrant
        yvol+=-0.5
    elif xpos - 10 >=  mouseX + 120 and xpos <= mouseX + 200 and ypos - 2 <= mouseY + 20 and ypos >= mouseY + 5:
        xvol+=1# this controls the bottom right quadrant
        yvol+=0.5
    if xpos > 750: # the next 4 if statements set the table boundries for the ball, telling it to reverse velocity once it collides with one of the sides
        xvol*=-1 #this controls the right edge of the table
    if xpos < 50:# this controls the left edge
        xvol*=-1
    if ypos < 50:#this controls the top
        yvol*=-1
    if ypos > 350:#this controls the bottom
        yvol*=-1
    if xpos <= 770 and xpos >= 730 and ypos <= 60 and ypos >= 30 or xpos <= 60 and xpos >= 30 and ypos <= 60 and ypos >= 30 or xpos <= 60 and xpos >= 30 and ypos <= 365 and ypos >= 335 or xpos <= 770 and xpos >= 730 and ypos <=365 and ypos >= 335 or xpos <= 400 and xpos >= 370 and ypos <= 80 and ypos >= 30 or xpos <= 400 and xpos >= 370 and ypos <= 385 and ypos >= 335:
        xvol = 0 # the if statement above tell states that if the ball touches any of the black pockets, the ball will reset at 200,200 and the x and y velocity are set back to 0
        yvol = 0
        ypos = 200
        xpos = 200 
        back1 += 79 # these adjustments to back1,2 and 3 allow the color of the background to change when the ball is sunk
        back2 += 71
        back3 += 61
    if back1 >= 255: #the next three if statement say that if any of the rgb values reach 255 to reset them back to zero
            back1=0
    if back2 >= 255:
            back2=0
    if back3 >= 255:
            back3=0

    
