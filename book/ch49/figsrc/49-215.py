import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
names = ['neutre', 'quart de tour', 'demi-tour', 'trois quarts']
ns = [16, 2, 4, 2]
text(ax, 44, 51, 'une ligne par élément', 'fixe', 's')
for r in range(4):
    y = 41 - r * 7.5
    text(ax, 3, y, names[r], 'encre', 's', ha='left')
    for k in range(ns[r]):
        box(ax, 27 + k * 3.2, y - 2.6, 3, 5.2, 'sujet', r=0.4, lw=0.5)
    text(ax, 82, y, str(ns[r]), 'sujet', 'm')
line(ax, [(27, 12), (86, 12)], 'fixe')
text(ax, 44, 6, r'$N$ = 16 + 2 + 4 + 2 = 24', 'resultat', 'm')
save(fig, '49-215')
