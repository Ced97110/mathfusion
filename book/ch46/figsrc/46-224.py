import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def cyc(ax, cx, cy, r, nums, role, rad=3.0, hl=(), lab=True):
    n = len(nums)
    start = {1: 90, 2: 180, 3: 90, 4: 135}.get(n, 90)
    pts = [(cx + r * math.cos(math.radians(start - 360 * i / n)), cy + r * math.sin(math.radians(start - 360 * i / n))) for i in range(n)]
    if n >= 2:
        for i in range(n):
            p, q = pts[i], pts[(i + 1) % n]
            d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
            arrow(ax, (p[0] + ux * (rad + 0.3), p[1] + uy * (rad + 0.3)), (q[0] - ux * (rad + 0.3), q[1] - uy * (rad + 0.3)), role, lw=0.8, curve=0.5 if n == 2 else 0.0)
    for i, (p, v) in enumerate(zip(pts, nums)):
        disc(ax, p[0], p[1], rad, 'varie' if i in hl else role, label=str(v) if lab else None, size='s')
    return pts

def chip(ax, x, y, s, role='sujet', w=14, h=8, dash=False, fill=True):
    box(ax, x, y, w, h, role, fill=fill, label=s, size='m', dash=dash)

fig, ax = canvas(66)
text(ax, 23, 58, 'paire', 'resultat', 'l', weight='bold'); text(ax, 23, 50, r'$sg(\sigma) = +1$', 'resultat', 'm')
text(ax, 65, 58, 'impaire', 'autre', 'l', weight='bold'); text(ax, 65, 50, r'$sg(\sigma) = -1$', 'autre', 'm')
chip(ax, 4, 32, 'identité', 'resultat', w=38, h=9); chip(ax, 4, 16, 'cycle de longueur 3', 'resultat', w=38, h=9)
chip(ax, 46, 32, 'un échange', 'autre', w=38, h=9); chip(ax, 46, 16, 'cycle de longueur 4', 'autre', w=38, h=9)
save(fig, '46-224')
