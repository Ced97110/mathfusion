import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(84)
# part de l'écart dans le sinus : 1 % = 8 mm
k = 8.0
blocs = [
    (50, 'sujet', r'$\sin 3{,}25°=0{,}05669$', r'$\sin 3{,}35°=0{,}05844$', r'$+0{,}00175\approx3\ \%$', 3.0),
    (12, 'autre', r'$\sin 60°=0{,}86603$', r'$\sin 60{,}1°=0{,}86690$', r'$+0{,}00087\approx0{,}1\ \%$', 0.1),
]
for y, role, l1, l2, l3, pct in blocs:
    box(ax, 4, y + 14, 38, 9, role, label=l1, size='s')
    box(ax, 46, y + 14, 38, 9, role, label=l2, size='s')
    arrow(ax, (42, y + 18.5), (46, y + 18.5), 'varie')
    ax.add_patch(Rectangle((4, y + 5), pct * k, 3.4, ec=COL['varie'], fc=FILL['varie'], lw=0.7, zorder=2))
    text(ax, 4 + pct * k + 2, y + 6.7, l3, 'varie', 's', ha='left')
text(ax, 44, 80, 'même ajout de 0,1°, effets différents', 'encre', 'm')
text(ax, 44, 45, 'barre : part de l’écart (1 % = 8 mm)', 'fixe', 's')
save(fig, '38-079')
