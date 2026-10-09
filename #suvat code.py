#suvat code v.2
import math

#starting with s
def calculate_s_u(v, a, t):
    return ((v * t) - 0.5 * (a * (t * t)))
    
def calculate_s_v(u, a, t):
    return ((u * t) + 0.5 * (a * (t * t)))

def calculate_s_a(u, v, t):
    return ((u + v) * 0.5 * t)

def calculate_s_t(u, v, a):
    return ((v * v) - (u * u) / (2 * a))

#starting with u
def calculate_u_v(u, a, t):
    return u + a * t

def calculate_u_s(v, a, t):
    return ((v * t) - 0.5 * (a * (t * t)))

def calculate_u_a(s, a, t):
    return ((s - 0.5 * a * t * t) / t)

def calculate_u_t(u, v, a):
    return ((v * v) - (u * u) / (2 * a))

#starting with v
def calculate_v_s(u, a, t):
    return ((u * t) + 0.5 * (a * (t * t)))

def calculate_v_u(s, a, t):
    return ((s / t) + 0.5 * a * t)

def calculate_v_a(s, u, t):
    ((2 * s / t) - u)
    
def calculate_v_t(s, u, a):
    return math.sqrt(((u * u) + 2 * a * s))

#starting with a
def calculate_a_s(v, u, t):
    return ((v - u) / t)

def calculate_a_u(v, s, t):
    return (2 * ((v * t) - s) / (t * t))

def calculate_a_v(u, s, t):
    return (2 * ((u * t) + s) / (t * t))

def calculate_a_t(u, s, v):
    return (((v * v) - (u * u)) / (2 * s))

#starting with t
def calculate_t_s(u, a, v):
    return (((v - u)) / a)

def calculate_t_u(s, a, v):
    t1 = (v + math.sqrt((v * v) - (2 * a * s))) / a
    t2 = (v - math.sqrt((v * v) - (2 * a * s))) / a
    if   t1 < 0:
        return t2
    else:
        return t1

def calculate_t_v(u, a, s):
    t1 = (-u + math.sqrt((u * u) + (2 * a * s))) / a
    t2 = (-u - math.sqrt((u * u) + (2 * a * s))) / a
    if t1 >= 0 and t2 >= 0:
        return (t1, t2)
    elif t1 >= 0:
        return ("t =", t1)
    else:
        return ("t =", t2)
    
def calculate_t_a(s, u, v):
    return (2 * s) / (u + v)

#simulation part (no idea what im doing)

GRAVITY = -9.8

def resolve_velocity(u, angle_deg):
    angle_rad = math.radians(angle_deg)
    return u * math.cos(angle_rad), u * math.sin(angle_rad)

def resolve_velocity(u, angle_deg):
    angle_rad = math.radians(angle_deg)  # convert here as python needs radians but degrees have more ease of use 

    u_x = u * math.cos(angle_rad)
    u_y = u * math.sin(angle_rad)

    return u_x, u_y

GRAVITY = -9.8

def resolve_velocity(u, angle_deg):
    angle_rad = math.radians(angle_deg)

    return (
        u * math.cos(angle_rad),
        u * math.sin(angle_rad)
    )

x = 0
y = 0

vx, vy = resolve_velocity(30, 45)

dt = 0.01

trajectory = []

while y >= 0:
    trajectory.append((x, y))

    vy += GRAVITY * dt

    x += vx * dt
    y += vy * dt

print("Range:", x)
print("Max points:", len(trajectory))

import matplotlib.pyplot as plt

xs = [p[0] for p in trajectory]
ys = [p[1] for p in trajectory]

plt.plot(xs, ys)
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid(True)

plt.show()