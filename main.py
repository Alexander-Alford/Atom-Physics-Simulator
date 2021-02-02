from vpython import *
import math

#mathematical constants
elec_mass = 9.1093837015e-31 # kg 
prot_mass = 1.6726219e-27 # kg
elem_charge = 1.602176634e-19 # C
coulombconst = 8.9875517923e9 # kg⋅m3⋅s^2/C^2

#approximation constants
delta_t = 1e-27 # s
min_dist = 1e-15 # m
scalefactor = 1e15
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

 


particlelist = []

def electroCheck(call):
    global electro_flag

    if electro_flag == True:
        electro_flag = False
    else:
        electro_flag = True

#calulators
def getDistance(pos_1, pos_2):
    return mag(pos_1 - pos_2)

def getElectroForce(q1, q2, rad):
    return q1*q2*coulombconst/(rad ** 2)

def pauseBut(self):
    global run_flag

    if not run_flag:
        run_flag = True
        self.text = "Pause"
    else:
        run_flag = False
        self.text = "Run"

def addForce(force, p1, p2):
    p1.velocity += (norm(p1.position - p2.position)*force*delta_t)/p1.mass
    p2.velocity += (norm(p2.position - p1.position)*force*delta_t)/p2.mass    

def applyForce(plist):
    for p1 in range(len(plist)):
        for p2 in range(p1 + 1,len(plist)):
            if p2 <= len(plist):
                addForce( getElectroForce(plist[p1].charge, plist[p2].charge, getDistance(plist[p1].position, plist[p2].position)), plist[p1], plist[p2])


run_flag = True
electro_flag = True

primescene = canvas(title="Atomic Physics Simulator", width = 800, height = 800, center=vector(0,0,0))


button(text = "Pause", pos = primescene.title_anchor, bind = pauseBut)
checkbox(text = "Electrostatic Force", bind = electroCheck, checked = True, id = 0)

sphere(pos=vector(1.29e-11,0,0), color=color.red, radius=1e-12)

particlelist.append(Particle([0,0,0], prot_mass, elem_charge, [0,0,0], color.purple, 1e-12))
particlelist.append(Particle([0,7.18e-2,0], elec_mass, -elem_charge, [5.29e-11,0,0], color.yellow, 1e-12))



while True:
    if run_flag:    
        rate(2000)
        
        if electro_flag == True:
            applyForce(particlelist)

        for p in range(len(particlelist)):
            particlelist[p].updatePos()
        
        time = time + delta_t

del particlelist
 