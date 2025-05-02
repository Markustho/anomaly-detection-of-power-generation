import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 300)

# Step 1: Create a circle
x = np.cos(theta)
y = np.sin(theta)

# Step 2: Scale it
a = 5  # semi-major axis
b = 2  # semi-minor axis
x_scaled = a * x
y_scaled = b * y

# Step 3: Rotate it
phi = np.radians(30)  # 30 degrees
x_rotated = x_scaled * np.cos(phi) - y_scaled * np.sin(phi)
y_rotated = x_scaled * np.sin(phi) + y_scaled * np.cos(phi)

# Plot
plt.plot(x_rotated, y_rotated)
plt.axis('equal')
plt.title("Ellipse built from rotation + scaling")
plt.grid(True)
plt.show()
