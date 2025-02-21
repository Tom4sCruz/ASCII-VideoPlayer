from PIL import Image

CHARS = ' .;+*?%S#@'

AM = 2 # Arbitrary Multiplier

def image_to_ascii(path):
    with Image.open(path) as img:
        # Converts image to Grayscale
        img = img.convert("L")
        
        width,height = img.size
        new_h = 148
        new_w = AM * int(new_h / height * width)
        # Resizes image
        img = img.resize((new_w, new_h))
        
        pixels = img.getdata()
        char_pixels = [CHARS[pixel//26] for pixel in pixels]
        
        num_pixels = len(char_pixels)

        ascii_image = [''.join(char_pixels[i:i+new_w]) for i in range(0, num_pixels, new_w)]
        ascii_image = '\n'.join(ascii_image)

        print(ascii_image)


if __name__ == "__main__":
    path = input("Paste the Path for an Image: ")
    path = "media/examples/black_hole.jpg" if path.strip() == '' else path
    image_to_ascii(path)

