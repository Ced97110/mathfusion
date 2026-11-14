import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
s, x0, y0 = 44, 3, 6
text(ax, x0 + s/2, 55, 'carreau central de p4m', 'sujet', 'm')
C = lambda u, v: (x0 + u*s, y0 + v*s)
poly(ax, [C(0,0), C(1,0), C(1,1), C(0,1)], 'fixe')
for a, b in [((0,0),(1,0)), ((1,0),(1,1)), ((1,1),(0,1)), ((0,1),(0,0)), ((0,.5),(1,.5)), ((.5,0),(.5,1)), ((0,0),(1,1)), ((0,1),(1,0))]:
    line(ax, [C(*a), C(*b)], 'sujet', lw=1.0)
m = [(.5,0), (1,.5), (.5,1), (0,.5)]
for k in range(4):
    line(ax, [C(*m[k]), C(*m[(k+1)%4])], 'resultat', lw=1.2, dash=True)
for p in [(0,0),(1,0),(1,1),(0,1),(.5,.5)]:
    x, y = C(*p); box(ax, x-1.6, y-1.6, 3.2, 3.2, 'varie', r=0.2)
for p in m:
    x, y = C(*p); poly(ax, [(x-2, y), (x, y+2.7), (x+2, y), (x, y-2.7)], 'encre')
lx = 55
items = [('miroirs', 'sujet'), ('symétrie glissée', 'resultat'), ("centres d’ordre 4", 'varie'), ("centres d’ordre 2", 'encre')]
for k, (lab, role) in enumerate(items):
    y = 40 - k*10
    if k == 0: line(ax, [(lx-4, y), (lx+2, y)], role, lw=1.2)
    elif k == 1: line(ax, [(lx-4, y), (lx+2, y)], role, lw=1.2, dash=True)
    elif k == 2: box(ax, lx-2.2, y-1.6, 3.2, 3.2, role, r=0.2)
    else: poly(ax, [(lx-2.2, y), (lx-.2, y+2.7), (lx+1.8, y), (lx-.2, y-2.7)], role)
    text(ax, lx+5, y, lab, role if role != 'encre' else 'fixe', 's', ha='left')
save(fig, '74-167')
