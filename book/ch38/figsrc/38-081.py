import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
# deux nombres de même longueur dessinée (100 %) ; l'ajout est mis à l'échelle de sa part
L = 62.0
x0 = 6
rows = [(42, 'sujet', r'$\sin3{,}25°=0{,}05669$', r'$+0{,}00175$ : $3\ \%$', 3.0),
        (18, 'autre', r'$\sin60°=0{,}86603$', r'$+0{,}00087$ : $0{,}1\ \%$', 0.1)]
for y, role, l1, l2, pct in rows:
    text(ax, x0, y + 9.5, l1, role, 's', ha='left')
    ax.add_patch(Rectangle((x0, y), L, 5, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    w = L * pct / 100
    ax.add_patch(Rectangle((x0 + L, y), w, 5, ec=COL['varie'], fc=COL['varie'], lw=0.8, zorder=3))
    text(ax, x0, y - 3.6, l2, 'varie', 's', ha='left')
text(ax, 44, 62, 'le même écart, comparé au nombre', 'encre', 'm')
text(ax, 44, 4.5, 'barre = le nombre (100 %)', 'fixe', 's')
save(fig, '38-081')
