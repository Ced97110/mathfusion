import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
vals = ['3', '5', '17', '257', '65 537']
for i, v in enumerate(vals):
    box(ax, 3 + i * 17, 52, 15, 14, 'sujet', label=rf'$F_{i}$' + '\n' + v, size='s')
brace(ax, 3, 85, 51, 'sujet', label='cinq premiers de Fermat connus, pas d’autre')
text(ax, 44, 33, 'avec 3, 5 et 17 : chacun au plus une fois', 'resultat', 's')
prods = [r'$3\times 5=15$', r'$3\times 17=51$', r'$5\times 17=85$', r'$3\times 5\times 17=255$']
box(ax, 2, 20, 27, 8, 'resultat', label=prods[0], size='s')
box(ax, 31, 20, 27, 8, 'resultat', label=prods[1], size='s')
box(ax, 60, 20, 26, 8, 'resultat', label=prods[2], size='s')
box(ax, 20, 7, 48, 8, 'resultat', label=prods[3], size='s')
save(fig, '66-070')
