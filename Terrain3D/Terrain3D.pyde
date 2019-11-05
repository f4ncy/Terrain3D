scl = 20
cols = 0
rows = 0



def setup():
    global cols, rows
    size(600, 600, P3D)
    w = width
    h = height
    cols = w / scl
    rows = h / scl
    
    
    
    
def draw():
    global cols, rows
    background(0)
    stroke(255)
    noFill()
    
    for y in range(rows):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            vertex(x*scl, y*scl)
            vertex(x*scl, (y+1)*scl)
        endShape()
