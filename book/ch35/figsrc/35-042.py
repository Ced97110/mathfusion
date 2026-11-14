import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
rows = [('deux ondes : 3 et 4', 'sujet'), ('un point (3 ; 4)', 'sujet'), ('distance R = 5', 'varie'),
        ('direction α = 53,13°', 'varie'), ('une onde : 5 et 53,13°', 'resultat')]
for i, (lab, role) in enumerate(rows):
    y = 61 - 13 * i
    disc(ax, 8, y + 5, 3.6, role, label=str(i + 1), size='m')
    box(ax, 15, y, 71, 10, role, label=lab, size='m')
    if i < 4: arrow(ax, (50, y), (50, y - 3), 'fixe')
save(fig, '35-042')
