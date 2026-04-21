import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function for Canny edge detection
def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

# Function to find region of interest
def region_of_interest(image):
    height = 700
    polygons = np.array([[(250, height), (1000, height), (600, 250)]], np.int32)
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_region = cv2.bitwise_and(image, mask)
    return masked_region
    

# Function to draw detected lines
def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1,y1), (x2,y2), (255,0,0), 10)
    return line_image

# Main lane detection pipeline
def detect_lanes(image_path):
    # Read the image
    image = cv2.imread(image_path)
    lane_image = np.copy(image)
    
    # Step 1: Apply Canny edge detection
    canny_image = canny(lane_image)
    
    # Step 2: Crop to region of interest
    cropped_image = region_of_interest(canny_image)
    
    # Step 3: Detect lines using Hough Transform
    lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    
    # Step 4: Draw detected lines
    line_image = display_lines(lane_image, lines)
    
    # Step 5: Combine original image with detected lines
    combo_image = cv2.addWeighted(lane_image, 1, line_image, 1, 1)
    
    # Display all steps
    plt.figure(figsize=(15, 10))
    
    plt.subplot(2, 3, 1)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    plt.subplot(2, 3, 2)
    plt.title("Canny Edge Detection")
    plt.imshow(canny_image, cmap='gray')
    plt.axis('off')
    
    plt.subplot(2, 3, 3)
    plt.title("Region of Interest")
    plt.imshow(cropped_image, cmap='gray')
    plt.axis('off')
    
    plt.subplot(2, 3, 4)
    plt.title("Hough Lines")
    plt.imshow(line_image)
    plt.axis('off')
    
    plt.subplot(2, 3, 5)
    plt.title("Final Result")
    plt.imshow(cv2.cvtColor(combo_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    plt.subplot(2, 3, 6)
    # Gaussian Blur visualization (intermediate step)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    plt.title("Gaussian Blur")
    plt.imshow(blur, cmap='gray')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

# Execute the lane detection
if __name__ == "__main__":
    detect_lanes("test_image.jpg")