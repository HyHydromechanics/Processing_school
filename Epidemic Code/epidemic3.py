# Modelling an epidemic with Python
w = 400
h = 400

class Ball(object):
  global w,h

  def __init__(self,x_,y_,vx_,vy_):
    self.x=x_
    self.y=y_
    self.vx=vx_
    self.vy=vy_

  def move(self):
    if self.x < 0 or self.x > w:
      self.vx *= -1
    if self.y < 0 or self.y > h:
      self.vy *= -1
    self.x += self.vx
    self.y += self.vy

  def display(self):
    fill(127)
    ellipse(self.x,self.y,10,10)

ball1 = Ball(100,300,5,5)

def setup():
  global w,h
  size(w,h)
  background(32)

def draw():
  background(32)
  ball1.move()
  ball1.display()