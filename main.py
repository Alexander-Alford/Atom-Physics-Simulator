from vpython import *
import math

#constants
delta_t = 1e-13 # s
min_dist = 1e-15 # m
elec_mass = 9.1093837015e-31 # kg 
prot_mass = 1.6726219e-27 # kg
elem_charge = 1.602176634e-19 # C
scalefactor = 1e15
coulombconst = 8.9875517923e9 # kg⋅m3⋅s^2/C^2

time = 0.0

class Particle:

    def __init__(self, velocity, mass, charge, position, color, radius):
        self.velocity = vector(velocity[0], velocity[1], velocity[2])
        self.position = vector(position[0], position[1], position[2])
        self.mass = mass
        self.charge = charge
        self.sphere = sphere(pos = self.position, radius = radius, color = color)

    def updatePos(self):
        self.position += (self.velocity*delta_t*scalefactor)
        self.sphere.pos = self.position

    def applyForce(self, other):
        force = getElectroForce(self.charge, other.charge, 
                                getDistance(self.position, other.position))

        self.velocity += (norm(self.position - other.position)*force*delta_t)/self.mass
        other.velocity += (norm(other.position - self.position)*force*delta_t)/other.mass


particlelist = []


#calulators
def getDistance(pos_1, pos_2):
    return mag(pos_1 - pos_2)

def getElectroForce(q1, q2, rad):
    return q1*q2*coulombconst/(rad ** 2)

def addForce():
    return 



primescene = canvas(width = 800, height = 800)


particlelist.append(Particle([0,0,0], prot_mass, elem_charge, [-0.001,0,0], color.purple, 0.0005))
particlelist.append(Particle([0,0.00001,0], elec_mass, -elem_charge, [0.001,0,0], color.yellow, 0.0005))



while time < delta_t*10000:
    rate(100)
    for p in range(len(particlelist)):
        p1 = p
        p2 = p + 1

        try:
            particlelist[p].applyForce(particlelist[p2])    
        except:
            i = 0 

    particlelist[p].updatePos()         
    print(particlelist[0].velocity)
    time = time + delta_t

del particlelist
 