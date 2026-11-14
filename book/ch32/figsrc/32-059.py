import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role, head=False, lw=0.9):
    n = 24
    pts = [pol(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw=lw)
fig, ax = canvas(72)
cx, cy, r = 28, 34, 22
disc(ax, cx, cy, r, 'fixe', fill=False)
line(ax, [(5, cy), (52, cy)], 'fixe')
xk = cx + 0.5 * r; h = math.sqrt(3) / 2 * r
line(ax, [(xk, cy - h), (xk, cy + h)], 'fixe', dash=True)
line(ax, [(cx, cy), (xk, cy + h)], 'sujet'); line(ax, [(cx, cy), (xk, cy - h)], 'varie')
arc(ax, cx, cy, 12, 0, 60, 'sujet', head=True); arc(ax, cx, cy, 12, 0, -60, 'varie', head=True)
disc(ax, xk, cy + h, 1.3, 'sujet'); disc(ax, xk, cy - h, 1.3, 'varie')
text(ax, 25.3, 31.3, '$O$', 'fixe', 's')
text(ax, xk + 2.5, cy + h + 2, '$P$', 'sujet', 'm'); text(ax, xk + 2.5, cy - h - 2, "$P'$", 'varie', 'm')
text(ax, 42.5, 43, r'$\theta$', 'sujet', 's'); text(ax, 43, 25, r'$-\theta$', 'varie', 's')
box(ax, 56, 48, 30, 9, 'sujet', label=r'vers le haut : $\theta$', size='s')
box(ax, 56, 28, 30, 9, 'varie', label=r'vers le bas : $-\theta$', size='s')
box(ax, 56, 8, 30, 9, 'fixe', label='bas = sens négatif', size='s')
save(fig, '32-059')
