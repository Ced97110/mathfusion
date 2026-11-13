import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
S = ('sin 0,8', 'autre'); C = ('cos 0,6', 'sujet'); U = ('1', 'fixe')
rows = [(S, C, 'tan ≈ 1,3333'), (U, C, 'sec ≈ 1,6667'), (U, S, 'cosec = 1,25'), (C, S, 'cotan = 0,75')]
for i, (num, den, res) in enumerate(rows):
    y = 79 - i * 19
    box(ax, 4, y, 20, 7, num[1], label=num[0], size='s')
    line(ax, [(4, y - 1.25), (24, y - 1.25)], 'encre', lw=1.0)
    box(ax, 4, y - 9.5, 20, 7, den[1], label=den[0], size='s')
    arrow(ax, (28, y - 1.25), (40, y - 1.25), 'varie')
    box(ax, 42, y - 5.75, 42, 9, 'resultat', label=res, size='m')
text(ax, 44, 4.5, 'on vérifie : diviseur ≠ 0', 'varie', 'm')
save(fig, '31-095')
