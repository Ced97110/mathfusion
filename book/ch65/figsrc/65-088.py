import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
vals = [6, 35, 10, 21, 14, 15]
names = [r'$t_1 = 41$', r'$t_2 = 31$', r'$t_3 = 29$']
for p in range(3):
    xa = 4 + p * 28
    for q in range(2):
        box(ax, xa + q * 13, 36, 11, 10, 'sujet', label=str(vals[2 * p + q]), size='s')
    brace(ax, xa, xa + 24, 35, 'sujet', names[p], down=True)
brace(ax, 4, 84, 47, 'resultat', 'somme des 6 produits : 101', down=False)
arrow(ax, (44, 27), (44, 21), 'varie')
box(ax, 12, 7, 64, 13, 'resultat', label=r'$b_1 = 41 + 31 + 29 = 101$', size='m')
save(fig, '65-088')
