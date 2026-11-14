import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role, head=False, lw=0.9):
    n = 24
    pts = [pol(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw=lw)
fig, ax = canvas(70)
r = 14; cy = 38
cx = 26
disc(ax, cx, cy, r, 'fixe', fill=False); line(ax, [(cx - r - 2, cy), (cx + r + 2, cy)], 'fixe')
line(ax, [(cx, cy - r - 2), (cx, cy + r + 2)], 'fixe', dash=True)
for a in (40, 140):
    line(ax, [(cx, cy), pol(cx, cy, r, a)], 'autre'); disc(ax, *pol(cx, cy, r, a), 1.2, 'autre')
arc(ax, cx, cy, 7, 0, 140, 'varie', head=True)
text(ax, 40, 50, r'$\alpha$', 'autre', 's'); text(ax, 13.5, 49.5, r'$180^\circ-\alpha$', 'autre', 's', ha='right')
cx = 68
disc(ax, cx, cy, r, 'fixe', fill=False); line(ax, [(cx - r - 2, cy), (cx + r + 2, cy)], 'fixe')
line(ax, [(cx, cy - r - 2), (cx, cy + r + 2)], 'fixe', dash=True)
for a in (60, -60):
    line(ax, [(cx, cy), pol(cx, cy, r, a)], 'sujet'); disc(ax, *pol(cx, cy, r, a), 1.2, 'sujet')
arc(ax, cx, cy, 7, 0, -60, 'varie', head=True)
text(ax, 78, 52, r'$\alpha$', 'sujet', 's'); text(ax, 78.5, 23.5, r'$-\alpha$', 'sujet', 's')
text(ax, 26, 62, 'sinus', 'autre', 'l'); text(ax, 68, 62, 'cosinus', 'sujet', 'l')
text(ax, 26, 12, 'avec un demi-tour', 'autre', 's'); text(ax, 68, 12, 'sans demi-tour', 'sujet', 's')
save(fig, '32-063')
