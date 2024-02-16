import seaborn as sns
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


def plot_violin_plots(data, labels):
    num_classes = ALPHABETS_COLLECTED
    num_rows = (num_classes + 4) // 5  # Calculate the number of rows needed for the subplot grid
    fig, axs = plt.subplots(num_rows, 5, figsize=(15, 4 * num_rows), sharex=True)
    
    for i in range(num_classes):
        row = i // 5
        col = i % 5
        class_indices = [j for j, label in enumerate(labels) if label == i]
        class_data = [data[j] for j in class_indices]
        sns.violinplot(data=class_data, ax=axs[row, col], inner='point')
        axs[row, col].set_title(f'Class {chr(i + ord("A"))}')
        axs[row, col].set_xlabel('Landmark Index')
        axs[row, col].set_ylabel('Coordinate Value')
    
    plt.tight_layout()
    plt.show()

# Example usage:
plot_violin_plots(data, labels)
