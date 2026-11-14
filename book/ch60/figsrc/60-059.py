import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# panneau ℤ
box(ax, 2, 45, 16, 11, 'fixe', label='−6', size='m')
box(ax, 26, 45, 36, 11, 'sujet', label='multiples de 6', size='s')
box(ax, 70, 45, 16, 11, 'resultat', label='6', size='m')
arrow(ax, (19, 50.5), (25, 50.5), 'fixe', both=True)
arrow(ax, (69, 50.5), (63, 50.5), 'resultat')
text(ax, 44, 40, 'sur ℤ : le générateur positif', 'resultat', 'm')
line(ax, [(4, 33), (84, 33)], 'fixe', lw=0.5, dash=True)
# panneau ℚ[λ]
box(ax, 2, 15, 20, 11, 'fixe', label='2λ − 2', size='s')
box(ax, 28, 15, 32, 11, 'sujet', label='multiples de λ − 1', size='s')
box(ax, 66, 15, 20, 11, 'resultat', label='λ − 1', size='s')
arrow(ax, (23, 20.5), (27, 20.5), 'fixe', both=True)
arrow(ax, (65, 20.5), (61, 20.5), 'resultat')
text(ax, 44, 8, 'ℚ[λ] : coefficient dominant 1', 'resultat', 'm')
save(fig, '60-059')
