import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
text(ax, 44, 90, r'$G$ : $12=2^2\times 3$ éléments', 'sujet', 'l')
xs = [10, 18, 26, 34]
rows = [(76, 'sujet'), (66, 'fixe'), (56, 'fixe')]
for y, role in rows:
    for x in xs:
        disc(ax, x, y, 3, role)
box(ax, 5, 72, 36, 8, 'sujet', fill=False, lw=1.1)
box(ax, 46, 70, 40, 12, 'sujet', label='Sylow donne $H$ :\n' + r'$4=2^2$ éléments')
arrow(ax, (41, 76), (46, 76), 'sujet')
box(ax, 46, 50, 40, 16, 'limite', label='3 rangées = degré 3\nsur $R$ : interdit')
arrow(ax, (41, 61), (46, 58), 'limite')
arrow(ax, (23, 51), (23, 40.5), 'fixe', lw=1.4)
text(ax, 26, 46, 'donc', 'fixe', 's', ha='left')
box(ax, 3, 28, 82, 12, 'resultat', label='seul cas possible : $m=1$\n$G$ est un 2-groupe')
arrow(ax, (44, 28), (44, 22.5), 'fixe', lw=1.4)
text(ax, 47, 25.2, 'donc', 'fixe', 's', ha='left')
box(ax, 3, 8, 82, 14, 'sujet', label='$E=R(i)$ : un degré 2 de plus\nest interdit par l’étape 1', weight='bold')
save(fig, '69-065')
