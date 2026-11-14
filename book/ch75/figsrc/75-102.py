import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$\det(-A)=(-1)^m\,\det A$', 'sujet', 'l')
for cx, m, res in ((22, 2, r'$(-1)(-1)=1$'), (66, 3, r'$(-1)^3=-1$')):
    text(ax, cx, 46, f'$m={m}$ lignes', 'sujet', 'm')
    for k in range(m):
        y = 36 - k * 9
        box(ax, cx - 14, y, 28, 7, 'varie', label=r'ligne $\times(-1)$', size='s')
    text(ax, cx, 36 - m * 9 - 1, res, 'resultat', 'm')
save(fig, '75-102')
