import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
for x0, title, a, b, lst, cap in [(3, 'le résultat dépasse N', '72', '12', '(0, 0, 2)', 'modules 3, 4 et 5'),
                                  (47, 'pas premiers entre eux', '0', '12', '(0, 0)', 'modules 4 et 6')]:
    text(ax, x0 + 19, 56, title, 'limite', 's')
    box(ax, x0 + 2, 36, 16, 9, 'sujet', label=a)
    box(ax, x0 + 22, 36, 16, 9, 'autre', label=b)
    arrow(ax, (x0 + 10, 36), (x0 + 14, 26.5), 'fixe'); arrow(ax, (x0 + 30, 36), (x0 + 26, 26.5), 'fixe')
    box(ax, x0 + 5, 17, 30, 9, 'limite', label=lst)
    text(ax, x0 + 20, 12, 'mêmes restes', 'limite', 's')
    text(ax, x0 + 20, 6, cap, 'fixe', 's')
save(fig, '52-263')
