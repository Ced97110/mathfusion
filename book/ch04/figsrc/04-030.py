import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(88)
# partie haute : 3 × 4 (3 rangées de 4) et 4 × 3 (4 rangées de 3), cellules de 4 mm
for i in range(4):
    for j in range(3):
        box(ax, 14 + 4*i, 70 + 4*j, 4, 4, 'autre', r=0.1)
for i in range(3):
    for j in range(4):
        box(ax, 50 + 4*i, 68 + 4*j, 4, 4, 'autre', r=0.1)
arrow(ax, (31, 76), (49, 76), 'varie', both=True)
text(ax, 44, 62, '3 × 4 = 4 × 3 = 12', 'autre', 'm')
line(ax, [(4, 56), (84, 56)], 'fixe')
# bas-haut : 2³ (trois facteurs 2)
for x in [4, 13, 22]:
    box(ax, x, 40, 8, 7, 'sujet', label='2')
brace(ax, 4, 30, 38, 'varie', label='3 facteurs 2', size='s')
text(ax, 42, 43.5, r'$2^{3} = 8$', 'resultat', 'l')
# bas-bas : 3² (deux facteurs 3)
for x in [4, 13]:
    box(ax, x, 18, 8, 7, 'sujet', label='3')
brace(ax, 4, 21, 16, 'varie', label='2 facteurs 3', size='s')
text(ax, 42, 21.5, r'$3^{2} = 9$', 'resultat', 'l')
# échange de 2 et 3 : interdit
arrow(ax, (35, 40.5), (35, 24.5), 'varie', both=True, curve=0.3)
text(ax, 42, 32.5, '≠', 'limite', 'l')
text(ax, 67, 46, 'base : nombre multiplié', 'sujet', 's')
text(ax, 67, 40, 'exposant : il compte', 'varie', 's')
save(fig, '04-030')
