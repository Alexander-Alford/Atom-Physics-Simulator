from vpython import *
import math

#constants
delta_t = 1e-4 # s
min_dist = 1e-15 # m
elec_mass = 9.1093837015e-31 # kg 
prot_mass = 1.6726219e-27 # kg
elem_charge = 1.602176634e-19 # C
scalefactor = 1e15
coulombconst = 8.9875517923e9 # kg⋅m3⋅s^2/C^2

time = 0.0

#calulators
def getDistance(pos_1, pos_2):
    x_diff_sqr = (pos_1[0] - pos_2[0]) ** 2
    y_diff_sqr = (pos_1[1] - pos_2[1]) ** 2
    z_diff_sqr = (pos_1[2] - pos_2[2]) ** 2

    return math.sqrt(x_diff_sqr + y_diff_sqr + z_diff_sqr)

def getElectroForce(q1, q2, rad):
    return q1*q2*coulombconst/(rad ** 2)

def addForce():
    return 

particleone = sphere(pos = (vector(-2,0,0)), radius = 1, color = color.yellow)
particletwo = sphere(pos = (vector(2,0,0)), radius = 0.1, color = color.red)


while time < 1:
    
    
    time = time + delta_t