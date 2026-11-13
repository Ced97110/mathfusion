import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
for y, (a, b, c, d), prods, ok in ((54, (3, 4, 6, 8), ('3×8=24', '4×6=24'), True), (18, (3, 4, 5, 6), ('3×6=18', '4×5=20'), False)):
    role = 'resultat' if ok else 'limite'
    box(ax, 2, y - 15, 84, 31, role, r=2)
    text(ax, 14, y, rf'$\frac{{{a}}}{{{b}}}$', 'sujet', 'l'); text(ax, 38, y, rf'$\frac{{{c}}}{{{d}}}$', 'autre', 'l')
    arrow(ax, (19, y+5), (33, y-5), 'varie'); arrow(ax, (33, y+5), (19, y-5), 'varie')
    text(ax, 60, y+5, prods[0].replace('×', r'$\times$'), 'varie', 'm'); text(ax, 60, y-5, prods[1].replace('×', r'$\times$'), 'varie', 'm')
    text(ax, 76, y, 'égaux' if ok else 'différents', role, 's')
save(fig, '43-031')
