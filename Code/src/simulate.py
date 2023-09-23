import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime


timestamp=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f'my_plot_{timestamp}.png'


def find_angles(side_a, side_b, side_c):
    # Calculate the angles using the law of cosines
    angle_a = math.degrees(math.acos((side_b**2 + side_c**2 - side_a**2) / (2 * side_b * side_c)))
    angle_b = math.degrees(math.acos((side_a**2 + side_c**2 - side_b**2) / (2 * side_a * side_c)))
    angle_c = math.degrees(math.acos((side_a**2 + side_b**2 - side_c**2) / (2 * side_a * side_b)))
    
    return angle_a, angle_b, angle_c

def plot_triangle(side_a=11, side_b=16, side_c=14):
    print(side_a,side_b,side_c)
    angles = find_angles(side_a, side_b, side_c)
    
    # Create a list of vertices (x, y) for the triangle
    vertices = [(0, 0), (side_a, 0), (side_c * math.cos(math.radians(angles[1])), side_c * math.sin(math.radians(angles[1])))]

    # Plot the triangle
    plt.gca().set_aspect('equal')  # Set aspect ratio to equal
    plt.triplot([v[0] for v in vertices], [v[1] for v in vertices], 'r--')
    plt.plot([v[0] for v in vertices], [v[1] for v in vertices], 'ro')

    # Add labels for the sides and angles
    plt.text(vertices[0][0] / 2, -1, f"Side A: {side_a}", ha='center')
    plt.text(vertices[1][0] / 2, -1, f"Side B: {side_b}", ha='center')
    plt.text(vertices[2][0] / 2, vertices[2][1] + 0.5, f"Side C: {side_c}", ha='center')
    plt.text(vertices[0][0] / 2, vertices[0][1] / 2, f"Angle A: {angles[0]:.2f}°", ha='center')
    plt.text(vertices[1][0] - 1, vertices[1][1] / 2, f"Angle B: {angles[1]:.2f}°", ha='center')
    plt.text(vertices[2][0] + 1, vertices[2][1] / 2, f"Angle C: {angles[2]:.2f}°", ha='center')

    # Set axis limits and labels
    plt.xlim(-1, side_a + 1)
    plt.ylim(-1, max(side_b, side_c) + 1)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Display the plot
    plt.savefig(filename)
    return angles




