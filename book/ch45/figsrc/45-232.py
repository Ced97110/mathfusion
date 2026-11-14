import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 72, 'bijections à essayer', 'encre', 'm', weight='bold')
for i, n in enumerate([6, 5, 4, 3, 2, 1]):
    box(ax, 4 + i * 13.6, 54, 11, 11, 'fixe', label=str(n), size='l')
text(ax, 44, 47, r'$6\times5\times4\times3\times2\times1=720$', 'limite', 'm', weight='bold')
arrow(ax, (44, 43), (44, 36), 'varie')
text(ax, 62, 39.5, 'un seul test suffit', 'varie', 's', ha='left')
box(ax, 2, 12, 40, 20, 'autre')
text(ax, 22, 27, r'$\mathbb{Z}/6$', 'autre', 'm'); text(ax, 22, 18, r'$a+b=b+a$', 'resultat', 'm')
box(ax, 46, 12, 40, 20, 'sujet')
text(ax, 66, 27, r'$S_3$', 'sujet', 'm'); text(ax, 66, 18, r'$ab\neq ba$ parfois', 'limite', 'm')
text(ax, 44, 5, '0 bijection essayée', 'resultat', 'm', weight='bold')
save(fig, '45-232')
