import numpy as np
from PIL import Image

# ---- IGNORE THIS PART -----------------------------------------
def load_image(filename, new_width=140):
    image = Image.open(filename)
    width, height = image.size
    aspect_ratio = height/width
    new_height = aspect_ratio * new_width * 0.45
    return np.array(image.resize((new_width, int(new_height))))
# ---- IGNORE THIS PART -----------------------------------------


def min_max_scaling(array):
    """
    normieren heisst: spanne zwischen min und max des input arrays
    werden zwischen 0 und 1 gesetzt
    """
    array_min = np.min(array)
    array_max = np.max((array))
    array_norm = (array - array_min)/(array_max - array_min)
    return array_norm

def get_numpy_array_infos(array):
    array_dtype = array.dtype
    array_size = array.size
    array_shape = array.shape
    array_min = np.min(array)
    array_max = np.max((array))
    print(array_dtype)
    print(array_size)
    print(array_shape)
    print(array_min)
    print(array_max)
    pass

def image_to_grayscale(image):
    """
    image to greyscale: look at 3rd dim of array (r, g, b data per pixel)
    > get mean of those three values
    norm values
    retun 2d normed array 
    """
    rgb_image_as_array = np.asanyarray(image)
    mono_image_as_array = np.mean(rgb_image_as_array, axis=2)

    # get_numpy_array_infos(rgb_image_as_array)
    # get_numpy_array_infos(mono_image_as_array)
    # print(mono_image_as_array)
    return mono_image_as_array

        
def image_to_ascii(image):
    """

    """
    chars = ["@", "B", "&", "#", "S", "$", "%", "p", "o", "*", "!", ";", ":", ".", " "]
    num_chars = len(chars)
    image_ascii = ""
    mono_image = image_to_grayscale(image)
    normed_mono = min_max_scaling(mono_image)
    #converted_to_chars = np.rint(normed_mono * num_chars)
    #converted_to_chars = converted_to_chars.astype(int)

    
    for row in normed_mono:
        for value in row:
            pixel_value = int(value * num_chars)
            image_ascii += chars[pixel_value-1]
        image_ascii += "\n"
    return image_ascii


# Die Bilddatei muss im gleichen Ordner wie das Pythonskript sein
filename = "/home/arabanus/Downloads/bike.png"
# Das Bild wird in die Variable image als NumPy-Array geladen 
image = load_image(filename)

print(image_to_ascii(image))
