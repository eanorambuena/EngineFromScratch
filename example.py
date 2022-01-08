from eggdriver import Image
from engine import *

def tablero(x, colors):
    m = []
    assert x % 2 == 0
    mid = int(x / 2)
    for j in range(mid):
        f = []
        for i in range(mid):
            f.append(colors[0])
            f.append(colors[1])
        m.append(f)
        f = []
        for i in range(mid):
            f.append(colors[2])
            f.append(colors[3])
        m.append(f)

    return  m

i = Image()
i.loadFromRGB(tablero(660, [red, green, blue, white])) # 36 maximo en esta pantalla
i.printRGB()
