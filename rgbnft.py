import random
from PIL import Image

#setting up the seed
random.seed('RGB_NFTs_41057157')

#image width and height
iwm=256

#pixel count, stands for how big each block should be
pc=64

#times you want the code to run. Every time it runs, it generates an image
t=8192

#creating the blank image
img=Image.new('RGB', (iwm,iwm))

#loading the blank image pixels
pixels=img.load()

#function that creates the 16x16 block
def gen(pixels,contx,conty,pc):
        #randomly picks a number between 1 to 3.
        #1=red, 2=green, 3=blue
        r=random.randint(1,3)
        if r==1:
            color=((256), (0), (0))
        elif r==2:
            color=((0), (256), (0))
        elif r==3:
            color=((0), (0), (256))

        #colors the 16x16 block
        for x in range(pc):
            for y in range(pc):
                pixels[x+contx,y+conty]=color


for n in range(t):

    contx=0
    conty=-pc

    for r in range(int(iwm/pc)):  #256/64=4
        contx=0
        if conty<=iwm-(pc*2):
            conty+=pc
        while contx<=iwm-pc:
            gen(pixels,contx,conty,pc)
            contx+=pc

    #names the image "rgbnft_number", where the number starts from 0 and ends to t-1 in the "rgbs_256x256_64px" folder
    name='rgbs_'+str(iwm)+'x'+str(iwm)+'_'+str(pc)+'px/rgbnft_'+str(n)+'.png'
    #prints the %
    print(f"{(n+1)/8192*100:.1f} %", end="\r")
    #saves the image
    img.save(name)
