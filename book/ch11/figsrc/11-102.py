import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grid(ax, x, y, n, m, c, role, lw=0.35):
    for i in range(n):
        for j in range(m):
            poly(ax, [(x+i*c, y+j*c), (x+(i+1)*c, y+j*c), (x+(i+1)*c, y+(j+1)*c), (x+i*c, y+(j+1)*c)], role, lw=lw)
fig, ax = canvas(58)
c = 2.7
grid(ax, 6, 16, 12, 8, c, 'sujet')
grid(ax, 46, 16, 10, 10, c, 'autre')
text(ax, 6 + 6 * c, 10, 'tour : 40 m', 'sujet', 's')
text(ax, 46 + 5 * c, 10, 'tour : 40 m', 'autre', 's')
text(ax, 6 + 6 * c, 52, '96 carrés', 'sujet', 'm', weight='bold')
text(ax, 46 + 5 * c, 52, '100 carrés', 'autre', 'm', weight='bold')
text(ax, 44, 4, 'carré = 1 m², l’aire $A$ les compte', 'fixe', 's')
save(fig, '11-102')
