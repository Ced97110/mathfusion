import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 70, r'écrire le point $(5,\,4)$', 'fixe', 's')
# deux moitiés de la définition
box(ax, 34, 56, 24, 9, 'sujet', label='génératrice', size='s')
box(ax, 60, 56, 26, 9, 'varie', label='indépendante', size='s')
text(ax, 46, 52, 's’écrit ?', 'sujet', 's')
text(ax, 73, 52, 'une seule façon ?', 'varie', 's')
rows = [('(1, 0)', '✗', 'limite', '—', 'fixe'),
        ('(1, 0), (0, 1), (1, 1)', '✓', 'resultat', '✗', 'limite'),
        ('(1, 0), (0, 1)', '✓', 'resultat', '✓', 'resultat')]
ys = [38, 24, 10]
for (fam, a, ra, b, rb), y in zip(rows, ys):
    box(ax, 2, y, 30, 10, 'fixe', label=fam, size='s')
    text(ax, 46, y + 5, a, ra, 'l', weight='bold')
    text(ax, 73, y + 5, b, rb, 'l', weight='bold')
save(fig, '58-168')
