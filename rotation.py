import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def apply_matrix_transformation(matrix, transformation_matrix):
    """
    Apply a matrix transformation to a set of points.

    Parameters:
    - matrix: Original matrix of points.
    - transformation_matrix: Transformation matrix.

    Returns:
    - Transformed matrix.
    """
    transformed_matrix = np.dot(matrix, transformation_matrix.T)
    return transformed_matrix

def plot_plane(ax, matrix, color, label):
    """
    Plot a plane on a 3D plot.

    Parameters:
    - ax: Axes3D object for 3D plotting.
    - matrix: Matrix of points forming the plane.
    - color: Color of the plot.
    - label: Label for the plot.
    """
    ax.plot_trisurf(matrix[:, 0], matrix[:, 1], matrix[:, 2], color=color, alpha=0.5, label=label)

def set_axes_equal(ax):
    """
    Set equal scaling for the axes of a 3D plot.

    Parameters:
    - ax: Axes3D object for 3D plotting.
    """
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = max(x_limits[1] - x_limits[0], y_limits[1] - y_limits[0], z_limits[1] - z_limits[0])
    mid_x = np.mean(x_limits)
    mid_y = np.mean(y_limits)
    mid_z = np.mean(z_limits)

    ax.set_xlim3d([mid_x - x_range / 2, mid_x + x_range / 2])
    ax.set_ylim3d([mid_y - x_range / 2, mid_y + x_range / 2])
    ax.set_zlim3d([mid_z - x_range / 2, mid_z + x_range / 2])

# Define the original plane
original_plane = np.array([
    [1, 1, 1],
    [1, 2, 1],
    [2, 1, 1],
    [2, 2, 1]
])

# Define the rotation angle in radians (for example, rotating by 45 degrees around the z-axis)
theta = np.radians(45)
c, s = np.cos(theta), np.sin(theta)
rotation_matrix = np.array([
    [c, -s, 0],
    [s, c, 0],
    [0, 0, 1]
])

# Apply the rotation transformation
rotated_plane = apply_matrix_transformation(original_plane, rotation_matrix)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original plane
plot_plane(ax, original_plane, color='blue', label='Original')

# Plot the rotated plane
plot_plane(ax, rotated_plane, color='red', label='Rotated')

# Set labels for each axis
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set equal scaling for the axes
set_axes_equal(ax)

# x_lim = ax.get_xlim3d()
# y_lim = ax.get_ylim3d()
# z_lim = ax.get_zlim3d()

# # Bolden the axes lines at x = 0, y = 0, and z = 0
# ax.plot([x_lim[0], x_lim[1]], [0, 0], [0, 0], color='black', linewidth=2)  # x = 0
# ax.plot([0, 0], [y_lim[0], y_lim[1]], [0, 0], color='black', linewidth=2)  # y = 0
# ax.plot([0, 0], [0, 0], [z_lim[0], z_lim[1]], color='black', linewidth=2)  # z = 0
# Add a legend
ax.legend()

# Show the plot
plt.show()
