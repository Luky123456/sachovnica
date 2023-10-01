from PIL import Image, ImageDraw
import pprint

sachovnica = []
for i in range(8):
    riadok = []
    for j in range(8):
        riadok.append(0)
    sachovnica.append(riadok)


def check(x: int, y: int) -> bool:
    for j in range(8):
        for i in range(8):
            if i == x or j == y or j + i == x + y or i - j == x - y:
                if sachovnica[j][i] == 1:
                    return False
    return True

pocitadlo = 0


def drticka(dama: int):
    global sachovnica
    global pocitadlo
    if dama == 8:
        pprint.pp(sachovnica)
        print("--------------------------")
        pocitadlo += 1
        h = 400
        w = 400
        img = Image.new("RGB", (h, w), (0, 0, 0))  
        pixels = img.load()  
        stvorec = img.size[0] // 8
        newimg = ImageDraw.Draw(img)
        for i in range(0,img.size[0],stvorec):
            for j in range(0,img.size[1],stvorec):
                horroh = (i, j)
                dolroh = (i + stvorec, j + stvorec)
                if ((i+j)/stvorec)%2 ==0:
                    newimg.rectangle([horroh, dolroh], fill='white')
        for stl in range(8):
            for ria in range(8):
                if sachovnica[ria][stl] == 1:   #check ci tam stoji dama
                    tup1 = (ria * stvorec, stl * stvorec)
                    tup2 = ((ria + 1) * stvorec, (stl + 1) * stvorec)
                    newimg.ellipse([tup1, tup2], fill='brown')     #vykreslenie damy
        img.save('dama' + str(pocitadlo) + '.jpg')
    else:
        for j in range(8):
            if check(j, dama):
                sachovnica[dama][j] = 1
                drticka(dama + 1)
                sachovnica[dama][j] = 0


drticka(0)
