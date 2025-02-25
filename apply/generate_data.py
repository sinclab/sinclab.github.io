import pandas as pd
import numpy as np
from scipy.signal import gaussian

# Set parameters
n_subjects = 7  
n_dyads = 4  
timepoints = 60  

# Define dyad assignments using lists of tuples instead of a dictionary
# Each tuple contains (subject_id, dyad_id)
dyad_assignments = [
    (1, "A"), (2, "A"),
    (3, "B"), (4, "B"),
    (5, "C"), (6, "C"),
    (5, "D"), (7, "D"),
    (8, "E"), (9, "E"),
    (10, "F"), (11, "F"),
    (12, "G"), (13, "G"),
    (14, "H"), (15, "H"),
    (16, "I"), (17, "I"),
    (18, "J"), (19, "J"),
    (20, "K"), (21, "K"),
    (22, "L"), (23, "L"),
    (24, "M"), (25, "M")
]  

# Simulate neural power with a Gaussian-smoothed random walk
def generate_neural_power(timepoints):
    random_walk = np.cumsum(np.random.randn(timepoints) * 0.05)
    smooth_filter = gaussian(15, std=2)
    smooth_filter /= smooth_filter.sum()
    return np.convolve(random_walk, smooth_filter, mode='same') + 0.3  

data = []

for subj_id, dyad_id in dyad_assignments:
    power_series = generate_neural_power(timepoints)  
    for t in range(timepoints):
        data.append({
            "subj_id": subj_id,
            "dyad_id": dyad_id,
            "time": t,
            "power": np.round(power_series[t], 3)
        })

df = pd.DataFrame(data)
df.to_csv("dyad_neural_data.csv", index=False)