import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import yaml
import pandas as pd

# Load the brown dwarf spectrum data
file_path = 'brown_dwarf.txt'
brown_dwarf_data = pd.read_csv(file_path, delim_whitespace=True, header=None, names=['Wavelength', 'Intensity'])

brown_dwarf_data.head()
from scipy.optimize import curve_fit

# Function to calculate the least squares difference
def calculate_least_squares(observed, template):
    return np.sum((observed - template) ** 2)
T0 = [0, 6 + 1]
T1 = [7, 12 + 1]
T2 = [13, 19 + 1]
T3 = [20, 23 + 1]
T4 = [24, 30 + 1]
T5 = [31, 41 + 1]
T6 = [42, 51 + 1]
T7 = [52, 56 + 1]
T8 = [57, 57 + 1]

L0 = [0, 5 + 1]
L1 = [6, 24 + 1]
L2 = [25, 32 + 1]
L3 = [33, 36 + 1]
L4 = [37, 46 + 1]
L5 = [47, 59 + 1]
L6 = [60, 69 + 1]
L7 = [70, 73 + 1]
L8 = [74, 77 ]
L9 = [77, 84 + 1]
# Load YAML file
with open("config.yaml") as file:
    config = yaml.safe_load(file)

# Extract necessary paths from the config
path_parent = config['workdir']
template_path_lt = config['templates_MLT']
templates_lt_list = config['templates_T_list']


#arr = np.genfromtxt(path_parent + templates_lt_list, dtype=str)[int(T5[0]):int(T5[1])]

# Load data from file list
arr = np.genfromtxt(path_parent + templates_lt_list, dtype=str)[int(T8[0]):int(T8[1])]
print(arr)
# Plotting
plt.figure(figsize=(6, 8))  # Adjust the figure size as per your preference

for i in range(len(arr)-1, -1,-1):  # Rweverse loop
    file_name = arr[i]
    # Load data from file
    data = np.loadtxt(path_parent + template_path_lt + file_name).T
    # Plot data with legend
    plt.plot(data[0], data[1], label=file_name[:-4])
    plt.title(file_name)
    plt.show()