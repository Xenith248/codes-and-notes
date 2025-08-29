import cv2
import numpy as np

def moving_average(data, window_size):
    result = []
    for i in range(len(data) - window_size + 1):
        window_sum = sum(data[i:i + window_size])  # Compute sum of the window
        result.append(window_sum / window_size)  # Compute average
    
    return result

def variable_thresholding(image, window_size=3):
    flattened_image = image.flatten().tolist()
    moving_avg_thresholds = moving_average(flattened_image, window_size)
    
    # Pad the threshold values to match the image size
    padded_thresholds = moving_avg_thresholds + [moving_avg_thresholds[-1]] * (len(flattened_image) - len(moving_avg_thresholds))
    
    # Apply thresholding pixel-wise
    thresholded_image = np.array([255 if pixel > thresh else 0 for pixel, thresh in zip(flattened_image, padded_thresholds)], dtype=np.uint8)
    
    return thresholded_image.reshape(image.shape)

image_path = "images\moving.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
output = variable_thresholding(image, window_size=3000)
cv2.imshow("input", image)
cv2.imshow("Moving Average", output)
cv2.waitKey(0)
cv2.destroyAllWindows()