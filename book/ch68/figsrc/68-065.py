import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
s, g, x0 = 2.6, 0.9, 28
text(ax, 44, 63, r'$\mathbb{F}_2^{\,n}$ : $2^{n}$ mots', 'sujet', 'l')
for r, n in enumerate([1, 2, 3, 4]):
    y = 46 - r * 11
    text(ax, 2, y + s / 2, f'$n={n}$ : {2 ** n} mots', 'encre', 'm', ha='left')
    for i in range(2 ** n):
        x = x0 + i * (s + g)
        role = 'sujet' if i < 2 ** (n - 1) else 'varie'
        poly(ax, [(x, y), (x + s, y), (x + s, y + s), (x, y + s)], role)
for x, role, lab in [(4, 'sujet', 'mots déjà comptés'), (46, 'varie', 'mots ajoutés')]:
    poly(ax, [(x, 3), (x + s, 3), (x + s, 3 + s), (x, 3 + s)], role)
    text(ax, x + s + 2, 3 + s / 2, lab, role, 's', ha='left')
save(fig, '68-065')
