import os
from PIL import Image, ImageOps

media_path = 'input_media'

images = list(os.walk(media_path))[0][2]

images = [image for image in images if image.split('.')[-1] in ('jpg', 'png', 'jpeg')]

for i in range(len(images)):
    name = f'image{i+1}.jpg'

    old_name = f'input_media/{images[i]}'
    new_name = f'input_media/{name}'
    print(old_name, new_name)
    os.rename(old_name, new_name)

    image = Image.open(f'input_media/{name}')

    image = image.resize((1080, 1080))

    image = ImageOps.grayscale(image)

    wm = Image.open('watermark.png').resize((100, 100))

    image.paste(wm, (25, 25), wm)
    image.save(f'output_media/{name}')