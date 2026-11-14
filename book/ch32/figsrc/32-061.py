import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role, head=False, lw=0.9):
    n = 24
    pts = [pol(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw=lw)

fig, ax = canvas(70)
for cx, k, s, a in [(22, 0.5, 'cos θ = 0,5 : α = 60°', 60), (66, 0.1, 'cos θ = 0,1 : α = 84,26°', 84.26)]:
    cy, r = 38, 15
    disc(ax, cx, cy, r, 'fixe', fill=False)
    line(ax, [(cx - r - 2, cy), (cx + r + 2, cy)], 'fixe')
    xk = cx + k * r; h = math.sqrt(1 - k * k) * r
    line(ax, [(xk, cy - h), (xk, cy + h)], 'fixe', dash=True)
    line(ax, [(cx, cy), (xk, cy + h)], 'sujet'); line(ax, [(cx, cy), (xk, cy - h)], 'varie')
    disc(ax, xk, cy + h, 1.2, 'sujet'); disc(ax, xk, cy - h, 1.2, 'varie')
    text(ax, xk + 3, cy + h + 1, r'$\alpha$', 'sujet', 's'); text(ax, xk + 3.5, cy - h - 1, r'$-\alpha$', 'varie', 's')
    text(ax, cx, 62, s, 'encre', 's')
box(ax, 2, 5, 40, 9, 'sujet', label=r'$\theta = \alpha + 360^\circ n$', size='s')
box(ax, 46, 5, 40, 9, 'varie', label=r'$\theta = -\alpha + 360^\circ n$', size='s')
save(fig, '32-061')
