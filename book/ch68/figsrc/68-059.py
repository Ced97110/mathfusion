import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cw, x0 = 9, 26
for y, w, role, nom in [(34, '000', 'sujet', 'mot 1'), (10, '111', 'autre', 'mot 2')]:
    for i, b in enumerate(w):
        box(ax, x0 + i * (cw + 1), y, cw, 9, role, label=b, size='l')
    text(ax, 12, y + 4.5, nom, role, 'm')
for i in range(3):
    cx = x0 + i * (cw + 1) + cw / 2
    arrow(ax, (cx, 33), (cx, 20), 'varie', both=True)
text(ax, 69, 33, '3 positions\ndiffèrent', 'varie', 'm')
text(ax, 69, 17, r'$d=3$', 'resultat', 'l')
save(fig, '68-059')
