from main import Simulation
from visualization import Visualization

# Variables
view = False

# Run the Simulation
sim = Simulation(3137)
sim.start(view,1)
sim.run_simulation(view,1000)

# Display the simulation
sim.run_visualization()
