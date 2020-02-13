import vpython as vp 

solar_mass = 1.988544e30
earth_mass = 5.97219e24 / solar_mass
jupiter_mass = 1898.13e24 / solar_mass

large_body = vp.sphere(
    pos=vp.vector(0, 0, 0),
    radius=0.1,
    color=vp.color.yellow,
)
large_body.m = 1
large_body.vel = vp.vector(0, 0, 0)
large_body.force = vp.vector(0, 0, 0)
large_body.name = "sol"

small_body = vp.sphere(
    pos=vp.vector(1, 0, 0),
    radius=0.05,
    color=vp.color.blue,
    make_trail=True,
    # retain=100,
)
small_body.m = earth_mass
small_body.vel = vp.vector(0, 2*vp.pi, 0)
small_body.force = vp.vector(0, 0, 0)
small_body.name = "earth"

jupiter = vp.sphere(
    pos=vp.vector(5.2, 0, 0),
    radius=0.07,
    color=vp.color.orange,
    make_trail=True,
)
jupiter.m = jupiter_mass
# jupiter.vel = vp.vector(0.036524, -3.6524, 0)
jupiter.vel = vp.vector(0, -2.75, 0)
jupiter.force = vp.vector(0, 0, 0)
jupiter.name = "jupiter"

bodies = [large_body, small_body, jupiter]
N = len(bodies)

dt = 0.005
t = 0
T = 10
G = 4*vp.pi*vp.pi

while t < T:
    vp.rate(50)

    # Reset forces 
    for i in range(0, N):
        bodies[i].force = vp.vector(0, 0, 0)

    # Compute forces
    for i in range(0, N):
        body_i = bodies[i]
        m_i = bodies[i].m
        r_i = body_i.pos
        
        for j in range(i + 1, N):
            body_j = bodies[j]
            m_j = bodies[j].m
            r_j = body_j.pos
            
            r = r_i - r_j 

            F = - ((G*m_i*m_j) / (r.mag2 * r.mag)) * r

            body_i.force += F
            body_j.force -= F 

    # Euler-Cromer    
    for i in range(0, N):
        a = bodies[i].force / bodies[i].m
        bodies[i].vel += a * dt
        bodies[i].pos += bodies[i].vel * dt

    t += dt