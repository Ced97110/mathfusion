import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 11, 68, r"$G$", 'fixe', 'm'); text(ax, 48, 68, r"$G/\ker f$", 'sujet', 'm'); text(ax, 79, 68, r"$\mathrm{im}\,f$", 'resultat', 'm')
box(ax, 2, 12, 18, 50, 'fixe')
for k in range(12):
    disc(ax, 6 + 5 * (k % 3), 18 + 11 * (k // 3), 1.6, 'fixe')
for j in range(4):
    y = 14 + 13 * j
    box(ax, 38, y, 20, 10, 'sujet')
    for m in range(3):
        disc(ax, 43 + 5 * m, y + 5, 1.6, 'sujet')
    arrow(ax, (58, y + 5), (71, y + 5), 'resultat', both=True)
    disc(ax, 79, y + 5, 3.4, 'resultat')
arrow(ax, (20, 37), (38, 37), 'varie', lw=1.4)
text(ax, 29, 5, "1. regrouper", 'varie', 's'); text(ax, 67, 5, "2. comparer", 'resultat', 's')
save(fig, '48-072')
