import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image (grayscale)
image = cv2.imread('D:\Work\#1 Subjects\CV\cv codes\images\jay.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate histogram
histogram = cv2.calcHist([image], [0], None, [256], [0, 256]).flatten()

# Total number of pixels
total_pixels = image.size

# Variables to track the optimal threshold and intermediate values
sum_all = np.dot(np.arange(256), histogram)  # Sum of all pixel intensities
sum_background = 0
weight_background = 0
weight_foreground = 0
max_variance = 0
optimal_threshold = 0
intermediate_thresholds = []  # To store all thresholds considered

# Iterate through all possible threshold values (0 to 255)
count = 0
for t in range(256):
    weight_background += histogram[t]
    if weight_background == 0:
        continue

    weight_foreground = total_pixels - weight_background
    if weight_foreground == 0:
        break

    sum_background += t * histogram[t]
    mean_background = sum_background / weight_background
    mean_foreground = (sum_all - sum_background) / weight_foreground

    # Between-class variance
    variance_between = weight_background * weight_foreground * (mean_background - mean_foreground) ** 2
    intermediate_thresholds.append((t, variance_between))

    # Update the optimal threshold if the variance is higher
    if variance_between > max_variance:
        max_variance = variance_between
        optimal_threshold = t
        count += 1

# Apply the optimal threshold
_, thresholded_image = cv2.threshold(image, optimal_threshold, 255, cv2.THRESH_BINARY)

# Plot histogram with iterative threshold
plt.figure(figsize=(10, 5))
plt.title("Grayscale Histogram with Threshold")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.plot(histogram, color='gray')
plt.axvline(x=optimal_threshold, color='red', linestyle='--', label=f'Threshold: {optimal_threshold}')
plt.legend()
plt.show()

# Plot all intermediate thresholds and their variance
thresholds, variances = zip(*intermediate_thresholds)
plt.figure(figsize=(10, 5))
plt.title("Threshold Values vs Variance")
plt.xlabel("Threshold Value")
plt.ylabel("Variance Between Classes")
plt.plot(thresholds, variances, color='blue', label='Variance')
plt.axvline(x=optimal_threshold, color='red', linestyle='--', label=f'Threshold: {optimal_threshold}')
plt.legend()
plt.show()

# Save and display the result


factor = 3
image = cv2.resize(image,(image.shape[1] // factor, image.shape[0] // factor))
thresholded_image = cv2.resize(thresholded_image,(thresholded_image.shape[1] // factor, thresholded_image.shape[0] // factor))


cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(intermediate_thresholds)



# Save the result
cv2.imwrite('thresholded_image_class.jpg', thresholded_image)
