import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 3, 18, 82, 46, 'sujet', fill=False, dash=True)
text(ax, 44, 59, r'$\mathbb{H}$ : tous les quaternions', 'sujet', 'l')
def strip(y, role):
    for k in range(4): box(ax, 22 + k * 11, y, 11, 8, role)
strip(44, 'sujet')
text(ax, 14, 48, r'$x$', 'sujet', 'l')
brace(ax, 22, 66, 44, 'sujet', label='4 réels', down=True)
for k in range(4): box(ax, 22 + k * 11, 24, 11, 8, 'fixe')
text(ax, 14, 28, r'$y$', 'fixe', 'l')
text(ax, 44, 9, r'$x\in\mathbb{H}$', 'resultat', 'l')
arrow(ax, (44, 17.5), (44, 13), 'resultat')
save(fig, '51-050')
