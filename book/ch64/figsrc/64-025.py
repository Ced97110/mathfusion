import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# haut : un produit devient deux produits simples
box(ax, 2, 50, 28, 12, 'sujet', label='3 × 4 × 5', size='m')
box(ax, 44, 57, 40, 9, 'resultat', label='3 × 4 = 12', size='s')
box(ax, 44, 44, 40, 9, 'resultat', label='12 × 5 = 60', size='s')
arrow(ax, (30.5, 58), (43.5, 61.5), 'resultat')
arrow(ax, (30.5, 54), (43.5, 48.5), 'resultat')
line(ax, [(2, 37), (86, 37)], 'fixe', dash=True)
# bas : un groupe devient trois quotients
box(ax, 2, 12, 34, 14, 'sujet', label=r'$S_4$ : 24, non abélien', size='s')
for i, lab in enumerate((r'ℤ/2 : 2', r'ℤ/3 : 3', r'$V$ : 4')):
    y = 27 - 11 * i
    box(ax, 50, y, 20, 8, 'resultat', label=lab, size='s')
    arrow(ax, (36.5, 19), (49.5, y + 4), 'resultat')
text(ax, 79, 19, 'abéliens', 'resultat', 's')
save(fig, '64-025')
