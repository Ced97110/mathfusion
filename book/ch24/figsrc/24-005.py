import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def plane(ax, ox, oy, s, xm, ym, xl=(), yl=(), size='s'):
    arrow(ax, (ox, oy), (ox + xm * s + 3, oy), 'fixe', lw=0.9)
    arrow(ax, (ox, oy), (ox, oy + ym * s + 3), 'fixe', lw=0.9)
    for v in range(1, int(xm) + 1):
        ax.plot([ox + v * s] * 2, [oy - 1, oy + 1], color=COL['fixe'], lw=0.7, zorder=1.5)
        if v in xl: text(ax, ox + v * s, oy - 3.2, str(v), 'fixe', size)
    for v in range(1, int(ym) + 1):
        ax.plot([ox - 1, ox + 1], [oy + v * s] * 2, color=COL['fixe'], lw=0.7, zorder=1.5)
        if v in yl: text(ax, ox - 3, oy + v * s, str(v), 'fixe', size)
    return lambda x, y: (ox + x * s, oy + y * s)

def at(P, x, y, dx=0.0, dy=0.0):
    p = P(x, y); return (p[0] + dx, p[1] + dy)
fig, ax = canvas(58); s = 5.5; oy = 10
A = plane(ax, 7, oy, s, 5.4, 6.2); B = plane(ax, 52, oy, s, 5.4, 6.2)
text(ax, 25, 53, '1 équation : 1 choix libre', 'varie', 's'); text(ax, 66, 53, '2 équations : 1 seul couple', 'resultat', 's')
line(ax, [A(0, 5), A(5, 0)], 'sujet', lw=1.4)
text(ax, *A(1.2, 5.1), r'$D_1$', 'sujet', 's')
for x, y, lab in [(1, 4, '(1 ; 4)'), (2, 3, '(2 ; 3)'), (4.5, 0.5, '(4,5 ; 0,5)')]:
    disc(ax, *A(x, y), 1.3, 'varie'); text(ax, *at(A, x, y, 1.5, 2.8), lab, 'varie', 's', ha='left')
line(ax, [B(0, 5), B(5, 0)], 'sujet', lw=1.4); line(ax, [B(0.9, 6.2), B(4, 0)], 'varie', lw=1.4)
disc(ax, *B(3, 2), 1.6, 'resultat'); text(ax, *at(B, 3, 2, 2, 2.6), 'P (3 ; 2)', 'resultat', 's', ha='left')
text(ax, *B(4.7, 1.3), r'$D_1$', 'sujet', 's'); text(ax, *B(1.3, 6.2), r'$D_2$', 'varie', 's', ha='left')
save(fig, '24-005')
