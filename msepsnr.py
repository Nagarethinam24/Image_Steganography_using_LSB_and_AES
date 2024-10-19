import cv2
import numpy as np
import math

def calculate_mse(image1, image2):
    squared_diff = np.square(image1 - image2)
    mse = np.mean(squared_diff)
    return mse

def calculate_psnr(image1, image2):
    mse = calculate_mse(image1, image2)
    max_pixel_value = 255.0  # Assuming 8-bit images
    psnr = 20 * math.log10(max_pixel_value / math.sqrt(mse))
    return psnr

# Load the images
image1 = cv2.imread("demo.png", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("demoencoded.png", cv2.IMREAD_GRAYSCALE)

# Calculate MSE and PSNR
mse_value = calculate_mse(image1, image2)
psnr_value = calculate_psnr(image1, image2)

print("MSE:", mse_value)
print("PSNR:", psnr_value)
