import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(42)
x0, y, s = 6.5, 20, 5
for i in range(15):
    box(ax, x0 + i * s, y, s - 0.5, s - 0.5, 'fixe' if i < 8 else 'resultat', r=0.3, lw=0.6)
text(ax, 44, y + 13, '3 × 5 = 15 cases', 'sujet', 'l')
brace(ax, x0, x0 + 8 * s - 0.5, y - 0.5, 'fixe', label='1 tour de 8')
brace(ax, x0 + 8 * s, x0 + 15 * s - 0.5, y - 0.5, 'resultat', label='reste 7')
text(ax, 44, y - 12, '15 ÷ 8 : quotient 1, reste 7', 'encre', 'm')
save(fig, '44-145')
