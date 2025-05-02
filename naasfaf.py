import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider
import math as  m

# --- Set up the figure and axis ---
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)
ax.set_aspect('equal')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.grid(True)
ax.set_title("Adjustable Gear Tracing Motion")

# --- Initial parameters ---
R1_init = 2.0        # Distance from Gear A to Gear B's center
R2_init = 1.0        # Distance from Gear B center to tracing point
omega_A_init = 1.0   # Angular speed of Gear A
omega_B_init = 4   # Angular speed of Gear B

# --- Data containers ---
xdata, ydata = [], []
cxdata, cydata = [], []

# --- Plot elements ---
orbit_path, = ax.plot([], [], lw=2, label="Trace Path")
center_path, = ax.plot([], [], '--', lw=1, alpha=0.5, label="Gear B Center Path")
point_dot, = ax.plot([], [], 'ro', label="Tracing Point")
ax.legend()

# --- Slider axes setup ---
axcolor = 'lightgoldenrodyellow'
slider_height = 0.03
s_omega_A = Slider(plt.axes([0.2, 0.25, 0.65, slider_height], facecolor=axcolor),
                   'Gear A Speed', 0.1, 5.0, valinit=omega_A_init)
s_omega_B = Slider(plt.axes([0.2, 0.2, 0.65, slider_height], facecolor=axcolor),
                   'Gear B Speed', 0.1, 5.0, valinit=omega_B_init)
s_R1 = Slider(plt.axes([0.2, 0.15, 0.65, slider_height], facecolor=axcolor),
              'Distance A to B', 0.1, 5.0, valinit=R1_init)
s_R2 = Slider(plt.axes([0.2, 0.1, 0.65, slider_height], facecolor=axcolor),
              'Distance B to Trace', 0.1, 5.0, valinit=R2_init)

# --- Initialization function ---
def init():
    orbit_path.set_data([], [])
    center_path.set_data([], [])
    point_dot.set_data([], [])
    return orbit_path, center_path, point_dot

# --- Animation update function ---
def update(frame):
    t = frame / 50.0  # Time variable

    # Read slider values
    omega_A = s_omega_A.val
    omega_B = s_omega_B.val
    R1 = s_R1.val
    R2 = s_R2.val

    # Gear B center position
    cx = R1 * np.cos(omega_A * t)
    cy = R1 * np.sin(omega_A * t)

    # Tracing point on Gear B
    px = cx + R2 * np.cos(omega_B * t)
    py = cy + R2 * np.sin(omega_B * t)

    xdata.append(px)
    ydata.append(py)
    cxdata.append(cx)
    cydata.append(cy)

    # Limit trace length
    if len(xdata) > 2000:
        xdata.pop(0)
        ydata.pop(0)
        cxdata.pop(0)
        cydata.pop(0)

    orbit_path.set_data(xdata, ydata)
    center_path.set_data(cxdata, cydata)
    point_dot.set_data([px], [py])  # ✅ Wrap in list to avoid RuntimeError

    return orbit_path, center_path, point_dot

# --- Create animation ---
ani = animation.FuncAnimation(fig, update, frames=range(10000),
                              init_func=init, blit=True, interval=20)

plt.show()
