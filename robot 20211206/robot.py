x = 60
y = 500
radius = 45
neck_length = 70
body_length = 160
easing = 0.5
new_color1 = int(random(255))
new_color2 = int(random(255))
new_color3 = int(random(255))

def setup():
    size(360, 480)
    strokeWeight(2)
    ellipseMode(RADIUS)

    
def draw():
    background(0, 153, 204)
    translate (mouseX, y)

    if mousePressed:
        scale(1.0)
    else:
        scale(0.6)
    
    noStroke()
    fill(255, 204, 0)
    ellipse(0, -33, 33, 33)
    fill(0)
    rect(-45, -body_length, 90, body_length - 33)

    #Neck
    stroke(255)
    neck_y=-(body_length + neck_length + radius)
    line(12, -body_length, 12, neck_y)


    # hair
    pushMatrix()
    translate(12, neck_y)
    angle = PI/30
    for i in range (45):
        line(80,0,0,0)
        rotate(angle)
    popMatrix()

    
    # head
    noStroke()
    fill(0)
    ellipse(12,neck_y,radius,radius)
    fill(new_color1,new_color2,new_color3)
    ellipse(24, neck_y-6, 14, 14)
    fill(0)
    ellipse(24, neck_y-6, 3, 3)
