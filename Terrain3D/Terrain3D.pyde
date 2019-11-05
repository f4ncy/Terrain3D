scl = 20
cols = 0
rows = 0
w = 600
h = 600



def setup():
    global cols, rows
    size(600, 600, P3D)
    cols = w / scl
    rows = h / scl
    
    
    
    
def draw():
    global cols, rows, w, h
    background(0)
    stroke(255)
    noFill()
    translate(width/2, height/2)
    rotateX(PI/3)
    
    translate(-w/2, -h/2)
    for y in range(rows):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            vertex(x*scl, y*scl)
            vertex(x*scl, (y+1)*scl)
        endShape()
