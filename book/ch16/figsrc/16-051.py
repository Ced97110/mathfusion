import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
def bal(cx, yb, l, r, role):
    poly(ax, [(cx - 3, yb - 12), (cx + 3, yb - 12), (cx, yb)], 'fixe')
    line(ax, [(cx - 15, yb), (cx + 15, yb)], 'fixe', lw=1.3)
    for s, wt in ((-1, l), (1, r)):
        line(ax, [(cx + 15 * s, yb), (cx + 15 * s, yb - 5)], 'fixe')
        box(ax, cx + 15 * s - 6, yb - 12, 12, 7, role, label=wt)
bal(44, 78, '6', '6', 'sujet'); text(ax, 44, 61, '6 et 6 : équilibre', 'sujet', 's')
bal(22, 36, '12', '12', 'resultat'); bal(66, 36, '3', '3', 'resultat')
text(ax, 22, 18, '12 et 12 : équilibre', 'resultat', 's'); text(ax, 66, 18, '3 et 3 : équilibre', 'resultat', 's')
arrow(ax, (36, 56), (25, 44), 'varie'); arrow(ax, (52, 56), (63, 44), 'varie')
text(ax, 26, 53, r'$\times$ 2', 'varie', 'm'); text(ax, 62, 53, r'$\div$ 2', 'varie', 'm')
text(ax, 44, 6, 'même nombre non nul des deux côtés', 'fixe', 's')
save(fig, '16-051')
