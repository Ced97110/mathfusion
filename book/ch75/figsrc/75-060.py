import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def grp(x, w, cols, rows, lab):
    box(ax, x, 14, w, 28, 'sujet', fill=False)
    for r in range(rows):
        for c in range(cols):
            disc(ax, x + 4.5 + c * 4.8, 38 - r * 4.8 if rows > 2 else 31 - r * 4.8, 1.8, 'sujet')
    text(ax, x + w / 2, 7, lab, 'resultat', 'm')
grp(4, 20, 3, 2, r'$|G|=6$')
grp(36, 48, 6, 4, r'$|G|=24$')
text(ax, 44, 51, 'nombre de points du groupe', 'encre', 's')
save(fig, '75-060')
