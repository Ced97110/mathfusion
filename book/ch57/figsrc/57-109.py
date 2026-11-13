import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, '$x$ = (2 ; 1), $a$ = 3, $b$ = 2', 'encre', 'm')
text(ax, 32.5, 50, 'd’abord $a$', 'sujet', 's')
text(ax, 52, 50, 'puis $b$', 'varie', 's')
text(ax, 76.5, 50, '$ab$ = 6\nd’un coup', 'autre', 's')
text(ax, 12, 34, 'action\n$x$ ↦ $a$·$x$', 'resultat', 's')
text(ax, 12, 12, 'action\n$x$ ↦ 2$a$·$x$', 'limite', 's')
def eq(x, y, role, neq=False):
    line(ax, [(x - 2.5, y + 1), (x + 2.5, y + 1)], role, lw=1.2)
    line(ax, [(x - 2.5, y - 1), (x + 2.5, y - 1)], role, lw=1.2)
    if neq: line(ax, [(x - 1.4, y - 2.4), (x + 1.4, y + 2.4)], role, lw=1.2)
rows = [(28, 'resultat', ('(6 ; 3)', '(12 ; 6)', '(12 ; 6)'), False),
        (6, 'limite', ('(12 ; 6)', '(48 ; 24)', '(24 ; 12)'), True)]
for y, role, vals, neq in rows:
    box(ax, 24, y, 17, 12, 'sujet', label=vals[0], size='s')
    box(ax, 43, y, 18, 12, role, label=vals[1], size='s')
    box(ax, 67, y, 19, 12, role, label=vals[2], size='s')
    eq(64, y + 6, role, neq)
save(fig, '57-109')
