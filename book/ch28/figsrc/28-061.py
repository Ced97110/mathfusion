import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(c, r, a): return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role, lw=1.0, head=True):
    n = max(8, int(abs(a1 - a0)/3)); pts = [pt(c, r, a0 + (a1 - a0)*i/n) for i in range(n + 1)]
    line(ax, pts, role, lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw)
def axes(ax, c, hx, hy, role='fixe'):
    arrow(ax, (c[0]-hx, c[1]), (c[0]+hx, c[1]), role, 0.7); arrow(ax, (c[0], c[1]-hy), (c[0], c[1]+hy), role, 0.7)
def dot(ax, p, role, r=0.9): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))
fig, ax = canvas(54)
O = (62, 10); s = 3
arrow(ax, (36, O[1]), (74, O[1]), 'fixe', 0.7); arrow(ax, (O[0], O[1] - 1), (O[0], O[1] + 38), 'fixe', 0.7)
d = (-3/5, 4/5); line(ax, [O, (O[0] + 40*d[0]*0.9, O[1] + 40*d[1]*0.9)], 'fixe', 1.0)
data = [((-6, 8), 'sujet', '8 ÷ 10 = 0,8', 40), ((-3, 4), 'autre', '4 ÷ 5 = 0,8', 31), ((-1.5, 2), 'varie', '2 ÷ 2,5 = 0,8', 22)]
for (x, y), r, lab, ty in data:
    p = (O[0] + x*s, O[1] + y*s); dot(ax, p, r, 1.1)
    line(ax, [p, (p[0], O[1])], r, 0.9, dash=True); text(ax, p[0] - 2.5, (p[1] + O[1])/2, f'{y:g}'.replace('.', ','), r, 's')
    text(ax, 20, ty, lab, r, 'm')
text(ax, 20, 49, r'$\sin\theta = y \div r$', 'encre', 'm'); text(ax, 20, 12, 'toujours 0,8', 'resultat', 'm')
text(ax, 47, 50, 'même demi-droite', 'fixe', 's')
save(fig, '28-061')
