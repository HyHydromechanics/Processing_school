void setup(){
  size(400,400);
  smooth();
  frameRate(10);
}

void draw(){
  background(0,0,0);
  
  noStroke();
  rect(200,150,30,100);
  
  noStroke();
  ellipse(190,150,50,50);
  
  noStroke();
  ellipse(240,150,50,50);
  
  noStroke();
  ellipse(215,250,30,30);
  
  stroke(0,0,0);
  line(218,265,215,250);
  
  stroke(0,0,0);
  line(213,265,215,250);
}
void mousePressed(){
  noStroke();
  rect(200,180,30,100);
  
  noStroke();
  ellipse(190,180,50,50);
  
  noStroke();
  ellipse(240,180,50,50);
  
  noStroke();
  ellipse(215,280,30,30);
  
  stroke(0,0,0);
  line(218,295,215,250);
  
  stroke(0,0,0);
  line(213,295,215,250);
}
