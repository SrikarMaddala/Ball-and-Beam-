from errno import EDEADLK
from time import time
from tkinter import E
import math 
import matplotlib.pyplot as plt

m = 80
b = 120
theta = 60
vo = 0 
vr = 143
float(vr)
eo = vr - vo
kp= 50
# ep is same as error
ki =  20
kd = 10
delta_t = 0.5
t = 0
ei = 0
g = 9.8
error_list = []
time_list = []
velocity_list = []
while t < 20 :
    ep = vr - vo
    ed = (ep - eo) /delta_t
    ei  = ei + ep*delta_t
    u = ep*kp + ei*ki + ed*kd
    error_list.append(ep)
    velocity_list.append(vo)
    time_list.append(t)
    a = (u + m*g*math.sin(theta))/ m
    vf = vo + a*delta_t
    if vf == vr*0.9 :
        print(t)
    vo = vf
    t = t + delta_t

print(-min(error_list)*100/int(vr))
plt.plot( time_list , error_list)
plt.axhline(y = vr , color = 'r', linestyle = '--')
plt.plot(time_list , velocity_list)

plt.show()


