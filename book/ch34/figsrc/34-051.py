import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
u = 4.5; x0 = 12; a = 7.62 * u; b = 5.38 * u
box(ax, x0, 14, a, 9, 'fixe', label='QH ≈ 7,62', size='s')
box(ax, x0 + a, 14, b, 9, 'resultat', label='HP ≈ 5,38', size='s')
brace(ax, x0, x0 + a + b, 26, 'sujet', label='QP = r = 13', down=False)
text(ax, x0, 10, 'Q', 'encre', 's'); text(ax, x0 + a, 10, 'H', 'encre', 's'); text(ax, x0 + a + b, 10, 'P', 'encre', 's')
text(ax, x0 + a / 2, 5, r'$p\cos(A+B)$', 'fixe', 's')
text(ax, x0 + a + b / 2 + 10, 5, r'$r - p\cos(A+B)$', 'resultat', 's')
save(fig, '34-051')
