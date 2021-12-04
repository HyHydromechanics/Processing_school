size(800,400)
background(0)
stroke(102)

for i in range(20,height-20,10):
    for a in range(20,width-20,10):
        ellipse(a,i,6,6)
        line(400,200,a,i)
