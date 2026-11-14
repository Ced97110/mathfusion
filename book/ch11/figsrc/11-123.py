import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 7; yb = 24
cx = (15, 44, 73)
# length
for i in range(3): box(ax, cx[0]-1.5*u+i*u, yb, u, u, 'varie' if i == 0 else 'sujet', r=0.2)
# surface
for i in range(3):
    for j in range(3): box(ax, cx[1]-1.5*u+i*u, yb+j*u, u, u, 'varie' if (i, j) == (0, 2) else 'sujet', r=0.2)
# volume
c, o = 5, (cx[2], yb)
cells = [(i, j, k) for i in range(3) for j in range(3) for k in range(3) if (i, j, k) != (0, 0, 2)]
cubes(ax, cells, o, 4.6, 'sujet'); cubes(ax, [(0, 0, 2)], o, 4.6, 'varie')
for x, t in zip(cx, ('longueur', 'surface', 'volume')): text(ax, x, 60, t, 'encre', 'm')
for x, t in zip(cx, ('3 mm', '9 carrés', '27 cubes')): text(ax, x, 17, t, 'sujet', 's')
for x, t in zip(cx, ('mm', 'mm²', 'mm³')): text(ax, x, 9, t, 'varie', 'm', weight='bold')
save(fig, '11-123')
