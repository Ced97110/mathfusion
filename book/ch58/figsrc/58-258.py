import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 24, 68, '1re case', 'fixe', 's')
text(ax, 48, 68, '2e case', 'fixe', 's')
rows = [(52, 'sujet', '−2', '0', 'sur X : 2e case = 0'),
        (36, 'varie', '3', '3', 'sur Z : cases égales')]
for y, role, a, b, tag in rows:
    box(ax, 14, y, 20, 11, role, label=a, size='l', weight='bold')
    box(ax, 38, y, 20, 11, role, label=b, size='l', weight='bold')
    text(ax, 62, y + 5.5, tag, role, 's', ha='left')
text(ax, 8, 41.5, '+', 'encre', 'l', weight='bold')
line(ax, [(5, 31.5), (60, 31.5)], 'encre', lw=1.0)
box(ax, 14, 14, 20, 11, 'resultat', label='1', size='l', weight='bold')
box(ax, 38, 14, 20, 11, 'resultat', label='3', size='l', weight='bold')
text(ax, 62, 19.5, 'P = (1, 3)', 'resultat', 'm', ha='left', weight='bold')
text(ax, 24, 6, '−2 + 3 = 1', 'resultat', 's')
text(ax, 48, 6, '0 + 3 = 3', 'resultat', 's')
save(fig, '58-258')
