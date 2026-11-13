import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
for i in (1, 2, 3):
    for j in (1, 2, 3):
        x = 8 + (j - 1) * 26; y = 52 - (i - 1) * 16
        role = 'resultat' if i < j else ('limite' if i > j else 'fixe')
        box(ax, x, y, 24, 14, role, label=f'({i}, {j})', size='m')
text(ax, 22, 10, r'gardées : $i<j$', 'resultat', 's')
text(ax, 66, 10, r'en double : $i>j$', 'limite', 's')
save(fig, '55-081')
