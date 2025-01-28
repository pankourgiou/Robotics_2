import matplotlib.pyplot as plt
import numpy as np
import time

# Robot arm parameters
link1_length = 1.0  # Length of the first link
link2_length = 0.5  # Length of the second link

def forward_kinematics(theta1, theta2):
    """Calculate the (x, y) positions of the arm's joints."""
    x1 = link1_length * np.cos(theta1)
    y1 = link1_length * np.sin(theta1)

    x2 = x1 + link2_length * np.cos(theta1 + theta2)
    y2 = y1 + link2_length * np.sin(theta1 + theta2)

    return (1, 1), (x1, y1), (x2, y2)

def update_plot(joint_positions, line):
    """Update the plot with the new joint positions."""
    x_data = [pos[0] for pos in joint_positions]
    y_data = [pos[1] for pos in joint_positions]
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    plt.draw()
    plt.pause(0.01)

# Initialize Matplotlib plot
plt.ion()
fig, ax = plt.subplots()
ax.set_xlim(-4, 2)
ax.set_ylim(-5, 2)
ax.set_aspect('equal', 'box')
line, = ax.plot([], [], 'o-', lw=4)  # Line to represent the arm

# Simulation parameters
steps = 200
for t in range(steps):
    # Calculate joint angles (simple sinusoidal motion)
    theta1 = np.sin(2 * np.pi * t / steps)
    theta2 = np.cos(2 * np.pi * t / steps)

    # Calculate forward kinematics
    joint_positions = forward_kinematics(theta1, theta2)

    # Update the plot
    update_plot(joint_positions, line)

    time.sleep(0.0002)

plt.ioff()
plt.show()
