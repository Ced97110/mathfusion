import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
def row(yb, name, a, b, res, wa, wb):
    gap = 10
    x0 = (W - (wa + gap + wb)) / 2
    xa, xb = x0, x0 + wa + gap
    text(ax, 44, yb + 36, name, 'fixe', 's', weight='bold')
    box(ax, xa, yb + 20, wa, 10, 'sujet', label=a)
    box(ax, xb, yb + 20, wb, 10, 'autre', label=b)
    text(ax, xa + wa + gap / 2, yb + 25, r'$=$', 'encre', 'l')
    for x, w in ((xa, wa), (xb, wb)):
        cx = x + w / 2
        arrow(ax, (cx, yb + 19.2), (cx, yb + 11.2), 'resultat')
        box(ax, cx - 7, yb, 14, 10, 'resultat', label=res, weight='bold')
    text(ax, xa + wa + gap / 2, yb + 5, r'$=$', 'resultat', 'l')
row(46, 'ordre changé', r'$3 + 11$', r'$11 + 3$', '14', 30, 30)
row(2, 'distributivité', r'$4\times(5+2)$', r'$4\times5+4\times2$', '28', 32, 36)
save(fig, '12-007')
