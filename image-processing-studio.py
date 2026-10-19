import PIL
from PIL import Image
import numpy as np
import ipywidgets
import os
# Prepopulated Imports - Inline Display
from IPython.display import display
from IPython.display import Image as Img

# Prepopulated Imports - Custom Script (all functions imported)
from image_data_functions import *

input_file = "original_image.jpg"

# Names of the files that will contain the modified images.
grayscale_file = "grayscale_image.png"
brightness_file = "brightness_image.png"
invert_file = "inverted_image.png"
stacked_file = "stacked_image.png"

# Controls how much the brightness is changed.
brightness_change = 40
def read_image_data(filename):
    """
    Opens an image and stores its pixel information in a 2D list.

    Each pixel is stored as a 1D list:
    [red, green, blue]

    The rows of pixels are stored in a 2D list.
    """

    # Open the image file.
    image_file = Image.open(filename)

    # Convert the image to RGB so every pixel has three channels.
    image_file = image_file.convert("RGB")

    # Store important information about the original image.
    image_width = image_file.width
    image_height = image_file.height
    image_mode = image_file.mode

    # Convert the image into a NumPy array.
    image_array = np.array(image_file)

    # Convert the NumPy array into nested Python lists.
    pixel_data = image_array.tolist()

    # Close the image file after reading its information.
    image_file.close()

    # Return both the pixel data and image information.
    return pixel_data, image_width, image_height, image_mode

original_pixels, image_width, image_height, image_mode = read_image_data(
    input_file
)

print("========================================")
print("        IMAGE PROCESSING STUDIO")
print("========================================")

print("Original file:", input_file)
print("Image width:", image_width, "pixels")
print("Image height:", image_height, "pixels")
print("Color mode:", image_mode)
print("Color channels:", len(original_pixels[0][0]))
print("Total pixels:", image_width * image_height)

print("Original file:", input_file)
print("Image width:", image_width, "pixels")
print("Image height:", image_height, "pixels")
print("Color mode:", image_mode)
print("Color channels:", len(original_pixels[0][0]))
print("Total pixels:", image_width * image_height)

file_size = os.path.getsize(input_file)
print("File size:", file_size, "bytes")

print("\nFirst pixel:")
print(original_pixels[0][0])

print("\nOriginal image:")

display(Img(filename=input_file))
def grayscale_image(pixel_data):
    """
    Converts an image into grayscale.

    This function uses nested loops to access every pixel
    in the 2D pixel list.
    """

    # Empty 2D list for the modified image.
    grayscale_pixels = []

    # Outer loop accesses each row.
    for row in pixel_data:

        # Create an empty list for the new row.
        new_row = []

        # Inner loop accesses each pixel.
        for pixel in row:

            # Pixel is a 1D list containing RGB values.
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            # Calculate a grayscale value.
            gray_value = (red + green + blue) // 3

            # Create a new grayscale RGB pixel.
            new_pixel = [
                gray_value,
                gray_value,
                gray_value
            ]

            # Add the new pixel to the row.
            new_row.append(new_pixel)

        # Add the completed row to the 2D list.
        grayscale_pixels.append(new_row)

    return grayscale_pixels

grayscale_pixels = grayscale_image(original_pixels)

print("\n========================================")
print("GRAYSCALE RESULT")
print("========================================")

print("Original pixel:", original_pixels[0][0])
print("Grayscale pixel:", grayscale_pixels[0][0])

def adjust_brightness(pixel_data, amount):
    """
    Changes the brightness of every RGB value.

    Positive values make the image brighter.
    Negative values make the image darker.

    Conditional statements prevent RGB values from
    becoming greater than 255 or less than 0.
    """

    # Empty 2D list for the modified image.
    brightness_pixels = []

    # Loop through every row.
    for row in pixel_data:

        # Create a new row.
        new_row = []

        # Loop through every pixel.
        for pixel in row:

            # Create a new 1D list for the pixel.
            new_pixel = []

            # Loop through each RGB channel.
            for channel_value in pixel:

                # Change the channel value.
                new_value = channel_value + amount

                # Decision-making prevents invalid RGB values.
                if new_value > 255:
                    new_value = 255

                elif new_value < 0:
                    new_value = 0

                # Add the corrected value to the pixel.
                new_pixel.append(new_value)

            # Add the modified pixel to the row.
            new_row.append(new_pixel)

        # Add the row to the 2D image list.
        brightness_pixels.append(new_row)

    return brightness_pixels

brightness_pixels = adjust_brightness(
    original_pixels,
    brightness_change
)

print("\n========================================")
print("BRIGHTNESS RESULT")
print("========================================")

