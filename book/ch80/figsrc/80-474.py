import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
text(ax, 44, 64, 'trois lettres : 8 positions', 'encre', 'm', weight='bold')
for i in range(8):
    x = 3.5 + i * 10.5
    box(ax, x, 42, 8.5, 12, 'sujet', label='2')
    disc(ax, x + 4.25, 37, 1.2, 'fixe'); disc(ax, x + 4.25, 33.5, 1.2, 'resultat')
brace(ax, 3.5, 87.0 - 5.0, 51, 'sujet', label='8 positions', down=False, depth=1.4) if False else None
text(ax, 44, 27.5, 'chaque position : éteinte ou allumée', 'encre', 's')
text(ax, 44, 21, r'$2\times2\times\cdots\times2$ (8 fois)', 'encre', 's')
box(ax, 20, 4, 48, 11, 'resultat', label=r'$2^8=256$ tables', weight='bold')
save(fig, '80-474')
