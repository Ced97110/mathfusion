import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def panel(y0, title, rl, rows, rr):
    text(ax, 44, y0+27, title, rl, 'm', weight='bold')
    for k, (lab, res) in enumerate(rows):
        y = y0 + 12 - k*12 + 2
        box(ax, 3, y, 44, 9, rl, label=lab, size='s')
        arrow(ax, (49, y+4.5), (62, y+4.5), 'varie')
        box(ax, 64, y, 20, 9, rr, label=res, size='m')
panel(38, r'homothétie $\times 3$', 'sujet',
      [('cisaillement, puis ×3', '(6, 3)'), ('×3, puis cisaillement', '(6, 3)')], 'resultat')
panel(2, 'dilatation des largeurs ×2', 'autre',
      [('cisaillement, puis ×2', '(4, 1)'), ('×2, puis cisaillement', '(3, 1)')], 'limite')
text(ax, 44, 70, 'départ : (1, 1)', 'fixe', 's')
save(fig, '73-051')
