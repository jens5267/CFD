import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np
import os

###############################################Creating the mean velocity profile################################################

# Creating the basic figure with the ramp
ramp_points_x = [-10, -10, 0, 22]
ramp_points_y = [0, 3.7, 3.7, 0]
required_ramp_point = 0
z1 = np.array(ramp_points_y)
z2 = np.array([required_ramp_point] * 4)
plt.figure(figsize=(25, 5))
plt.plot(ramp_points_x, ramp_points_y, color = 'black')
plt.xlim([-10, 50])
plt.ylim([0, 4.7])
plt.xlabel('$x/H + 10U/U_b$', fontsize=18)
plt.ylabel('$y/H$', fontsize=16)
x_ticks = [i if i in [-10, 0, 10, 20, 30, 40, 50] else '' for i in range(-10, 51)]
y_ticks = [i/10 if i/10 in [0, 1, 2, 3, 4] else '' for i in range(0,48)]
plt.xticks(np.arange(-10, 51), x_ticks)
plt.yticks(np.arange(0, 48) * 0.1, y_ticks)
plt.tick_params(right=True)
plt.tick_params(top=True)
plt.tight_layout()
plt.fill_between(ramp_points_x, ramp_points_y, 0,
                 where=(z1 >= z2),
                 alpha=0.30, color='grey', interpolate=True)
plt.title("Streamwise velocity profiles")
                 
# Obtaining the experimental results
location_experimental = 'data' # Location in the folder
letter = 'm'
variable = '__U'
section_code = ['-6', '6', '14', '20', '27', '34', '40', '47']
x_H = [-5.87, 5.98, 13.56, 20.32, 27.09, 33.87, 39.85, 46.62]

# Function for plotting the experimental data

def plot_experimental_data_from_file(file_location: str, letter: str, variable: str, section_code: str, x_H: float):
    final_location = os.getcwd() + '/' + file_location + '/' + letter + variable + '_x' + section_code + '.csv'
    text_data = np.loadtxt(final_location)
    y_data = list(reversed([ele[0] for ele in text_data]))
    x_data = list(reversed([x_H + 10 * ele[1] for ele in text_data]))
    plt.scatter(x_data, y_data, facecolors='none', edgecolors='b')
for i in range(len(section_code)):
    plot_experimental_data_from_file(file_location = location_experimental, letter = letter, variable = variable, section_code = section_code[i], x_H = x_H[i])

# Obtaining the velocity profile data

analysis = ['kOmegaSST', 'kEpsilonPhitF', 'LaunderSharmaKE', 'SpalartAlmaras']
color_list = ['green', 'pink', 'purple', 'black']
linestyle_list = ['dashed', 'solid', 'dotted', 'solid']

# Plotting the numerical data

def plot_numerical_data(text_data, x_H, range_for_data):
    
    # Obtaining the data from the numerical results 
    

    for m in range(len(analysis)):
        directories = sorted([int(x) for x in os.listdir(os.getcwd() + '/' + analysis[m] + '/' + 'postProcessing/surfaces')])
        last_time_directory = directories[-1]
        reading_file = os.getcwd() + '/' + analysis[m] + '/' + 'postProcessing/surfaces/' + str(last_time_directory) + '/U_velocityProfile.raw'
        text_data = np.loadtxt(reading_file) 
        range_for_data = [0.01, 0.03, 0.04, 0.031, 0.06, 0.06, 0.2, 0.33]
        plot_numerical_data(text_data, x_H, range_for_data)

# Adding the correct legend for the figure (This is only for adding the legend)

line_1 = Line2D([0,1],[0,1],color = 'blue', linestyle = 'none',marker='o',markersize=5, markerfacecolor="none")
line_2 = Line2D([0,1],[0,1],color = color_list[0], linestyle = linestyle_list[0])
line_3 = Line2D([0,1],[0,1],color = color_list[1], linestyle = linestyle_list[1])
line_4 = Line2D([0,1],[0,1],color = color_list[2], linestyle = linestyle_list[2])
line_5 = Line2D([0,1],[0,1],color = color_list[3], linestyle = linestyle_list[3])
plt.legend([line_1, line_2, line_3, line_4, line_5],['Experimental','k-Omega SST', 'k-Epsilon-Phit-F', 'Launder Sharma k-Epsilon', 'Spalart Allmaras'], loc='lower left', facecolor='white')

plt.savefig(f'Mean_velocity_profile.png', bbox_inches='tight',
             pad_inches=0.1, format='png')
plt.clf()
