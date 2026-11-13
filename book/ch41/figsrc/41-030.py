import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# 41-030 : la lettre b = composante en y du vent ≈ 86,60 ; elle vient après a dans ⟨a, b⟩
fig, ax = canvas(76)
s = 0.5
O = (30, 10)
V = (O[0] + 50 * s, O[1] + 86.6 * s)
Q = (O[0], V[1])
arrow(ax, (O[0], O[1]), (O[0], O[1] + 52), 'fixe', lw=0.7)
line(ax, [V, Q], 'fixe', dash=True)
arrow(ax, O, V, 'varie', lw=1.2)
arrow(ax, O, Q, 'sujet', lw=2.0)
text(ax, O[0] - 3, O[1] + 24, r'$b$ ≈ 86,6', 'sujet', 'l', ha='right', weight='bold')
text(ax, O[0] + 2, O[1] + 51, 'axe $y$ (nord)', 'fixe', 's', ha='left')
text(ax, (O[0] + V[0]) / 2 + 3, (O[1] + V[1]) / 2 - 3, '100', 'varie', 'm', ha='left')
text(ax, (Q[0] + V[0]) / 2, Q[1] + 3.5, '50', 'fixe', 'm')
# écriture ⟨a, b⟩ : b est le second nombre
yb = 30
text(ax, 62, yb + 12, 'écriture :', 'fixe', 's')
text(ax, 54, yb, r'$\langle$', 'encre', 'xl')
box(ax, 57, yb - 4, 7, 8, 'fixe', label=r'$a$')
text(ax, 66, yb - 1, ',', 'encre', 'l')
box(ax, 68.5, yb - 4, 7, 8, 'sujet', label=r'$b$')
text(ax, 79, yb, r'$\rangle$', 'encre', 'xl')
save(fig, '41-030')
