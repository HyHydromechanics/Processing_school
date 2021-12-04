x = 60
y = 440
radius = 45
neck_length = 70
body_length = 160
easing = 0.5

def setup():
    size(1280, 720)
    strokeWeight(2)
    background(0, 153, 204)
    ellipseMode(RADIUS)

    
def draw():
    global x
    global y
    targetX = mouseX
    targetY = mouseY
    easing = 0.03
    frameRate(60)
    x += (targetX - x)
    y += (targetY - y)
    
    new_color1 = int(random(255))
    new_color2 = int(random(255))
    new_color3 = int(random(255))

    if mousePressed:
        neck_length = 200
        body_length = 50
    
    else:
        neck_length = 250
        body_length = 100
        
    neck_y = y - body_length - neck_length
    
    background(new_color1, new_color2, new_color3)
    
    # Neck
    stroke(255)
    line(x+12, y, x+12, neck_y)


    # line
    line(x+12, neck_y+100, x-12, neck_y)
    line(x+12, neck_y+100, x+42, neck_y)
    line(x+12, neck_y+100, x+100, neck_y)


    # bottom
    noStroke()
    fill(255, 204, 0)
    ellipse(x, y-33, 33, 33)
    fill(0)
    rect(x-45, y-body_length, 90, body_length - 33)


    # head
    fill(0)
    ellipse(x+12, neck_y+100, radius, radius)
    fill(255)
    ellipse(x+24, neck_y+100, 14, 14)
    fill(0)
    ellipse(x+24, neck_y+100, 3, 3)
