import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grid(ax, x, y, n, m, c, role, lw=0.35):
    for i in range(n):
        for j in range(m):
            poly(ax, [(x+i*c, y+j*c), (x+(i+1)*c, y+j*c), (x+(i+1)*c, y+(j+1)*c), (x+i*c, y+(j+1)*c)], role, lw=lw)
fig, ax = canvas(52)
c = 3.4
grid(ax, 8, 12, 8, 8, c, 'sujet')
text(ax, 8 + 4 * c, 7, '8 po', 'varie', 's')
text(ax, 4, 12 + 4 * c, '8 po', 'varie', 's', rot=90)
text(ax, 8 + 4 * c, 46, '64 carrés d’un pouce', 'sujet', 's')
text(ax, 62, 38, r'8 × 8 = 8$^2$', 'varie', 'm')
text(ax, 62, 30, r'po × po = po$^2$', 'varie', 'm')
text(ax, 62, 21, r'= 64 po$^2$', 'resultat', 'l', weight='bold')
text(ax, 62, 14, 'pouces carrés', 'resultat', 's')
save(fig, '11-100')
