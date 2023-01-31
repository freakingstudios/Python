from vpython import *

# Create a sphere
sphere = sphere(pos=vector(0,0,0), radius=1, color=color.red)

# Create a box
box = box(pos=vector(5,0,0), size=vector(1,1,1), color=color.blue)

# Create a scene
scene = canvas(title='3D Animation Example', width=500, height=500)

# Animate the sphere and box
while True:
    rate(30)
    sphere.pos.x = sphere.pos.x + 0.1
    box.rotate(angle=0.05, axis=vector(0,1,0))
