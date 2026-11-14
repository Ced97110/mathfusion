import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# x^3 - 6x^2 + 11x - 6 : coefficients 1, -6, 11, -6 ; roots 1, 2, 3
coefs = [1, -6, 11, -6]
e1, e2 = -coefs[1], coefs[2]
assert (e1, e2) == (6, 11) and e1 ** 2 - 2 * e2 == 14 == 1 + 4 + 9 and 6 + 11 * 0 == 6
heads = [r'$x^3$', r'$x^2$', r'$x$', '1']
neg = lambda n: str(n).replace('-', '−')
X0, ST, CW = 14, 17, 15
for j, (h, c) in enumerate(zip(heads, coefs)):
    text(ax, X0 + j * ST + CW / 2, 79, h, 'fixe', 'm')
    box(ax, X0 + j * ST, 68, CW, 9, 'sujet', label=neg(c), size='m')
# e1 from the x^2 coefficient, e2 from the x coefficient
arrow(ax, (X0 + ST + CW / 2, 68), (22, 59.5), 'varie')
arrow(ax, (X0 + 2 * ST + CW / 2, 68), (66, 59.5), 'varie')
box(ax, 3, 50, 38, 9, 'varie', label=r'$e_1=6$ : somme', size='s')
box(ax, 47, 50, 38, 9, 'varie', label=r'$e_2=11$ : produits 2 à 2', size='s')
arrow(ax, (22, 50), (36, 43.5), 'varie')
arrow(ax, (66, 50), (52, 43.5), 'varie')
box(ax, 4, 34, 80, 9, 'resultat', label=r'$e_1^2-2e_2=36-22=14$', size='m')
arrow(ax, (44, 33.5), (44, 26.5), 'resultat', both=True)
box(ax, 4, 17, 80, 9, 'fixe', label=r'contrôle : $1^2+2^2+3^2=14$', size='m')
text(ax, 44, 9, 'racines 1, 2, 3 : trouvées seulement pour contrôler', 'fixe', 's')
save(fig, '55-130')
