import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
rows = [(60, r'$[E:\mathbb{Q}]=4$', 'sujet'), (38, r'$|G|=4$', 'varie'), (16, r'$|\mathrm{Gal}|=4$', 'sujet')]
for y, lab, role in rows:
    text(ax, 2, y + 4, lab, role, 's', ha='left')
    for i in range(4):
        box(ax, 28 + i * 9, y, 8, 8, role)
text(ax, 34, 49, r'$\leq$', 'encre', 'l')
text(ax, 40, 49, "lemme d'Artin", 'fixe', 's', ha='left')
text(ax, 34, 27, r'$\leq$', 'encre', 'l')
text(ax, 40, 27, r'$G\subseteq\mathrm{Gal}$', 'fixe', 's', ha='left')
line(ax, [(66, 20), (72, 20), (72, 64), (66, 64)], 'resultat', lw=1.2)
text(ax, 80, 46, '=', 'resultat', 'l', weight='bold')
text(ax, 80, 38, 'Judson', 'resultat', 's')
text(ax, 44, 5, 'chaîne : 4 ≤ 4 ≤ 4 = 4', 'resultat', 's')
save(fig, '63-121')
