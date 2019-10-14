# Import library
from steg import steg_img

# Extracting
# Select the carrier image
s_prime = steg_img.IMG(image_path="D:/Projekt/LiU/TNM031/TNM031-Keylogger/new.jpeg")
# Extract the payload
s_prime.extract()
