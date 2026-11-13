import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
text(ax, 44, 64, r'$10^{81}=10\times(10^{10})^{8}$', 'sujet', 'l')
box(ax, 2, 40, 10, 11, 'sujet', label='10')
for i in range(8):
    box(ax, 14 + 9 * i, 40, 8.4, 11, 'varie')
brace(ax, 14, 85.4, 51, 'varie', label='8 blocs, chacun 10¹⁰', down=False)
arrow(ax, (50, 39.5), (50, 28), 'varie')
text(ax, 53, 33.5, 'Fermat : 10¹⁰ ≡ 1', 'varie', 's', ha='left')
box(ax, 2, 16, 10, 11, 'sujet', label='10')
for i in range(8):
    box(ax, 14 + 9 * i, 16, 8.4, 11, 'resultat')
brace(ax, 14, 85.4, 16, 'resultat', label='8 blocs ≡ 1')
text(ax, 44, 4, r'$10^{81}\equiv10\times1=10$ (mod 11)', 'resultat', 's')
save(fig, '53-141')
