import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'$F_5$ : pente voulue b = 4', 'encre', 'l')
rows = [('sujet', r'$d=2,\ d^2-1=3$'), ('varie', r'$3\times 2=6\equiv 1$ : inverse 2'),
        ('varie', r'$c=4\times 2=8\equiv 3$'), ('resultat', r'$3\times 3=9\equiv 4=b$')]
ys = [54, 40, 26, 12]
for i, (r, l) in enumerate(rows):
    box(ax, 12, ys[i], 64, 9, r, label=l, size='m')
    if i: arrow(ax, (44, ys[i - 1]), (44, ys[i] + 9.3), 'fixe')
text(ax, 80, 16.5, 'vérifié', 'resultat', 's', ha='right') if False else None
save(fig, '73-168')
