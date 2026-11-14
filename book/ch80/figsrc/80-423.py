import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(58)
for y, s in ((44, 'ouvert'), (30, 'fermé')):
    box(ax, 2, y, 30, 10, 'varie', label=rf"$b$ {s}", size='m')
    arrow(ax, (32, y + 5), (42, y + 5), 'fixe')
    box(ax, 42, y, 44, 10, 'resultat', label=r"$I\vee b=I$", size='m')
text(ax, 44, 22, "si $\\vee$ était l'addition :", 'fixe', 's')
box(ax, 2, 4, 30, 10, 'limite', label=r"$I=5$, $b=3$", size='m')
arrow(ax, (32, 9), (42, 9), 'fixe')
box(ax, 42, 4, 44, 10, 'limite', label=r"$5\vee3=8\neq I$", size='m')
save(fig, '80-423')
