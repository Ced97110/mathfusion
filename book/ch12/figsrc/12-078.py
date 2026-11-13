import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 2, 41, '3/4 =', 'encre', 'm', ha='left')
box(ax, 18, 36, 9, 10, 'fixe', label='0,')
for c, d in enumerate('75'):
    box(ax, 28 + 10 * c, 36, 9, 10, 'resultat', label=d)
line(ax, [(49.5, 34), (49.5, 48)], 'resultat', lw=1.6)
text(ax, 53, 41, 's’arrête', 'resultat', 's', ha='left')
text(ax, 2, 19, '15/11 =', 'encre', 'm', ha='left')
box(ax, 18, 14, 9, 10, 'fixe', label='1,')
for c, d in enumerate('3636'):
    box(ax, 28 + 10 * c, 14, 9, 10, 'varie', label=d)
text(ax, 72, 19, '…', 'varie', 'l')
brace(ax, 28, 46.5, 14, 'varie', label='bloc 36')
brace(ax, 48, 66.5, 14, 'varie', label='bloc 36')
save(fig, '12-078')
