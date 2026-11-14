import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
rows = [(56, r'$u=2+i$', r'$N(u)=2$'), (40, r'$v=i$', r'$N(v)=1$'), (20, r'$uv=2+2i$', r'$N(uv)=2$')]
for y, l, r in rows:
    box(ax, 10, y, 30, 9, 'fixe', label=l, size='s')
    box(ax, 50, y, 30, 9, 'autre', label=r, size='s')
    arrow(ax, (40.5, y + 4.5), (49.5, y + 4.5), 'autre')
    text(ax, 45, y + 7.5, r'$N$', 'autre', 's')
line(ax, [(10, 60.5), (7, 60.5), (7, 24.5)], 'varie', lw=1.0)
line(ax, [(10, 44.5), (7, 44.5)], 'varie', lw=1.0)
arrow(ax, (7, 24.5), (9.8, 24.5), 'varie')
text(ax, 3.2, 42, 'multiplier', 'varie', 's', rot=90)
line(ax, [(80, 60.5), (83, 60.5), (83, 24.5)], 'varie', lw=1.0)
line(ax, [(80, 44.5), (83, 44.5)], 'varie', lw=1.0)
arrow(ax, (83, 24.5), (80.2, 24.5), 'varie')
text(ax, 85.8, 42, r'$2\times1=2$', 'varie', 's', rot=90)
text(ax, 44, 8, r'$N(uv)=N(u)\,N(v)$', 'autre', 's')
save(fig, '67-140')
