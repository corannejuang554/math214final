import numpy as np
import matplotlib.pyplot as plt

def apply_matrix_transformation(matrix, transformation_matrix):
    # transformed_matrix = np.dot(matrix, transformation_matrix.T)
    return transformed_matrix

def plot_points(ax, matrix, color, label):
    ax.plot(matrix[:, 0], matrix[:, 1], color=color, label=label)

def shade_area(ax, matrix, color, label):
    ax.fill(matrix[:, 0], matrix[:, 1], color=color, alpha=0.2, label=label)

width = int(input("enter the width of your matrix: "))
height = int(input("enter the height of your matrix: "))
original_plane = []
for h in range(height):
    arr = []
    for w in range(width):
        print("enter number at", h, w, ": ", end='')
        el = int(input())
        arr.append(el)
    original_plane.append(arr)

width = int(input("enter the width of your transformation matrix: "))
height = int(input("enter the height of your transformation matrix: ")) 
transformation_matrix = []
for h in range(height):
    arr = []
    for w in range(width):
        print("enter number at", h, w, ": ", end='')
        el = int(input())
        arr.append(el)
    transformation_matrix.append(arr)

original_plane = np.array(original_plane)

transformation_matrix = np.array(transformation_matrix)
# Define the original rectangle points in 2D
# original_plane = np.array([
#     [1, 1],
#     [1, 3],
#     [4, 3],
#     [4, 1],
#     [1, 1]  
# ])

# transformation_matrix = np.array([
#     [-1, 0],
#     [0, 1]
# ])

# theta = np.radians(45)
# transformation_matrix = np.array([
#     [np.cos(theta), -np.sin(theta)],
#     [np.sin(theta), np.cos(theta)]
# ])

transformed_matrix = apply_matrix_transformation(original_plane, transformation_matrix)

# Create a 2D plot
fig, ax = plt.subplots()

# Plot the original rectangle
plot_points(ax, original_plane, color='blue', label='Original')

# Plot the transformed rectangle
plot_points(ax, transformed_matrix, color='green', label='Transformed')

# Shade the area of the original rectangle in blue
shade_area(ax, original_plane, color='blue', label='Original Area')

# Shade the area of the transformed rectangle in green
shade_area(ax, transformed_matrix, color='green', label='Transformed Area')

# Set labels for each axis
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Add grid lines
ax.grid(True)

# Add a legend
ax.legend()

# Show the plot
plt.show()



# import numpy as np
# import matplotlib.pyplot as plt

# def apply_matrix_transformation(matrix, transformation_matrix):
#     """
#     Apply a matrix transformation to a set of points.

#     Parameters:
#     - matrix: Original matrix of points.
#     - transformation_matrix: Transformation matrix.

#     Returns:
#     - Transformed matrix.
#     """
#     transformed_matrix = np.dot(matrix, transformation_matrix.T)
#     return transformed_matrix

# def plot_points(ax, matrix, color, label):
#     """
#     Plot points on a 2D plot.

#     Parameters:
#     - ax: Axes object for 2D plotting.
#     - matrix: Matrix of points.
#     - color: Color of the plot.
#     - label: Label for the plot.
#     """
#     ax.plot(matrix[:, 0], matrix[:, 1], color=color, label=label)

# # Define the original rectangle points in 2D
# original_rectangle = np.array([
#     [1, 1],
#     [1, 3],
#     [4, 3],
#     [4, 1],
#     [1, 1]  
# ])

# # Define the rotation angle (in radians)
# # theta = np.radians(45)

# # Define the rotation matrix
# # rotation_matrix = np.array([
# #     [np.cos(theta), -np.sin(theta)],
# #     [np.sin(theta), np.cos(theta)]
# # ])
# transformation_matrix = np.array([
#     [1, 0],
#     [0, 2]
# ])

# # Apply the rotation transformation
# transformed_matrix = apply_matrix_transformation(original_rectangle, transformation_matrix)

# # Create a 2D plot
# fig, ax = plt.subplots()

# # Plot the original rectangle
# plot_points(ax, original_rectangle, color='blue', label='Original')

# # Plot the transformed rectangle
# plot_points(ax, transformed_matrix, color='green', label='Transformed')

# # Set labels for each axis
# ax.set_xlabel('X')
# ax.set_ylabel('Y')

# # Add grid lines
# ax.grid(True)

# # Add a legend
# ax.legend()

# # Show the plot
# plt.show()
