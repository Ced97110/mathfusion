import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cw, ch, x, y = 11, 9, 33, 22
for i, row in enumerate([['2', '0'], ['0', '10']]):
    for j, v in enumerate(row):
        role = 'resultat' if i == j else 'fixe'
        box(ax, x + j * cw, y + (1 - i) * ch, cw, ch, role, r=0.4, label=v, size='m')
text(ax, 44, 58, '10 = 5 × 2 + 0', 'encre', 'm', weight='bold')
text(ax, 44, 51, '2 divise 10 : rien à changer', 'resultat', 's')
text(ax, 14, y + ch + 4.5, 'd₁ = 2', 'resultat', 's')
arrow(ax, (22, y + ch + 4.5), (x - 1, y + ch + 4.5), 'resultat', lw=1.0)
text(ax, 72, y + 4.5, 'd₂ = 10', 'resultat', 's')
arrow(ax, (63, y + 4.5), (x + 2 * cw + 1, y + 4.5), 'resultat', lw=1.0)
text(ax, 44, 8, 'forme normale : diag(2, 10)', 'resultat', 'm', weight='bold')
save(fig, '59-115')
