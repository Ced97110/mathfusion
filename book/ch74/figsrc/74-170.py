import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
s, x0, y0 = 40, 5, 8
C = lambda u, v: (x0 + u*s, y0 + v*s)
poly(ax, [C(0,0), C(1,0), C(1,1), C(0,1)], 'fixe', fill=False)
def dia(x, y): poly(ax, [(x-1.9, y), (x, y+2.6), (x+1.9, y), (x, y-2.6)], 'sujet')
for p in [(0,0),(1,0),(1,1),(0,1)]:
    x, y = C(*p); box(ax, x-3.4, y-3.4, 6.8, 6.8, 'varie', fill=False, r=0.3, lw=1.1); dia(x, y)
x, y = C(.5, .5); box(ax, x-3.4, y-3.4, 6.8, 6.8, 'varie', fill=False, r=0.3, lw=1.1); disc(ax, x, y, 2.2, 'resultat')
arrow(ax, (x+8, y), (x, y+8), 'varie', curve=0.5)
text(ax, x+9, y+9.5, 'quart de tour', 'varie', 's', ha='left')
text(ax, 25, 54, '5 centres d’ordre 4', 'varie', 'm')
lx = 52
box(ax, lx-3.4, 30-3.4, 6.8, 6.8, 'varie', fill=False, r=0.3, lw=1.1)
dia(lx, 30)
text(ax, lx+5, 30, '4 sommets', 'sujet', 's', ha='left')
box(ax, lx-3.4, 18-3.4, 6.8, 6.8, 'varie', fill=False, r=0.3, lw=1.1)
disc(ax, lx, 18, 2.2, 'resultat')
text(ax, lx+5, 18, '1 centre', 'resultat', 's', ha='left')
save(fig, '74-170')
