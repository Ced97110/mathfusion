import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
for y, k, n in [(36, 3, 3), (12, 12, 4)]:
    text(ax, 12, y + 9, f'$|A_{n}|$', 'sujet', 'm', ha='left')
    for i in range(k): box(ax, 14 + i * 4.8, y - 2.5, 4, 5, 'sujet', lw=0.5, r=0.3)
    e = 14 + k * 4.8
    for xb in (11.5, e + 0.3): line(ax, [(xb, y - 4.5), (xb, y + 4.5)], 'sujet', lw=1.5)
    text(ax, e + 4, y, f'= {k}', 'resultat', 'm', ha='left')
text(ax, 44, 48, 'les barres comptent les éléments', 'encre', 's')
save(fig, '46-234')
