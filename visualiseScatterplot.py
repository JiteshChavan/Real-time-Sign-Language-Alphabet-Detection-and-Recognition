import pickle
import matplotlib.pyplot as plt
import numpy as np

ALPHABETS_COLLECTED = 10

def map_to_letter(number):
    if 0 <= number <= 25:
        return chr(number + ord('A'))
    else:
        return None

# Load data from pickle file
with open('data.pickle', 'rb') as f:
    data_dict = pickle.load(f)

data = data_dict['data']
labels = data_dict['labels']

# Convert labels to integers for proper sorting
labels = [int(label) for label in labels]


def map_to_letter(number):
    if 0 <= number <= 25:
        return chr(number + ord('A'))
    else:
        return None

# Sort labels
sorted_indices = sorted(range(len(labels)), key=lambda k: labels[k])



def plot_landmarks(label, landmarks_list):
    """
    Plot scatterplot for the landmarks of all images belonging to a specific label.

    Args:
    - label (int): The label (alphabet) associated with the landmarks.
    - landmarks_list (list): A list containing the x and y values of the landmarks for all images.

    Returns:
    - None
    """
    plt.figure(figsize=(8, 6))
    plt.title(f"Landmarks for Label {map_to_letter(label)}")
    
    # Extract x and y values for all landmarks
    x_values = np.array(landmarks_list)[:, ::2]
    y_values = np.array(landmarks_list)[:, 1::2]
    
    # Plot each feature with different color coding
    for i in range(x_values.shape[1]):  # Iterate over each feature
        plt.scatter(x_values[:, i], y_values[:, i], label=f'Feature {i+1}')

    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.legend()
    plt.grid(True)
    plt.show()



#scatter plot of features for visualisation of 14 alphabet classes
for label_to_plot in range(ALPHABETS_COLLECTED):  
    landmarks_list = []
    for i, label in enumerate(labels):
        if label == label_to_plot:
            landmarks = data[i]
            landmarks_list.append(landmarks)
    if landmarks_list:
        plot_landmarks(label_to_plot, landmarks_list)