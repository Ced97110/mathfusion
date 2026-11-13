import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
CL = {0: 'sujet', 1: 'varie', 2: 'resultat', 3: 'limite'}
fig, ax = canvas(80)
for y, a, b, s in [(60, 1, 5, r'$5-1=4$'), (22, -1, 3, r'$-1-3=-4$')]:
    f = numberline(ax, 10, 70, y, -1, 5, labels=True, arrow_right=False, every=2)
    for v in (a, b):
        disc(ax, f(v), y, 2.4, CL[v % 4], label=None)
    if y > 40:
        arrow(ax, (f(a), y + 3), (f(b), y + 3), 'fixe', curve=-0.35)
    else:
        arrow(ax, (f(b), y + 3), (f(a), y + 3), "fixe", curve=0.35)
    text(ax, 40, y + 16, s, 'encre', 'l')
text(ax, 40, 48, 'même couleur : orange', 'varie', 's')
text(ax, 40, 10, 'même couleur : rouge', 'limite', 's')
save(fig, '52-021')
