import vpython as vp
import numpy as np

initial_position = vp.vector(-4, 0, 0)
initial_velocity = vp.vector(0, -20, 0)

ball = vp.sphere(
    pos=initial_position,
    radius=0.5,
    color=vp.color.cyan,
    make_trail=True,
    # retain=50
)
ball.velocity = initial_velocity
ball.mass = 0.1

rod = vp.cylinder(
    pos=initial_position, axis=-ball.pos, radius=0.1
)


dt = 0.005
t = 0
T = 20
# k = 10
k = lambda t: np.sin(t)
d = 4
g = -9.81 * 0
drag_coefficient = 0.001 * 0

# A plot
kinetic = vp.gcurve(color=vp.color.blue)

while t < T:
    vp.rate(100)
    relative_displacement = rod.length - d
    ball_force = - k(t) * relative_displacement * ball.pos.norm()
    ball_force.y += g
    ball_force -= drag_coefficient * ball.velocity.mag**2 * ball.velocity.norm()
    acceleration = ball_force / ball.mass 
    ball.velocity += acceleration * dt
    kinetic_energy = 0.5 * ball.mass * ball.velocity.mag**2
    kinetic.plot(t, kinetic_energy)
    ball.pos += ball.velocity * dt
    rod.pos = ball.pos
    rod.axis = -ball.pos
    t += dt
