import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
u = 2.8; x0 = 8
def bar(y, n, role, start=0):
    box(ax, x0 + start * u, y, n * u, 6, role, r=0.2)
    for i in range(1, n): line(ax, [(x0 + (start + i) * u, y), (x0 + (start + i) * u, y + 6)], role, lw=0.3)
bar(28, 25, 'sujet'); bar(28, 2, 'limite', 25); bar(12, 25, 'autre')
text(ax, x0, 38, r'$x^2$+10$x$+16 = 27', 'sujet', 'm', ha='left', weight='bold')
text(ax, x0, 22, r'$(x+4)^2$ = 25', 'autre', 'm', ha='left', weight='bold')
text(ax, 78, 22, 'écart : 2', 'limite', 's')
text(ax, 44, 44, r'$x$ = 1', 'encre', 's')
text(ax, 44, 5, r'milieu : 2 × $x$ × 4 = 8$x$, pas 10$x$', 'limite', 's')
save(fig, '18-062')
