import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 67, r'$2{,}35$', 'encre', 'xl', weight='bold')
rows = [('2', '1', '« deux »', 'sujet'), (',', '2', '« et »', 'varie'),
        ('35', '3', '« trente-cinq »', 'sujet'), ('5 : sa place', '4', '« centièmes »', 'resultat')]
for i, (chip, n, word, role) in enumerate(rows):
    y = 52 - i * 14
    box(ax, 4, y - 5, 28, 10, role, label=chip, size='m', weight='bold')
    arrow(ax, (33, y), (46, y), role, lw=1.0)
    text(ax, 49, y, n, role, 'm', ha='left', weight='bold')
    text(ax, 56, y, word, role, 'm', ha='left')
save(fig, '08-031')
