import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(ax, x, y, r, role, lw=2.2):
    th = [i * math.pi / 90 for i in range(181)]
    line(ax, [(x + r * math.cos(t), y + r * math.sin(t)) for t in th], role, lw=lw)
fig, ax = canvas(84)
disc(ax, 22, 66, 8, 'sujet'); ring(ax, 22, 66, 8, 'sujet', 1.4)
disc(ax, 64, 66, 16, 'autre'); ring(ax, 64, 66, 16, 'autre', 1.4)
arrow(ax, (33, 66), (45, 66), 'varie', lw=1.2)
text(ax, 39, 70, r'$\times$ 2', 'varie', 's')
text(ax, 22, 42, r'$d$ = 10 cm', 'sujet', 's'); text(ax, 22, 38, r'$C$ = 31,4 cm', 'sujet', 's')
text(ax, 64, 42, r'$d$ = 20 cm', 'autre', 's'); text(ax, 64, 38, r'$C$ = 62,8 cm', 'autre', 's')
box(ax, 4, 22, 38, 8, 'resultat', label=r'31,4 $\div$ 10 = 3,14', size='s')
box(ax, 46, 22, 38, 8, 'resultat', label=r'62,8 $\div$ 20 = 3,14', size='s')
text(ax, 44, 12, r'$C$ $\div$ $d$ : le même nombre', 'resultat', 'm', weight='bold')
save(fig, '11-087')
