# Write a cosole program that calculates the trajectory that a projectile will follow. You will prompt the user for the projectile's initial velocity, its initia angle relative to the horizontal, and the number of time increments to display. Here is an example output lof from your program:
#
# This program computes the trajectory of a prjectile givin its initial velocity and angle relative to the horizontal.
# 
# Velocity (m/s)? 30
# Angle (degrees)? 50
# Number of steps? 10
# 
# step  x      y     time
# --------------------------
# 0     0.00   0.00   0.00
# 1     9.03   9.69   0.47
# 2     18.07  17.23  0.94
# 3     27.10  22.61  1.41
# 4     36.14  25.84  1.87
# 5     45.17  26.92  2.34
# 6     54.21  25.84  2.81
# 7     63.24  22.61  3.28
# 8     72.28  17.23  3.75
# 9     81.31  9.69   4.22
# 10    90.35  0.00   4.69
# 
# You can compute the x and y components of velocity using the cos and sin of the initial angle, respectively. The projectile will be pulled downward by gravity with a force of 9.81 m/s^2. Recall that you can compute the displacement of a body in motion using the following formula:
# 
# displacement = vt + 1/2at^2
#
# The following is a psuedocode description of the process:
# 
# x, y, t = 0.
# for (the given number of steps):
#    add the time increment to t.
#    add x increment to x.
#    reset y to y-velecity * t * 0.5 * -9.81 * t * t.
#    rport step #, x, y, and t.
# 
# You should break down your program into several functions, each of which helps solve the overall problem
# 
# The output columns should align into 8-space-wide columns, left-aligned.

# Write your functions here
def get_velocity():
    return float(input("Velocity (m/s)? "))
def get_angle():
    return float(input("Angle (degrees)? "))
def get_steps():
    return int(input("Number of steps? "))
def get_time_increment(velocity, angle, steps):
    return 2 * velocity * math.sin(math.radians(angle)) / -9.81 / steps
def get_x_increment(velocity, angle, time_increment):
    return velocity * math.cos(math.radians(angle)) * time_increment
def get_y_increment(velocity, angle, time_increment, time):
    return velocity * math.sin(math.radians(angle)) * time_increment + 0.5 * -9.81 * time_increment * time_increment
def print_header():
    print("\nstep    x    y    time")
    print("--------------------------")
def print_step(step, x, y, time):
    print("{:0d}    {:5.2f}    {:5.2f}    {:5.2f}".format(step, x, y, time))

def main():
    print("This program computes the trajectory of a projectile given its initial velocity and angle relative to the horizontal./n")
    velocity = get_velocity()
    angle = get_angle()
    steps = get_steps()
    time_increment = get_time_increment(velocity, angle, steps)
    x_increment = get_x_increment(velocity, angle, time_increment)
    print_header()
    x, y, t = 0., 0., 0.
    for i in range(steps + 1):
        print_step(i, x, y, t)
        t += time_increment
        x += x_increment
        y += get_y_increment(velocity, angle, time_increment, t)

main()