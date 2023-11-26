# projectile_plot.py

import matplotlib.pyplot as plt

def plot_xy(x_positions, y_positions):
    """
    Plot x vs y position at each timestep.

    Args:
        x_positions (list): List containing x positions.
        y_positions (list): List containing y positions.
    """
    plt.figure(figsize=(8, 6))
    plt.plot(x_positions, y_positions, marker='o', linestyle='-')
    plt.title('Projectile Motion: x vs y Position')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.grid(True)
    plt.show()
