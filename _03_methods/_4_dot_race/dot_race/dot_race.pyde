# When you are done, this program will draw an ellipse 
# that travels across the screen when the mouse is pressed.

# ***********  SOUND ***************
# Some computers are unable to play sounds. 
# If you cannot play sound on this computer, set canPlaySounds to false.
# If you are not sure, ask your teacher 

can_play_sounds = True

def setup():
    global x
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global j
    global k
    global l
    global m
    global n
    global o

    size(800, 800)
    x=50

    # 1. Set the variable named x to 50.

def draw():
    global x
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global j
    global k
    global l
    global m
    global n
    global o
    background(200, 200, 200)

    
    # 2. Draw an ellipse of height and width 50. Make sure to use the x variable
    # for its X position. Pick a y value that places it half way down the window.
    
    fill("#0EE5EA")

    ellipse(x+10, 100, 50, 50)
    ellipse(a, 50, 50, 50)
    ellipse(b, 150, 50, 50)
    ellipse(c, 200, 50, 50)
    ellipse(d, 250, 50, 50)
    ellipse(e, 50, 50, 50)
    ellipse(f, 300, 50, 50)
    ellipse(g, 350, 50, 50)
    ellipse(h, 400, 50, 50)
    ellipse(i, 450, 50, 50)
    ellipse(j, 500, 50, 50)
    ellipse(k, 550, 50, 50)
    ellipse(l, 600, 50, 50)
    ellipse(n, 650, 50, 50)
    ellipse(m, 700, 50, 50)
    ellipse(o, 750, 50, 50)
    

    # 3. Fill in the ellipse with a nice color. Remember to put it above the code
    # where you draw the ellipse.
    if mousePressed:
        x = x + 0.2
        a = a + 100
        b=b+10
        c = c + 50
        d=d+40
        e=e+4
        f=f+8
        g=g+93
        h=h+83
        i=i+89
        j=j+32
        k=k+23
        
        
    # 4. If the mouse is pressed change the x value so that the dot moves to the right
    
    # 5. If your dot moves slowly, make it move faster. If it moves too quickly,
    # slow it down (you have to figure out what part of your code to change)

    # 6. Use an if statement to play a sound (ding) when your dot crosses the finish
    if x > 800:
        play_sound()
    # line (right side of window). A playSound() method is provided (you have to
    # uncomment the code at the bottom of this program to get this to work)


    sound_played = True
    
def play_sound():
  
    # if can_play_sounds:
    #     if sound_played:
    #         Minim minim = new Minim(this)
    #         AudioSample sound = minim.loadSample("ding.wav")
    #         sound.trigger()
    #         soundPlayed = true
    #         pass
    fill(0)
    textSize(36)
    text("WINNER!!", width/2, height/2)
