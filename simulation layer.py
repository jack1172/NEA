
import math
GRAVITY = -9.81

# velocity calculation stuff the angle is changed from radians to degrees as degrees are easier to use in the simulation but python only uses radians
def v(u, angle_deg):
    angle_rad = math.radians(angle_deg)
    return u * math.cos(angle_rad), u * math.sin(angle_rad)
def projectile_simulation(u, angle):
    vx, vy = v(u, angle)
    x, y = 0, 0
    change_t = 0.01
    traj = []
    while y >= 0:
        traj.append((x, y))
        x += vx * change_t
        y += vy * change_t + 0.5 * GRAVITY * change_t**2
        vy += GRAVITY * change_t
    return traj

#graphing part for the NEA and it will link to a html eventually

u = float(input("what is the initial velocity: "))
angle = float(input("what is the angle when the projectile is fired: "))
traj = projectile_simulation(u, angle)
xs = (p[0] for p in traj)
ys = (p[1] for p in traj)
traj = projectile_simulation(u, angle)
for point in traj[:10]:
    print(point)
print("Final range:", traj[-1][0])
print("Max height:", max([p[1] for p in traj])) 


import json

with open("trajectory.json", "w") as f:
    json.dump(traj, f)
