import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grid(ax, x, y, n, m, c, role, lw=0.35):
    for i in range(n):
        for j in range(m):
            poly(ax, [(x+i*c, y+j*c), (x+(i+1)*c, y+j*c), (x+(i+1)*c, y+(j+1)*c), (x+i*c, y+(j+1)*c)], role, lw=lw)
fig, ax = canvas(52)
c = 8
text(ax, 15, 30, '$3^2$', 'varie', 'l', weight='bold')
text(ax, 15, 22, '3 × 3', 'varie', 'm')
arrow(ax, (27, 30), (36, 30), 'varie')
grid(ax, 40, 12, 3, 3, c, 'sujet')
brace(ax, 40, 40 + 3 * c, 12, 'sujet', label='3 carrés', down=True)
text(ax, 71, 12 + 1.5 * c, '3 rangées', 'sujet', 's', ha='left')
text(ax, 55, 44, '9 carrés : « 3 au carré »', 'resultat', 's')
save(fig, '11-106')
