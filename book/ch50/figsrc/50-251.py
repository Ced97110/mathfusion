import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 58, 'liste des ordres possibles', 'fixe', 's')
for i, (n, m) in enumerate([('20', 'comptage'), ('48', 'normalisateur'), ('56', 'compter\nles éléments')]):
    x = 4 + 21 * i
    box(ax, x, 28, 17, 16, 'fixe'); text(ax, x + 8.5, 48, n, 'encre', 'l', weight='bold')
    line(ax, [(x + 1, 29), (x + 16, 43)], 'limite', lw=1.2); line(ax, [(x + 1, 43), (x + 16, 29)], 'limite', lw=1.2)
    text(ax, x + 8.5, 20 if '\n' in m else 21, m, 'fixe', 's')
box(ax, 67, 28, 17, 16, 'varie', fill=False, dash=True, label='…', size='l')
text(ax, 75.5, 21, 'à barrer', 'varie', 's')
text(ax, 44, 8, 'but : tout barrer', 'varie', 'm', weight='bold')
save(fig, '50-251')
