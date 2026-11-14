import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
ya, yb = 44, 18

def row(y, root, role, title):
    f = numberline(ax, 8, 74, y, -3, 3, 1, labels=False, role='fixe')
    text(ax, 4, y + 10, title, role, 'm', ha='left')
    for v in (-root, root):
        disc(ax, f(v), y, 2.2, role)
        text(ax, f(v), y - 6, f'{v:d}'.replace('-', '−'), role, 'm')

row(ya, 2, 'autre', r"$x^2=4$ : racines de 4")
row(yb, 1, 'sujet', r"$x^2=1$ : racines de l'unité")
text(ax, 44, 3, 'seul le second membre change', 'encre', 'm')
save(fig, '64-145')
