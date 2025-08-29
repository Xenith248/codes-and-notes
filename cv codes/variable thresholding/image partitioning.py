import cv2
import numpy as np

def variable_thresholding(image_path, grid_size=(4, 4), threshold_type=cv2.THRESH_BINARY):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    h, w = image.shape
    gh, gw = grid_size
    ph, pw = h // gh, w // gw  # Partition height and width
    
    result = np.zeros_like(image)

    
    for i in range(gh):
        for j in range(gw):
            y1, y2 = i * ph, (i + 1) * ph if (i + 1) * ph < h else h
            x1, x2 = j * pw, (j + 1) * pw if (j + 1) * pw < w else w
            
            partition = image[y1:y2, x1:x2]
            
            # Calculate the histogram of the image segment
            histogram = cv2.calcHist([partition], [0], None, [256], [0, 256]).flatten()
            total_pixels = np.sum(histogram)
            
            if total_pixels == 0:
                threshold_value = 0  # Avoid division by zero
            else:
                # Calculate the weighted average (threshold)
                weighted_sum = np.dot(np.arange(256), histogram)  # Sum of (intensity * frequency)
                threshold_value = weighted_sum / total_pixels  # Weighted average
            
            # Apply thresholding to the partition only
            _, thresholded_partition = cv2.threshold(partition, threshold_value, 255, threshold_type)
            result[y1:y2, x1:x2] = thresholded_partition
    
    return result


image_path = "images\image1.jpg"  # Replace with actual image path
image = cv2.imread(image_path)
output = variable_thresholding(image_path, grid_size=(10, 10))
cv2.imshow("input", image)
cv2.imshow("Variable Thresholding", output)
cv2.waitKey(0)
cv2.destroyAllWindows()