import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(46)
items = [(3, 'sujet', r'$D$'), (19, 'varie', r'$T(2)$'), (35, 'sujet', r'$D^{-1}$'), (51, 'varie', r'$T(-2)$')]
for x, role, lab in items: box(ax, x, 22, 13, 12, role, label=lab, size='m')
text(ax, 67.5, 28, '=', 'encre', 'l'); box(ax, 71, 22, 14, 12, 'resultat', label=r'$T(6)$', size='m')
brace(ax, 3, 48, 20, 'fixe', label=r'$D\,T(2)\,D^{-1}=T(8)$', down=True)
brace(ax, 51, 85, 20, 'varie', label=r'$8-2=6$', down=True)
brace(ax, 3, 64, 36, 'encre', label=r'commutateur $g\,h\,g^{-1}\,h^{-1}$', down=False)
save(fig, '73-159')
