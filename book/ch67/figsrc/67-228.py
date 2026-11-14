import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$m_u$, $u=a+bi$, base $(1,i)$', 'encre', 'm')
text(ax, 14, 36, r'$m_u=$', 'encre', 'm')
cells = [(30, 36, r'$a$', 'varie'), (44, 36, r'$-b$', 'fixe'), (30, 24, r'$b$', 'fixe'), (44, 24, r'$a$', 'varie')]
for x, y, s, ro in cells:
    box(ax, x, y, 14, 11, ro, label=s)
line(ax, [(28.5, 23), (26.5, 23), (26.5, 48), (28.5, 48)], 'encre')
line(ax, [(59.5, 23), (61.5, 23), (61.5, 48), (59.5, 48)], 'encre')
text(ax, 65, 42, 'diagonale', 'varie', 's', ha='left')
text(ax, 65, 36, r'$a+a=2a$', 'varie', 's', ha='left')
text(ax, 44, 10, 'aucun conjugué nécessaire', 'fixe', 's')
save(fig, '67-228')
