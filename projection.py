import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def line_projection(v, w):
    v_dot_w = np.dot(v, w)
    w_norm_squared = np.dot(w, w)
    projection = (v_dot_w / w_norm_squared) * w
    return projection

# Example usage:
v = np.array([2, 3, 4])  # Direction vector of line L1
w = np.array([1, 1, 1])  # Direction vector of line L2

projection = line_projection(v, w)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original vector representing line L1
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='blue', label='Line L1')

# Plot the line representing line L2
t = np.linspace(-5, 5, 10)
line_L2 = np.outer(t, w)
ax.plot3D(line_L2[:, 0], line_L2[:, 1], line_L2[:, 2], color='red', label='Line L2')

# Plot the orthogonal projection of L1 onto L2
ax.quiver(0, 0, 0, projection[0], projection[1], projection[2], color='green', label='Projection of L1 onto L2')

# Set labels for each axis
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set equal scaling for the axes
ax.set_box_aspect([np.ptp(arr) for arr in [ax.get_xlim(), ax.get_ylim(), ax.get_zlim()]])

# Add a legend
ax.legend()

# Show the plot
plt.show()
