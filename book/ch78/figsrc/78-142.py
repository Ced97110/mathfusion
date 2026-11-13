import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
T = [(1,2,4),(2,3,5),(3,4,6),(4,5,7),(5,6,1),(6,7,2),(7,1,3)]
pos = [(3 + 22 * i, 38) for i in range(4)] + [(3 + 22 * i, 14) for i in range(3)]
for k, (t, (x, y)) in enumerate(zip(T, pos)):
    role = 'sujet' if k == 0 else ('varie' if k == 4 else 'fixe')
    box(ax, x, y, 16, 9, role, label='$(%d,%d,%d)$' % t, size='s')
for k in range(6):
    if k == 3: continue
    (x, y), (x2, _) = pos[k], pos[k + 1]
    arrow(ax, (x + 16, y + 4.5), (x2, y + 4.5), 'varie')
arrow(ax, (77, 38), (11, 23), 'varie', curve=-0.15)
text(ax, 11, 8.5, '$7+1=8\\to1$', 'varie', 's')
text(ax, 75, 17, '+1 à chaque\nindice', 'varie', 's')
save(fig, '78-142')
