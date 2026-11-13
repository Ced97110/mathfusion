import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 3.8; L = 3 ** 0.5 * u; x0 = 4.5
box(ax, x0, 38, L, L, 'fixe')
text(ax, x0 + L + 3, 43.5, 'carré d\'aire 3', 'fixe', 's', ha='left')
text(ax, x0 + L + 3, 40, r'côté $\sqrt{3}$', 'fixe', 's', ha='left')
for i in range(12):
    box(ax, x0 + i * L, 20, L, 8, 'sujet' if i < 4 else 'autre')
brace(ax, x0, x0 + 4 * L, 29, 'sujet', r'$4\sqrt{3}$', down=False)
brace(ax, x0 + 4 * L, x0 + 12 * L, 29, 'autre', r'$8\sqrt{3}$', down=False)
brace(ax, x0, x0 + 12 * L, 19, 'resultat', r'$12\sqrt{3}$', down=True)
save(fig, '22-099')
