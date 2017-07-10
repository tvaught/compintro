#!/usr/bin/python

from PIL import Image

ASCII_CHARS_RAW = "#@%*=+;:,. "
ASCII_CHARS = list(ASCII_CHARS_RAW)

def scale_image(image, new_width=100):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    # because characters are twice as tall as wide, convert aspect_ratio to half
    aspect_ratio = (original_height/float(original_width))*0.5
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image
    
def map_pixels_to_ascii_chars(image, range_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies.

    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())

    pixels_to_chars = [ASCII_CHARS[pixel_value/range_width] for pixel_value in
            pixels_in_image]

    return "".join(pixels_to_chars)

def convert_image_to_ascii(image, new_width=100):
    image = scale_image(image)
    image = image.convert('L')  # Convert to grayscale

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
            xrange(0, len_pixels_to_chars, new_width)]

    return "\n".join(image_ascii)

def handle_image_conversion(image_filepath):
    image = None
    try:
        image = Image.open(image_filepath)
    except Exception, e:
        print "Unable to open image file {image_filepath}.".format(image_filepath=image_filepath)
        print e
        return

    image_ascii = convert_image_to_ascii(image)
    return image_ascii

if __name__=='__main__':

    image_file_path = "../img/test_portrait1.jpg"
    ascii_img = handle_image_conversion(image_file_path)
    #fh = open("../img/test.txt", 'wa')
    #fh.write(ascii_img)
    #fh.close()
    print ascii_img
