import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
cols = [(2, [r'$x+4=6$', r'$x+0=2$', r'$x=2$'], ['opposé\n' + r'$4+(-4)=0$', 'neutre\n' + r'$x+0=x$']),
        (46, [r'$2x=6$', r'$1x=3$', r'$x=3$'], ['inverse\n' + r'$2\times\frac{1}{2}=1$', 'neutre\n' + r'$1x=x$'])]
ys = [58, 33, 8]
for x0, rows, labs in cols:
    cx = x0 + 11
    for i, (s, y) in enumerate(zip(rows, ys)):
        box(ax, x0, y, 22, 10, 'resultat' if i == 2 else 'sujet', label=s)
    for i, lab in enumerate(labs):
        y0 = ys[i]; y1 = ys[i + 1] + 10
        arrow(ax, (cx, y0 - 0.5), (cx, y1 + 0.5), 'varie')
        text(ax, x0 + 24, (y0 + y1) / 2, lab, 'varie', 's', ha='left', weight='bold')
save(fig, '12-131')
