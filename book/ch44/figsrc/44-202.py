import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
box(ax, 8, 60, 72, 11, 'varie', label='l’opération est l’addition')
rows = [('nombres', '3 + 5', '5 + 3'), ('rotations', '30° + 50°', '50° + 30°'), ('horloge de 4 h', '3 h + 2 h', '2 h + 3 h')]
for k, (n, a, b) in enumerate(rows):
    y = 40 - k * 18
    box(ax, 2, y, 22, 11, 'fixe', label=n, size='s')
    box(ax, 28, y, 23, 11, 'sujet', label=a)
    box(ax, 61, y, 23, 11, 'autre', label=b)
    line(ax, [(53.5, y + 6.5), (58.5, y + 6.5)], 'resultat', lw=1.2); line(ax, [(53.5, y + 4.5), (58.5, y + 4.5)], 'resultat', lw=1.2)
    arrow(ax, (44, 59.5), (44, 52.5), 'varie') if k == 0 else None
save(fig, '44-202')
