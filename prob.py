import random

r=0
cont=0
n=0
name=''

def tryd():
    colors=[]
    cc=0
    while cc!=16: #1/3 ^ 16 = 1/43mln
        a=random.randint(1,3)
        colors.append(a)
        cc+=1

    return colors


while True:
    cont=0
    n+=1
    name='RGB_NFTs_'+str(n)
    print(name)
    random.seed(name)
    colors=tryd()
    print(colors)
    if 1 in colors and 2 not in colors and 3 not in colors:
        print('FINALMENTE (ROSSO)')
        print(name)
        break
    if 2 in colors and 1 not in colors and 3 not in colors:
        print('FINALMENTE (VERDE)')
        print(name)
        break
    if 3 in colors and 1 not in colors and 2 not in colors:
        print('FINALMENTE (BLU)')
        print(name)
        break
