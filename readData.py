import pickle


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

# Sort labels
sorted_indices = sorted(range(len(labels)), key=lambda k: labels[k])

# Print data in the desired format
for i in sorted_indices:
    label = labels[i]
    landmarks = data[i]
    
    
    # Print label
    print(f"({map_to_letter(label)}) : ", end='')
    
    # Print x and y values
    for j in range(0, len(landmarks), 2):
        x = landmarks[j]
        y = landmarks[j+1]
        print(f"[{(j/2)}]x = {x} y = {y} ", end=' ')
    
    print()  # Move to the next line for the next data point
    print()

