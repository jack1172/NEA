import math

GRAVITY = -9.8

def velocity(initial_speed, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    vx = initial_speed * math.cos(angle_radians)
    vy = initial_speed * math.sin(angle_radians)
    return vx, vy

def projectile_simulation(initial_speed, angle_degrees):
    vx, vy = velocity(initial_speed, angle_degrees)
    x, y = 0, 0
    time_step = 0.01
    trajectory = []

    while y >= 0:
        trajectory.append((x, y))
        x += vx * time_step
        y += vy * time_step + 0.5 * GRAVITY * time_step ** 2
        vy += GRAVITY * time_step

    return trajectory

initial_speed = 30
angle = 45

trajectory = projectile_simulation(initial_speed, angle)

for point in trajectory[:10]:
    print(point)

print(Final_range:, trajectory[-1][0])
print(Max_height:, max(point[1] for point in trajectory))