print("Brightness change:", brightness_change)
print("Original pixel:", original_pixels[0][0])
print("Brightness pixel:", brightness_pixels[0][0])

def invert_colors(pixel_data):
    """
    Inverts the RGB values of every pixel.

    The new value is calculated with:
    255 - original value
    """

    # Empty 2D list for the inverted image.
    inverted_pixels = []

    # Outer loop accesses each row.
    for row in pixel_data:

        # Create a new row.
        new_row = []

        # Inner loop accesses each pixel.
        for pixel in row:

            # Create a new pixel.
            new_pixel = []

            # Loop through each RGB channel.
            for channel_value in pixel:

                # Invert the color value.
                inverted_value = 255 - channel_value

                # Add the new value to the pixel.
                new_pixel.append(inverted_value)

            # Add the modified pixel to the row.
            new_row.append(new_pixel)

        # Add the row to the image.
        inverted_pixels.append(new_row)

    return inverted_pixels

inverted_pixels = invert_colors(original_pixels)

print("\n========================================")
print("INVERTED RESULT")
print("========================================")

print("Original pixel:", original_pixels[0][0])
print("Inverted pixel:", inverted_pixels[0][0])

def reconstruct_image(pixel_data):
    """
    Converts a 2D list of RGB pixel data into a PIL image.
    """

    # Convert the 2D Python list into a NumPy array.
    image_array = np.array(pixel_data, dtype=np.uint8)

    # Convert the NumPy array into a PIL image.
    reconstructed_image = Image.fromarray(
        image_array,
        mode="RGB"
    )

    return reconstructed_image

def export_image(pixel_data, filename):
    """
    Reconstructs pixel data and saves the result as a PNG file.
    """

    # Reconstruct the image.
    reconstructed_image = reconstruct_image(pixel_data)

    # Export the reconstructed image.
    reconstructed_image.save(filename, format="PNG")

    # Close the reconstructed image file.
    reconstructed_image.close()
    
export_image(
    grayscale_pixels,
    grayscale_file
)

export_image(
    brightness_pixels,
    brightness_file
)

export_image(
    inverted_pixels,
    invert_file
)

print("\n========================================")
print("INDIVIDUAL MANIPULATIONS")
print("========================================")

print("\n1. GRAYSCALE")
display(Img(filename=grayscale_file))

print("\n2. BRIGHTNESS")
display(Img(filename=brightness_file))

print("\n3. COLOR INVERSION")
display(Img(filename=invert_file))

# Start with the original 2D pixel list.
stacked_pixels = original_pixels

# First manipulation: grayscale.
stacked_pixels = grayscale_image(stacked_pixels)

# Second manipulation: brightness.
stacked_pixels = adjust_brightness(
    stacked_pixels,
    brightness_change
)

# Third manipulation: color inversion.
stacked_pixels = invert_colors(stacked_pixels)

export_image(
    stacked_pixels,
    stacked_file
)

print("\n========================================")
print("STACKED MANIPULATIONS")
print("========================================")

print("Original")
print("   ↓")
print("Grayscale")
print("   ↓")
print("Brightness +", brightness_change)
print("   ↓")
print("Color Inversion")
print("   ↓")
print("Final Image")

display(Img(filename=stacked_file))

# This variable determines which effect the program selects.
selected_effect = "stacked"


# Start with the original image data.
selected_pixels = original_pixels


# Decide which manipulation to perform.
if selected_effect == "grayscale":

    selected_pixels = grayscale_image(
        selected_pixels
    )

elif selected_effect == "brightness":

    selected_pixels = adjust_brightness(
        selected_pixels,
        brightness_change
    )

elif selected_effect == "invert":

    selected_pixels = invert_colors(
        selected_pixels
    )

elif selected_effect == "stacked":

    selected_pixels = grayscale_image(
        selected_pixels
    )

    selected_pixels = adjust_brightness(
        selected_pixels,
        brightness_change
    )

    selected_pixels = invert_colors(
        selected_pixels
    )

else:

    print("Invalid effect selected.")
    selected_pixels = original_pixels

selected_file = "selected_effect.png"

export_image(
    selected_pixels,
    selected_file
)

print("\n========================================")
print("FINAL PROGRAM OUTPUT")
print("========================================")

print("Selected effect:", selected_effect)
print("Output file:", selected_file)

display(Img(filename=selected_file))

print("\n========================================")
print("PROJECT SUMMARY")
print("========================================")

print("Original image:", input_file)
print("Image dimensions:", image_width, "x", image_height)
print("Color mode:", image_mode)

print("\nFiles created:")
print("-", grayscale_file)
print("-", brightness_file)
print("-", invert_file)
print("-", stacked_file)
print("-", selected_file)

print("\nImage processing complete!")