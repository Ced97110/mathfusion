import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 54, 60, r'$A_n$ : paires, $n!/2$', 'resultat', 's')
text(ax, 74, 54, 'impaires', 'fixe', 's')
x0, w = 24, 60
rows = [(r'$S_3$ : 6', '3', '3'), (r'$S_4$ : 24', '12', '12'), (r'$S_5$ : 120', '60', '60')]
for k, (lab, a, b) in enumerate(rows):
    y = 38 - k * 17
    text(ax, 2, y + 5, lab, 'fixe', 's', ha='left')
    box(ax, x0, y, w / 2, 10, 'resultat', label=a, size='m')
    box(ax, x0 + w / 2, y, w / 2, 10, 'fixe', label=b, size='m')
save(fig, '65-029')
