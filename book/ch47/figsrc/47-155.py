import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for y, a, b, ra, rb, cap in [(42, 'R', 'S', 'sujet', 'varie', 'rotation · retournement'), (22, 'S', 'R', 'varie', 'sujet', 'retournement · rotation')]:
    box(ax, 6, y - 5, 14, 10, ra, label=a, size='l'); box(ax, 32, y - 5, 14, 10, rb, label=b, size='l'); box(ax, 58, y - 5, 14, 10, 'varie', label='S', size='l')
    text(ax, 26, y, '·', 'encre', 'l'); text(ax, 52, y, '=', 'encre', 'l')
    text(ax, 39, y - 8, cap, 'fixe', 's')
box(ax, 8, 2, 72, 8, 'resultat', label='R est le neutre du quotient', size='s')
save(fig, '47-155')
