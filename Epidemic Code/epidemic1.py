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

ball1 = Ball(100,200,5,5)

def setup():
  global w,h
  size(w,h)
  background(32)

def draw():
  ellipse(200,200,10,10)