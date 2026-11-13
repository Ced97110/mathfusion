import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# trois listes de sacs pour faire la vente (5, 4)
text(ax, 44, 61, 'faire la vente (5, 4) avec…', 'encre', 'm')
cols = [(2, ['(1, 0)', '(2, 0)'], 'impossible', 'limite'),
        (31, ['(1, 0)', '(2, 0)', '(0, 1)'], 'plusieurs façons', 'limite'),
        (60, ['(1, 0)', '(0, 1)'], 'une seule façon', 'resultat')]
for x, sacs, verdict, role in cols:
    for k, s in enumerate(sacs):
        box(ax, x + 4, 46 - k * 11, 19, 8, 'sujet', label=s, size='s')
    box(ax, x, 6, 26, 9, role, label=verdict, size='s', weight='bold')
    arrow(ax, (x + 13, 46 - (len(sacs) - 1) * 11 - 1.5), (x + 13, 16.5), role, lw=0.9)
text(ax, 73, 2.6, r'$(e_1,\ e_2)$ : une base', 'resultat', 's', weight='bold')
save(fig, '58-010')
