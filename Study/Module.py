__author__ = 'Love Purple'

import sys

def test():
    args = sys.argv
    if len(args)==1:
            print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

#if __name__=='__main__':
  
from PIL import Image
im = Image.open("C:\\Users\\admin\\Desktop\\838d4a9a6dba98a25c1ae36b93f31db0_b.png") 
print(im.format,im.size,im.mode)

im.thumbnail((200,100))
im.save("thumb.jpg","JPEG")