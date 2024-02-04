from PIL import Image

image_path = 'your_file_path'

im = Image.open(image_path)

pixel_matrix = []
pixel_flat = []
ascii_charcters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_matrix = [[] for _ in range(im.height)] #NOTE: iterating through width will flip and rotate image

def rgb_to_averagebrightness(r, g, b):
    return int((r + g + b) / 3)

def rgb_to_luminance(r, g, b):
    return int(((r * 299)+ (g * 587)+ (b * 114)) / 1000)

# Loop over each pixel and append pixel data to list 
for x in range(im.width):
    row = []
    pixel_matrix.append(row)

    for y in range(im.height):
        pixel_rgb = im.getpixel((x, y))
        row.append(pixel_rgb)
        pixel_flat.append(pixel_rgb)

'''
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

# Loop over each stored pixel data and insert to new list based on position
for x in range(im.width):
    for y in range(im.height):
        pixel = pixel_matrix[x][y]
        brightness = rgb_to_averagebrightness(pixel[0], pixel[1], pixel[2])
        ascii_matrix[y].insert(x, ascii_charcters[int(brightness * 1/4)]) #NOTE: table index and insert index MUST match ascii matrix

picture = ''

# Scale results
for x in ascii_matrix:
    for y in x:
        picture += y*2

    picture += '\n'

print(picture)