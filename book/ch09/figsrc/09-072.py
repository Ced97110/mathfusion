import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
s = 3.4
for i in range(100):
    r_, c_ = divmod(i, 10)
    role = 'resultat' if i < 35 else 'fixe'
    ax.add_patch(Rectangle((4 + c_ * s, 11 + (9 - r_) * s), s, s, ec=COL['fixe'], fc=FILL[role], lw=0.2, zorder=2))
for r_ in range(10):
    for h in range(2):
        g = r_ * 2 + h
        rl = 'resultat' if g < 7 else 'fixe'
        ax.add_patch(Rectangle((4 + h * 5 * s, 11 + (9 - r_) * s), 5 * s, s, ec=COL[rl], fc='none', lw=0.9, zorder=3))
text(ax, 21, 50, '35 carreaux verts sur 100', 'resultat', 's')
text(ax, 21, 6, '7 paquets de 5 sur 20', 'resultat', 's')
for y, lab in [(37, '35 %'), (24, '0,35'), (11, r'$\frac{7}{20}$')]:
    box(ax, 52, y, 32, 12 if y == 11 else 10, 'resultat', label=lab, size='l')
text(ax, 68, 34.5, '=', 'encre', 'l')
text(ax, 68, 21.5 if False else 22, '=', 'encre', 'l')
save(fig, '09-072')
