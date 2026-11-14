import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

assert 21 * 3 == 63 and -63 + 78 == 15 and 78 == 3 * 26
g = 6
val = 21 * g + 15
assert val == 141 and val % 26 == 11 and val == 5 * 26 + 11 and (5 * 21) % 26 == 1

fig, ax = canvas(80)
box(ax, 8, 66, 72, 10, 'sujet', label=r'$21\,(c - 3) = 21\,c - 63$')
box(ax, 8, 50, 72, 10, 'varie', label=r'$-63 + 78 = 15$  ($78 = 3 \times 26$)')
box(ax, 8, 34, 72, 10, 'resultat', label=r'$f^{-1}(c) = 21\,c + 15$ (mod 26)', weight='bold')
arrow(ax, (44, 66), (44, 60.5), 'fixe')
arrow(ax, (44, 50), (44, 44.5), 'fixe')
text(ax, 44, 27, 'test avec la lettre G', 'fixe', 's')
box(ax, 2, 6, 14, 14, 'sujet', label='G\n6')
box(ax, 22, 6, 44, 14, 'varie', label=r'$21 \times 6 + 15 = 141$' + '\n' + r'$141 = 5 \times 26 + 11$', size='s')
box(ax, 72, 6, 14, 14, 'resultat', label='L\n11')
arrow(ax, (17, 13), (21, 13), 'fixe')
arrow(ax, (67, 13), (71, 13), 'fixe')
save(fig, '53-058')
