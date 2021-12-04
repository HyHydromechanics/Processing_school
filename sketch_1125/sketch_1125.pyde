x = 0
y = 0
py = 0
px = 0
easing = 0.03
def setup():
    size(600,600)
    frameRate(200)
def draw():
    global x
    global y
    py = y
    px = x
    noStroke()
    x += (mouseX - x) * easing
    y += (mouseY - y) * easing
    weight = dist(x,y,px,py)
    strokeWeight(weight)
    line(x, y, px,py)
