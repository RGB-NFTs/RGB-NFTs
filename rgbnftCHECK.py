from PIL import Image


#image width and height
iwm=256
#pixel count, stands for how big each block should be
pc=int(iwm/64)  #iwm/64
pc=64
lista=[]
rares=0
ultrarares=0
t=8192


def gen(pixels,contx,conty,pc,lista):

        for x in range(pc):
            for y in range(pc):
                lista.append(pixels[x+contx,y+conty])

def check_rare(lista,name):
    global rares
    if (255, 0, 0) not in lista:
        print('No reds in',name)
        rares+=1
    if (0, 255, 0) not in lista:
        print('No greens in',name)
        rares+=1
    if (0, 0, 255) not in lista:
        print('No blues in',name)
        rares+=1

def check_ultrarare(lista,name):
    global ultrarares
    if (255, 0, 0) not in lista and (0, 255, 0) not in lista:
        print('Only blues in',name)
        ultrarares+=1
    if (0, 255, 0) not in lista and (0, 0, 255) not in lista:
        print('Only reds',name)

    if (0, 0, 255) not in lista and (255, 0, 0) not in lista:
        print('Only greens',name)

for n in range(t):
    name='rgbs_'+str(iwm)+'x'+str(iwm)+'_'+str(pc)+'px2/rgbnft_'+str(n+1)+'.png'
    img = Image.open(name)
    pixels=img.load()
    contx=0
    conty=-pc

    for r in range(int(iwm/pc)):
        contx=0
        if conty<=iwm-(pc*2):
            conty+=pc
        while contx<=iwm-pc:
            gen(pixels,contx,conty,pc,lista)
            contx+=pc

    check_rare(lista,name)
    check_ultrarare(lista,name)
    print(f"{(n+1)/t*100:.1f} %", end="\r")

    lista=[]
print('Total rares:',rares)
print('Total ultrarares:',ultrarares)
