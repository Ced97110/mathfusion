import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'ω est envoyé sur une racine de f', 'encre', 's')
disc(ax, 12, 32, 7, role='sujet', label='ω')
ks = [(1, 'ω'), (2, 'ω²'), (3, 'ω³'), (4, 'ω⁴')]
for i, (k, t) in enumerate(ks):
    y = 48 - 14 * i
    box(ax, 50, y, 36, 9, role='varie', label=f'σ{"₁₂₃₄"[k - 1]} : ω ↦ {t}')
    arrow(ax, (19.2, 32 + (y + 4.5 - 32) * 0.1), (49.2, y + 4.5), 'varie')
text(ax, 26, 5, '4 possibilités : [E:ℚ] = 4,\npas d’autre', 'resultat', 's')
save(fig, '63-159')
