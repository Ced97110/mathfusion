import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 63, r'$C$ = 2 × $\pi$ × $r$', 'sujet', 'l')
data = [(1, '6,28', 14), (3, '18,84', 42), (5, '31,4', 70)]
for r, c, cx in data:
    rr = 1.8 * r
    cy = 38 + rr
    disc(ax, cx, cy, rr, 'sujet')
    line(ax, [(cx, cy), (cx + rr, cy)], 'varie', lw=1.1)
    text(ax, cx, 34, rf'$r$ = {r} cm', 'varie', 's')
    text(ax, cx, 29.5, rf'$C$ ≈ {c} cm', 'varie', 's')
    text(ax, cx, 20, f'{c} ÷ {r}', 'fixe', 's')
    text(ax, cx, 15.5, f'= 6,28', 'resultat', 'm', weight='bold')
    arrow(ax, (cx, 26.5), (cx, 22.5), 'fixe')
    text(ax, cx + 2.5, 24.5, r'$C$ ÷ $r$', 'fixe', 's', ha='left')
text(ax, 44, 6, r'2 × $\pi$ ≈ 6,28 (approché)', 'resultat', 's')
save(fig, '11-097')
