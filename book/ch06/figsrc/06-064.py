import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
bx, bw, bh = 26, 58, 13
box(ax, bx, 64, bw, bh, 'sujet', label=r'$M\times\frac{2}{5}=\frac{3}{4}$')
box(ax, bx, 36, bw, bh, 'varie', label=r'$M\times1=\frac{3}{4}\times\frac{5}{2}$')
box(ax, bx, 8, bw, bh, 'resultat', label=r'$M=\frac{15}{8}$')
xm = bx + 12
arrow(ax, (xm, 64), (xm, 49), 'varie'); arrow(ax, (xm, 36), (xm, 21), 'varie')
text(ax, xm + 3, 56.5, r'$\times\frac{5}{2}$ des deux côtés', 'varie', 's', ha='left')
text(ax, xm + 3, 28.5, 'à gauche : $\\frac{2}{5}\\times\\frac{5}{2}=1$', 'varie', 's', ha='left')
for y, t, r in [(70.5, 'départ', 'sujet'), (42.5, 'étape clé', 'varie'), (14.5, 'arrivée', 'resultat')]:
    text(ax, 13, y, t, r, 's', weight='bold')
save(fig, '06-064')
