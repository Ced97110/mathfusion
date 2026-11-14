import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role, head=False, lw=0.9):
    n = 24
    pts = [pol(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw=lw)
fig, ax = canvas(76)
cx, cy, r = 30, 36, 22
disc(ax, cx, cy, r, 'fixe', fill=False)
line(ax, [(6, cy), (54, cy)], 'fixe'); line(ax, [(cx, 10), (cx, 62)], 'fixe')
xk = cx + 0.5 * r; h = math.sqrt(3) / 2 * r
line(ax, [(xk, 10), (xk, 62)], 'varie', lw=1.2)
line(ax, [(cx, cy), (xk, cy + h)], 'sujet'); line(ax, [(cx, cy), (xk, cy - h)], 'resultat')
arc(ax, cx, cy, 6, 0, 60, 'sujet'); arc(ax, cx, cy, 6, -60, 0, 'resultat')
disc(ax, xk, cy + h, 1.3, 'sujet'); disc(ax, xk, cy - h, 1.3, 'resultat')
text(ax, 27.5, 33.2, '$O$', 'fixe', 's')
text(ax, 44, cy + h + 1.5, '$P$', 'sujet', 'm'); text(ax, 44, cy - h - 1.5, "$P'$", 'resultat', 'm')
text(ax, 37.6, 40.6, r'$\theta$', 'sujet', 's'); text(ax, 37.8, 31.4, r'$-\theta$', 'resultat', 's')
text(ax, xk, 66, '$x$ = 0,5', 'varie', 's')
box(ax, 58, 46, 26, 9, 'sujet', label='P : 60°')
box(ax, 58, 22, 26, 9, 'resultat', label='P′ : −60°')
save(fig, '32-056')
