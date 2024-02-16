import numpy as np
import matplotlib.pyplot as plt
import pickle


ALPHABETS_COLLECTED = 14


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


def plot_heatmaps(data, labels):
    num_classes = ALPHABETS_COLLECTED
    num_rows = (num_classes + 4) // 5  # Calculate the number of rows needed for the subplot grid
    fig, axs = plt.subplots(num_rows, 5, figsize=(20, 4 * num_rows))
    
    for i in range(num_classes):
        row = i // 5
        col = i % 5
        class_indices = [j for j, label in enumerate(labels) if label == i]
        class_data = np.array([data[j] for j in class_indices])
        if class_data.size > 0:  # Check if class_data is not empty
            avg_coordinates = np.mean(class_data, axis=0)
            axs[row, col].hist2d(avg_coordinates[::2], avg_coordinates[1::2], bins=20, cmap='hot')
            axs[row, col].set_title(f'Class {chr(i + ord("A"))}')
            axs[row, col].set_xlabel('X Values')
            axs[row, col].set_ylabel('Y Values')
            axs[row, col].grid(True)
            fig.colorbar(axs[row, col].collections[0], ax=axs[row, col], label='Counts')
        else:
            axs[row, col].set_title(f'Class {chr(i + ord("A"))} (No Data)')
            axs[row, col].axis('off')  # Hide the subplot if there's no data
    
    plt.tight_layout()
    plt.show()

# Example usage:
plot_heatmaps(data, labels)