import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def row(y, cells, label):
    text(ax, 3, y + 8, label, 'encre', 'm', ha='left')
    for i, r in enumerate(cells): box(ax, 4 + i * 3.35, y, 3.0, 6, r, lw=0.5, r=0.3)
P, I = 'sujet', 'autre'
row(50, [P] * 12 + [I] * 12, r'$S_4$ : toutes, 24')
row(28, [P] * 12, r'$A_4$ : seulement les paires, 12')
row(6, [I] * 12, 'impaires : 12')
text(ax, 85, 34, 'moitié de $S_4$', 'sujet', 's', ha='right')
text(ax, 46, 3, "pas d'identité : pas un groupe", 'limite', 's', ha='left')
save(fig, '46-227')
