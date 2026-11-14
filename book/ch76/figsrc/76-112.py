import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
def fmt(v): return str(v).replace('-', '−').rjust(2, ' ')
def mat(cx, rows, role, det):
    for i, r in enumerate(rows):
        text(ax, cx, 34 - 9 * i, '  '.join(fmt(v) for v in r), role, 'm')
    for x, s in ((cx - 9, 1.5), (cx + 9, -1.5)):
        line(ax, [(x + s, 38), (x, 38), (x, 21), (x + s, 21)], role)
    text(ax, cx, 14, det, role, 's')
mat(13, [[2, 1], [-1, 1]], 'sujet', r'$\det A=3$')
text(ax, 29, 29.5, r'$\times$', 'encre', 'l')
mat(44, [[1, -1], [1, 1]], 'autre', r'$\det B=2$')
text(ax, 60, 29.5, r'$=$', 'encre', 'l')
mat(74, [[3, -1], [0, 2]], 'resultat', r'$\det AB=6$')
text(ax, 44, 5, r'$3\times2=6$', 'resultat', 'l', weight='bold')
save(fig, '76-112')
