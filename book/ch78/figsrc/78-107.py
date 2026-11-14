import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for i, d in enumerate(['1', '2', '4', '8', '16']):
    bad = d == '16'
    box(ax, 4 + i * 15, 24, 12, 10, 'limite' if bad else 'resultat', label=d, size='l')
brace(ax, 4, 55, 37, 'resultat', label=r'$|xy|=|x||y|$', down=False)
text(ax, 70, 46.5, r'$|xy|\neq|x||y|$', 'limite', 's')
text(ax, 70, 17, 'non alternatif', 'limite', 's')
text(ax, 70, 11, 'pas de composition', 'limite', 's')
text(ax, 4, 17, 'dimension', 'fixe', 's', ha='left')
save(fig, '78-107')
