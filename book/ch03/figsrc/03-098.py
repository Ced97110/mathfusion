import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *

fig, ax = canvas(80)

# Les cinq chiffres de 31 048
for x0, chiffre in ((20, '3'), (31, '1'), (42, '0'), (53, '4'), (64, '8')):
    box(ax, x0, 66, 11, 10, 'sujet', label=chiffre, size='l')

# Pour 4 : la coupe après 310 ; la part de gauche vaut 310 × 100
text(ax, 3, 52.5, 'pour 4', 'encre', 'm', ha='left', weight='bold')
box(ax, 20, 48, 33, 9, 'fixe', label=r'310 $\times$ 100', size='m')
box(ax, 53, 48, 22, 9, 'resultat', label='48 (2 chiffres)', size='s')
line(ax, [(53, 46), (53, 59)], 'varie', lw=1.4)
text(ax, 36.5, 42.5, r'100 = 4 $\times$ 25', 'varie', 'm')

# Pour 8 : la coupe après 31 ; la part de gauche vaut 31 × 1 000
text(ax, 3, 26.5, 'pour 8', 'encre', 'm', ha='left', weight='bold')
box(ax, 20, 22, 22, 9, 'fixe', label=r'31 $\times$ 1 000', size='s')
box(ax, 42, 22, 33, 9, 'resultat', label='048 (3 chiffres)', size='s')
line(ax, [(42, 20), (42, 33)], 'varie', lw=1.4)
text(ax, 30, 16.5, r'1 000 = 8 $\times$ 125', 'varie', 'm')

save(fig, '03-098')
