import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
X0, YN = 14, 64
f = numberline(ax, X0, X0 + 60, YN, 1, 5, arrow_right=False)
for v in (2, 4):
    ax.plot([f(v)], [YN], 'o', color=COL['sujet'], ms=4.5, zorder=4)
    text(ax, f(v), YN + 5, 'note', 'sujet', 's')
ax.plot([f(3)], [YN], 'o', color=COL['varie'], ms=4.5, zorder=4)
text(ax, f(3), YN + 5, r'$m=3$', 'varie', 's')
Yb, u = 14, 7.0
line(ax, [(X0, Yb), (X0 + 60, Yb)], 'fixe')
for m, s in ((2, 4), (3, 2), (4, 4)):
    r = 'resultat' if s == 2 else 'sujet'
    box(ax, f(m) - 6, Yb, 12, u * s, r)
    text(ax, f(m), Yb + u * s + 3.5, str(s), r, 'm')
    text(ax, f(m), Yb - 3.5, r'$m=%d$' % m, 'fixe', 's')
text(ax, 86, 3, r'$2(m-3)^2+2$', 'resultat', 'm', ha='right')
text(ax, 2, 3, 'somme des carrés', 'fixe', 's', ha='left')
save(fig, '23-105')
