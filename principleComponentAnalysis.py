import pickle
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA

ALPHABETS_COLLECTED = 21


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



# Perform PCA
def perform_pca(features):
    pca = PCA(n_components=2)
    pca.fit(features)
    transformed_features = pca.transform(features)
    return transformed_features

# Plot PCA-transformed points
def plot_pca_points(transformed_features, labels):
    plt.figure(figsize=(10, 8))
    for i in range(ALPHABETS_COLLECTED):  # Iterate over each alphabet class
        class_indices = [j for j, label in enumerate(labels) if label == i]
        class_points = transformed_features[class_indices]
        plt.scatter(class_points[:, 0], class_points[:, 1], label=f'Class {chr(i + ord("A"))}', alpha=0.7)
    plt.title('PCA-transformed Points')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
# Assuming 'transformed_data' contains PCA-transformed features and 'labels' contains corresponding labels
transformed_data = perform_pca(data)  # 'data' contains the 21 features per image per alphabet class
labels = np.array(labels)  # Convert labels to numpy array for easier manipulation
plot_pca_points(transformed_data, labels)
