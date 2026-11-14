import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 20, 72, 'avant', 'fixe', 's')
text(ax, 68, 72, 'dans ce chapitre', 'resultat', 's')
rows = [('ch. 55 : symétriques', r'groupe de l\'équation : $S_n$'),
        ('ch. 46 : parité', 'discriminant : carré ?'),
        ('ch. 50 : Sylow', 'le 5-cycle')]
for i, (a, b) in enumerate(rows):
    y = 52 - i * 20
    box(ax, 2, y, 34, 12, 'fixe', label=a, size='s')
    box(ax, 50, y, 36, 12, 'resultat', label=b.replace("\\'", "'"), size='s')
    arrow(ax, (37, y + 6), (49, y + 6), 'varie', lw=1.3)
save(fig, '65-152')
