import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# 41-038 : ‖v‖ = √(a² + b²) : trois triangles à la même échelle (2,2 mm par unité) ; le signe de a ne change pas la norme
fig, ax = canvas(74)
s = 2.2
text(ax, 44, 67, r'$\|v\| = \sqrt{a^2 + b^2}$', 'sujet', 'l', weight='bold')
cases = [  # (centre x, a, b, titre, calcul)
    (14, 3, 4, '⟨3 ; 4⟩', '√(9 + 16) = 5'),
    (46, -3, 4, '⟨−3 ; 4⟩', '√(9 + 16) = 5'),
    (72, 5, 12, '⟨5 ; 12⟩', '√(25 + 144) = 13'),
]
yb = 20
for cx, a, b, tit, calc in cases:
    O = (cx - a * s / 2, yb)
    V = (O[0] + a * s, O[1] + b * s)
    P = (V[0], O[1])
    line(ax, [O, P], 'fixe', lw=1.2); line(ax, [P, V], 'fixe', lw=1.2)
    arrow(ax, O, V, 'resultat', lw=1.6)
    text(ax, (O[0] + P[0]) / 2, yb - 3.5, f'{a}'.replace('-', '−'), 'fixe', 's')
    off = 2.0 if a > 0 else -2.0
    text(ax, P[0] + off, (P[1] + V[1]) / 2, f'{b}', 'fixe', 's', ha='left' if a > 0 else 'right')
    text(ax, cx, 56, tit, 'encre', 's')
    text(ax, cx, 9, calc, 'resultat', 's')
save(fig, '41-038')
