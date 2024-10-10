import matplotlib.pyplot as plt
import numpy as np

# Define the system parameters
mass = 75  # Mass of the body (kg), assume an average person
damping_coefficient = 10  # Damping factor due to tissues and muscles
stiffness = 500  # Stiffness of bones and tendons (N/m)

#time vector for simulation
time=np.linspace(0,10,1000)


# Function to calculate displacement of the mass under vibration
def displacement(time, mass, damping_coefficient, stiffness):
    # Define the natural frequency of the system
    natural_frequency = np.sqrt(stiffness / mass)

    # Define the damping ratio
    damping_ratio = damping_coefficient / (2 * np.sqrt(mass * stiffness))

    # Solve the displacement for underdamped system (damping_ratio < 1)
    if damping_ratio < 1:
        # underdamped case (oscillatory motion)
        damped_frequency = natural_frequency * np.sqrt(1 - damping_ratio ** 2)

        # Exponential decay for displacement (due to damping)
        displacement = np.exp(-damping_ratio * natural_frequency * time) * \
                       np.cos(damped_frequency * time)
    else:
        # Critically damped or overdamped, solve accordingly
        displacement = np.zeros_like(time)  # Simplifying for this case

    return displacement
# Calculate displacement of the body under vibration
disp = displacement(time, mass, damping_coefficient, stiffness)

# Plot the result
plt.plot(time,disp, label="Displacement", color="Red")
plt.title("Human body Modelled under vibrations as a Mass-Spring-Damper System")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")

plt.grid(True)
plt.legend()
plt.show()
