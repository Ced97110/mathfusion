import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grid(ax, x, y, n, m, c, role, lw=0.35):
    for i in range(n):
        for j in range(m):
            poly(ax, [(x+i*c, y+j*c), (x+(i+1)*c, y+j*c), (x+(i+1)*c, y+(j+1)*c), (x+i*c, y+(j+1)*c)], role, lw=lw)
fig, ax = canvas(56)
c = 14
grid(ax, 6, 10, 2, 2, c, 'sujet', lw=0.6)
text(ax, 6 + c, 5, '2 po', 'varie', 's')
text(ax, 2.5, 10 + c, '2 po', 'varie', 's', rot=90)
text(ax, 6 + c, 44, '4 carrés d’un pouce', 'sujet', 's')
poly(ax, [(52, 24), (52 + 8, 24), (52 + 8, 32), (52, 32)], 'sujet', lw=0.8)
text(ax, 56, 20, '1 po de côté', 'sujet', 's')
text(ax, 56, 36, '1 po$^2$', 'sujet', 'm', weight='bold')
text(ax, 69, 12, r'4 po$^2$', 'resultat', 'm', weight='bold')
text(ax, 69, 5.5, r'pas 2 po$^2$', 'limite', 's')
save(fig, '11-101')
