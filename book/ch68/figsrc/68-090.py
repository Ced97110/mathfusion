import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 39, 75, 'détectées', 'sujet', 'm')
text(ax, 74, 75, 'corrigées', 'resultat', 'm')
for i, d in enumerate([1, 2, 3, 4, 5, 7]):
    y = 64 - i * 11
    t = (d - 1) // 2
    text(ax, 3, y, rf'$d={d}$', 'encre', 'm', ha='left')
    for k in range(d - 1):
        disc(ax, 28 + 6 * k, y, 2.2, 'sujet')
    for k in range(t):
        disc(ax, 68 + 6 * k, y, 2.2, 'resultat')
    if d - 1 == 0: text(ax, 28, y, '0', 'sujet', 'm')
    if t == 0: text(ax, 68, y, '0', 'resultat', 'm')
save(fig, '68-090')
