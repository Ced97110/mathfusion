import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def panel(x0, x1, y, title, eq, pts, role):
    box(ax, x0 - 1, y - 18, x1 - x0 + 2, 52, role, fill=False, lw=0.7)
    text(ax, (x0 + x1) / 2, y + 30, title, role, 's')
    f = numberline(ax, x0 + 3, x1 - 3, y + 12, -2, 2, labels=False, arrow_right=False)
    for v, r, t in pts:
        disc(ax, f(v), y + 12, 2.0, r)
        text(ax, f(v), y + 18, t, r, 's')
    text(ax, (x0 + x1) / 2, y - 6, eq, 'encre', 's')
panel(2, 43, 20, r'$\det b=-1$', r'$(\det h)^2=1$', [(-1, 'resultat', '−1'), (1, 'resultat', '1')], 'resultat')
panel(45, 86, 20, r'$\det b=0$', r'$(\det h)^2\times 0=0$', [(-1, 'resultat', '−1'), (1, 'resultat', '1'), (2, 'limite', '2')], 'limite')
text(ax, 22, 58, 'seulement −1 et 1', 'resultat', 's')
text(ax, 66, 58, '2 convient aussi', 'limite', 's')
save(fig, '72-060')
