from PIL import Image

image_path = 'your_file_path'
brightness_mode = 'average'
ascii_characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def get_image_object(path):
    return Image.open(path)

def rgb_to_averagebrightness(r, g, b):
    return int((r + g + b) / 3)

def rgb_to_luminance(r, g, b):
    return int(((r * 299)+ (g * 587)+ (b * 114)) / 1000)

def get_pixel_matrix(im):
    ''' Returns every pixel in an image in matrix form '''
    pixel_matrix = []

    # Loop over each pixel and append pixel data to list 
    for y in range(im.height):
        row = []

        for x in range(im.width):
            pixel_rgb = im.getpixel((x, y))
            row.append(pixel_rgb)

        pixel_matrix.append(row)
    
    return pixel_matrix

def get_pixelbrightness_matrix(pixel_matrix):
    ''' Returns pixel brightness from a given pixel matrix '''

    width = len(pixel_matrix[1])
    height = 0

    for _ in pixel_matrix:
        height += 1

    brightness_matrix = [[] for _ in range(height-1)]

    # Loop over each stored pixel data and insert to new list based on position
    for x in range(width-1):
        for y in range(height-1):
            pixel_rgb = pixel_matrix[y][x]
            brightness = None
            
            if brightness_mode.lower() == 'average':
                brightness = rgb_to_averagebrightness(pixel_rgb[0], pixel_rgb[1], pixel_rgb[2])
            elif brightness_mode.lower() == 'luminance':
                brightness = rgb_to_luminance(pixel_rgb[0], pixel_rgb[1], pixel_rgb[2])

            brightness_matrix[y].insert(x, brightness)

    return brightness_matrix

def get_ascii_matrix(brightness_matrix):
    ''' Returns char matrix from given brightness matrix 
    c = 20
    b = 0-100

    b[50] = c[10]
    b[60] = c[12]
    b[30] = c[6]
    b[75] = c[15]
    b[20] = c[4]

    y = 1/5x

    255/65 = ~1/4x
    '''

    ascii_matrix = list(brightness_matrix)

    for y in brightness_matrix:
        for x in y:
            ascii_matrix[y][x] = ascii_characters[int(x * 1/4)]

    return ascii_matrix

def pixelmatrix_to_picture(ascii_matrix):
    picture = ''

    # Scale results
    for y in ascii_matrix:
        for x in y:
            picture += x*2

        picture += '\n'

    return picture

if __name__ == '__main__':
    im = get_image_object(image_path)
    pixel_matrix = get_pixel_matrix(im)
    brightness_matrix = get_pixelbrightness_matrix(pixel_matrix)
    ascii_matrix = get_ascii_matrix(brightness_matrix)
    print(pixelmatrix_to_picture(ascii_matrix))