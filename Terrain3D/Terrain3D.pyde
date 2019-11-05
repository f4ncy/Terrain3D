scl = 20
cols = 0
rows = 0
w = 2000
h = 2000
flying = 0
rotation = 0


def setup():
    global cols, rows, terrain
    size(1080, 720, P3D)
    cols = int(w / scl)
    rows = int(h / scl)
    #terrain = [[map(noise(i, j), 0, 1, -50, 50) for i in range(rows)] for j in range(cols)]
    terrain = [[0 for i in range(rows)] for j in range(cols)]
    
    
    
    
def draw():
    global cols, rows, w, h, flying, rotation
    flying -= 0.1
    rotation += 0.01
    yoff = flying
    for y in range(rows):
        xoff = 0
        for x in range(cols):
            terrain[x][y] = map(noise(xoff, yoff), 0, 1, -100, 100)
            xoff += 0.1
        yoff += 0.1
    
    
    
    
    
    background(0)
    stroke(255)
    noFill()
    translate(width/2, height/2)
    rotateY(map(mouseX,0,width, 0, 2*PI))
    rotateX(map(mouseY,0,height, 0, 2*PI))
    
    translate(-w/2, -h/2)
    for y in range((rows-1)):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            vertex(x*scl, y*scl, terrain[x][y])
            vertex(x*scl, (y+1)*scl, terrain[x][y+1])
        endShape()
