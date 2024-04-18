import pickle

# Load data from the pickle file
with open('data.pickle', 'rb') as f:
    data_dict = pickle.load(f)

# Extract labels and data from the data dictionary
labels = data_dict['labels']
data = data_dict['data']

# Initialize a dictionary to store lengths of sequences for each label
label_lengths = {}

# Iterate through labels and corresponding data sequences
for label, seq in zip(labels, data):
    # Check if the length of the sequence is already recorded for the label
    if len(seq) not in label_lengths:
        label_lengths[len(seq)] = [label]
    else:
        label_lengths[len(seq)].append(label)

# Iterate through label lengths dictionary and print labels with inhomogeneous sequences
for length, labels in label_lengths.items():
    if len(labels) > 1:
        print(f"Sequences of length {length} found for labels: {', '.join(labels)}")
