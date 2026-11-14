import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(52)
x0 = 6; s = 76 / 44; xb = x0 + 41 * s; xe = x0 + 76
box(ax, x0, 24, 41 * s, 10, 'sujet', label="l'an dernier : 41 €")
box(ax, xb, 24, 3 * s, 10, 'varie', label='3')
brace(ax, x0, xe, 36, 'resultat', label='44 € cette année', down=False)
arrow(ax, (xe - 1.5, 20), (xb + 1.5, 20), 'varie')
text(ax, 74, 15, 'retirer 3', 'varie', 's')
text(ax, 44, 5, 'vérification : 41 + 3 = 44', 'resultat', 's')
save(fig, '16-001')
