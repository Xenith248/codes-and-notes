import numpy as np
import cv2

def variable_thresholding(image, neighborhood_size, a, b, global_threshold=None):


    rows, cols = image.shape[:2]
    thresholded_image = np.zeros((rows, cols), dtype=np.uint8)

    for y in range(rows):
        for x in range(cols):
            # Define the neighborhood boundaries (handling edge cases)
            y_start = max(0, y - neighborhood_size // 2)
            y_end = min(rows, y + neighborhood_size // 2 + 1)
            x_start = max(0, x - neighborhood_size // 2)
            x_end = min(cols, x + neighborhood_size // 2 + 1)

            neighborhood = image[y_start:y_end, x_start:x_end]

            # Calculate standard deviation and mean of the neighborhood
            std_dev = np.std(neighborhood)
            if global_threshold is None:
                mean = np.mean(neighborhood)
            else:
                mean = global_threshold  # Use global threshold if provided

            # Calculate the threshold for the current pixel
            threshold = a * std_dev + b * mean

            # Apply the threshold
            if image[y, x] > threshold:
                thresholded_image[y, x] = 255  # or 1, depending on your preference
            else:
                thresholded_image[y, x] = 0

    return thresholded_image

# Example Usage:
# Load the image in grayscale
image = cv2.imread("path_to_your_image.jpg", cv2.IMREAD_GRAYSCALE)

# Set parameters
neighborhood_size = 5  # Adjust as needed
a = 0.5  # Adjust weights as needed
b = 0.5 

# Apply variable thresholding
thresholded_image = variable_thresholding(image, neighborhood_size, a, b)

# Display or save the result
cv2.imshow("Thresholded Image", thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
