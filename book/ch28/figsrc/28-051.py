import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(c, r, a): return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role, lw=1.0, head=True):
    n = max(8, int(abs(a1 - a0)/3)); pts = [pt(c, r, a0 + (a1 - a0)*i/n) for i in range(n + 1)]
    line(ax, pts, role, lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw)
def axes(ax, c, hx, hy, role='fixe'):
    arrow(ax, (c[0]-hx, c[1]), (c[0]+hx, c[1]), role, 0.7); arrow(ax, (c[0], c[1]-hy), (c[0], c[1]+hy), role, 0.7)
def dot(ax, p, role, r=0.9): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))
fig, ax = canvas(62)
c = (46, 30); R = 18
disc(ax, *c, R, 'fixe', fill=False); axes(ax, c, R + 5, R + 5)
P = pt(c, R, 130); d = (P[0] - c[0], P[1] - c[1])
line(ax, [(c[0] - 0.8*d[0], c[1] - 0.8*d[1]), (c[0] + 1.4*d[0], c[1] + 1.4*d[1])], 'sujet', 1.3)
H = (P[0], c[1]); arrow(ax, c, H, 'autre', 1.2); arrow(ax, H, P, 'varie', 1.2)
dot(ax, P, 'sujet'); text(ax, P[0] + 2.5, P[1] + 2.5, r'$P$', 'sujet', 's'); text(ax, c[0] + 2, c[1] - 2.5, r'$O$', 'encre', 's')
text(ax, (c[0] + H[0])/2, c[1] - 3, 'avancée', 'autre', 's'); text(ax, H[0] - 8, (c[1] + P[1])/2, 'montée', 'varie', 's')
text(ax, 44, 8.5, r'$\tan\theta = $ montée $\div$ avancée', 'resultat', 'm')
text(ax, 44, 3.8, 'à 130° : environ −1,19', 'resultat', 's')
save(fig, '28-051')
