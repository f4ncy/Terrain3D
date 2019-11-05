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
    
    for y in range(rows):
        for x in range(cols):
            stroke(255)
            noFill()
            rect(x*scl, y*scl, scl, scl)
            
