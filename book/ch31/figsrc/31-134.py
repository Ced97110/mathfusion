import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def lbox(ax, x, y, w, h, role, label=None, **k): return box(ax, x, y, w, h, role, label=label, **k)
fig, ax = canvas(48)
rows = (('0°', 1, 1), ('90°', 0, 0), ('180°', 1, 1), ('270°', 0, 2))
text(ax, 8, 28, r'$\cos^2 x$', 'sujet', 's'); text(ax, 8, 12, r'$1-\sin x$', 'autre', 's')
for i, (a, u, v) in enumerate(rows):
    x = 17 + i * 17.5; role = 'resultat' if u == v else 'limite'
    text(ax, x + 7.5, 41, a, 'encre', 'm', weight='bold')
    lbox(ax, x, 22, 15, 12, role, str(u)); lbox(ax, x, 6, 15, 12, role, str(v))
save(fig, '31-134')
