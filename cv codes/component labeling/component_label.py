import cv2
import numpy as np

# Read the image
image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

# Thresholding to get a binary image (black and white)
#_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

#making a labeling matrix
labels = np.zeros_like(image, dtype=int)

# Directions for 4-connected neighbors
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


#storing all the conflicting thingies
equivalence = {}

#starting woth 1 label, 0 for bg
current_label = 1


#getting height and width
height, width, channels = image.shape


# Find the connected components
for x in range (height):
    for y in range (width):
        #image[i,j]
        if image[x,y] == 0:
            # Check neighbors for labeling
            neighbors = []
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height and image[ny, nx] == 255:
                    if labels[ny, nx] > 0:  # If the neighbor is labeled
                        neighbors.append(labels[ny, nx])   
            if len(neighbors) == 0:
                # No neighbors, assign new label
                labels[y, x] = current_label
                current_label += 1
            else:
                # Assign the minimum label from neighbors
                min_label = min(neighbors)
                labels[y, x] = min_label
                # If there are multiple neighbors, we need to record equivalence
                for neighbor in neighbors:
                    if neighbor != min_label:
                        # Record equivalence: all the neighbors are part of the same component
                        equivalence[neighbor] = min_label

# Second pass: Resolve equivalences and assign final labels
# Iterate through all labels and change them based on equivalences
for y in range(height):
    for x in range(width):
        if labels[y, x] > 0:
            current_label = labels[y, x]
            # Keep checking equivalence until we get the root label
            while current_label in equivalence:
                current_label = equivalence[current_label]
            labels[y, x] = current_label

# Print number of components
print(f'Number of components: {num_components}')

# Display the original and labeled images
cv2.imshow('Original Image', image)
cv2.imshow('Labeled Image', labeled_image * 30)  # Multiply by 30 for better visualization

# Wait for key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
