import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role="fixe", label=None, size="m", **k): return _box(ax, x, y, w, h, role, True, label, size, **k)
fig, ax = canvas(52)
f = numberline(ax, 8, 76, 24, 0, 180, step=30, arrow_right=False)
line(ax, [(f(0), 24), (f(90) - 1.5, 24)], 'resultat', lw=2.4); line(ax, [(f(90) + 1.5, 24), (f(180), 24)], 'resultat', lw=2.4)
disc(ax, f(90), 24, 1.5, 'limite', fill=True)
text(ax, f(45), 33, 'identité démontrée', 'resultat', 's'); text(ax, f(135), 33, 'identité démontrée', 'resultat', 's')
text(ax, f(90), 45, r'$\theta = 90^\circ$ : $\cos\theta = 0$', 'limite', 's')
text(ax, f(90), 40, r'$\tan\theta$ n’existe pas', 'limite', 's')
arrow(ax, (f(90), 38), (f(90), 27), 'limite')
text(ax, 44, 4, r'$\theta$ en degrés', 'fixe', 's')
save(fig, '31-122')
