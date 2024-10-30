import sys
import os
from PIL import Image

def get_ascii_char(val):
    if val < 64:
        return '*'
    elif val < 128:
        return '#'
    elif val < 192:
        return '@'
    else:
        return '$'
        

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <image_path>")
        return
    img_path = sys.argv[1] #image path
    
    if os.path.exists(img_path):
        img = Image.open(img_path).convert('L')
        width, height = img.size
        pixel_vals = [[0 for _ in range(width)] for _ in range(height)]
        
        for i in range(height):
            for j in range(width):
                pixel_vals[i][j] = img.getpixel((j,i))
        
        txt_file = img_path.split('.')[0] + '.txt'
        with open(txt_file, 'w') as file:
            char = 'x'
            for i in range(height):
                for j in range(width): 
                    p_val = pixel_vals[i][j]
                    file.write(f'{get_ascii_char(p_val)}')
                file.write('\n')
        
        #print(pixel_vals)
    else:
        print('image not found make sure it is in the current directory')
        
    
    

if __name__ == "__main__":
    main()
