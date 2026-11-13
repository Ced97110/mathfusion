import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 22, 50, '1 × 3', 'resultat', 'l'); text(ax, 66, 50, '2 × 3', 'limite', 'l')
for c in range(3):
    disc(ax, 22 + (c - 1) * 6, 38, 2, 'resultat')
n = 0
for r in range(2):
    for c in range(3):
        disc(ax, 66 + (c - 1) * 6, 41 - 6 * r, 2, 'fixe' if n < 5 else 'limite'); n += 1
text(ax, 22, 28, '3 → reste 3', 'resultat', 'm'); text(ax, 66, 28, '5 + 1 → reste 1', 'limite', 'm')
text(ax, 22, 20, '3 inchangé', 'resultat', 'm'); text(ax, 66, 20, '1 ≠ 3 : change', 'limite', 'm')
text(ax, 44, 8, '1 est le neutre (mod 5)', 'resultat', 'l')
save(fig, '44-157')
