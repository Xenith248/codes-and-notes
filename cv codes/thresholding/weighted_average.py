import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
path = r"images\thresholding.png"
image = cv2.imread(path, cv2.IMREAD_GRAYSCALE )

# Calculate the histogram of the image
histogram = cv2.calcHist([image], [0], None, [256], [0, 256]).flatten()

# Total number of pixels
total_pixels = np.sum(histogram)

# Calculate the weighted average (threshold)
weighted_sum = np.dot(np.arange(256), histogram)  # Sum of (intensity * frequency)
threshold_value = weighted_sum / total_pixels  # Weighted average

# Apply global thresholding using the computed threshold
_, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

# Plot the original image, histogram, and thresholded image
plt.figure(figsize=(15, 5))


# Histogram with threshold value
plt.plot(histogram,)
plt.axvline(x=threshold_value, color='red', linestyle='--', label=f'Threshold: {threshold_value:.2f}')
plt.title('Histogram with Threshold')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.legend()
plt.show()

#showing both images
factor = 3
image = cv2.resize(image,(image.shape[1] // factor, image.shape[0] // factor))
thresholded_image = cv2.resize(thresholded_image,(thresholded_image.shape[1] // factor, thresholded_image.shape[0] // factor))
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Save the result
cv2.imwrite('weighted_thresholded_image.jpg', thresholded_image)
