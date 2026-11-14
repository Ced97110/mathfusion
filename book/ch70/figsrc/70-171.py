import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
rows = [(50, 'plusieurs équations', r'$x-1=0$ et $y-2=0$', r'$(x-1)^2+(y-2)^2=0$'),
        (30, 'plusieurs « différent de 0 »', r'$x\neq 0$ et $y\neq 0$', r'$xy\neq 0$'),
        (10, 'une inégalité', r'$x>0$', r'$\exists z,\ xz^2-1=0$')]
for y, head, a, b in rows:
    text(ax, 2, y + 16, head, 'encre', 's', ha='left', weight='bold')
    box(ax, 2, y, 38, 12, 'sujet', label=a, size='s')
    arrow(ax, (42, y + 6), (46, y + 6), 'varie')
    box(ax, 48, y, 38, 12, 'resultat', label=b, size='s')
save(fig, '70-171')
