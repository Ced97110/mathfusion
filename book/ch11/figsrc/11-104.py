import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grid(ax, x, y, n, m, c, role, lw=0.35):
    for i in range(n):
        for j in range(m):
            poly(ax, [(x+i*c, y+j*c), (x+(i+1)*c, y+j*c), (x+(i+1)*c, y+(j+1)*c), (x+i*c, y+(j+1)*c)], role, lw=lw)
fig, ax = canvas(56)
c = 8
grid(ax, 6, 14, 4, 3, c, 'sujet')
text(ax, 6 + 2 * c, 9, '$L$ = 4 m', 'varie', 's')
text(ax, 3.5, 14 + 1.5 * c, '$l$ = 3 m', 'varie', 's', rot=90)
text(ax, 6 + 2 * c, 45, '3 rangées de 4 dalles', 'sujet', 's')
text(ax, 62, 40, r'$A$ = $L$ × $l$', 'sujet', 'm')
text(ax, 62, 32, '4 × 3 = 12', 'varie', 'm')
text(ax, 62, 25, r'm × m = m$^2$', 'varie', 'm')
text(ax, 62, 15, r'$A$ = 12 m$^2$', 'resultat', 'l', weight='bold')
save(fig, '11-104')
