from PIL import Image, ImageFilter

# Open an image file
image = Image.open("example.jpg")  # Replace "example.jpg" with the path to your image file

# Display some information about the image
print("Image Format:", image.format)
print("Image Size:", image.size)
print("Image Mode:", image.mode)

# Show the original image
image.show()

# Apply a simple image filter (blur)
blurred_image = image.filter(ImageFilter.BLUR)

# Show the blurred image
blurred_image.show()

# Save the modified image to a new file
blurred_image.save("blurred_example.jpg")

# Close the original image
image.close()
