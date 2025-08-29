import cv2

# Load the image (grayscale)
image = cv2.imread('D:\Work\#1 Subjects\CV\cv codes\images\jay.jpg', cv2.IMREAD_GRAYSCALE)

# Apply a basic threshold
threshold_value = 127  # Change this value as needed
max_value = 255
_, thresholded_image = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)

# Save the result
cv2.imwrite('thresholded_image.jpg', thresholded_image)

# Display the result (optional)
factor = 3
image = cv2.resize(image,(image.shape[1] // factor, image.shape[0] // factor))
thresholded_image = cv2.resize(thresholded_image,(thresholded_image.shape[1] // factor, thresholded_image.shape[0] // factor))
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
