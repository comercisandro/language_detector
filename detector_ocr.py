# show an image
from PIL import ImageDraw
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import easyocr

from langdetect import detect

dir_path = 'Input/'
#font = ImageFont.truetype("arial.ttf", 18)
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 28, encoding="unic") 
reader = easyocr.Reader(['es'], model_storage_directory='./model/', user_network_directory='./model/', gpu=False)

def draw_boxes(name, image, bounds, width=2, text=False):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        #Descomentar para solo detectar letras con ese tamaño de alto
        """if(p2[1] - p0[1] < 100):
            continue"""
        draw.line([*p0, *p1, *p2, *p3, *p0], fill='blue', width=width) # random colors to better see
        if text:
            w, h = font.getsize(bound[1])
            x,y = p0[0]-10, p0[1]-10
            c = np.random.randint(100)+155
            draw.rectangle((x, y, x + w, y + h), fill=(c,c,c))
            draw.text([x,y],bound[1],fill='blue',font=font,stroke_fill='white')
            
            print(bound[1])
            idiom=detect(bound[1])
            print(idiom)

    image.save('Output/' + name)

    return image

def process_images(input_dir, show_text=False):
    files = os.listdir(input_dir)
    for image_name in files:
        path = input_dir + image_name
        print(path)
        image = Image.open(path)
        image_result = reader.readtext(path, text_threshold=0.8, min_size=400, paragraph=True)
        # Draw bounding boxes
        draw_boxes(image_name, image, image_result, text=show_text)

process_images(dir_path, True)