import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def E(ax, p, q, r=3.4, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def N(ax, x, y, s, role='sujet', r=3.4, size='m'):
    disc(ax, x, y, r, role, label=s, size=size)

fig, ax = canvas(72)
text(ax, 44, 64, r'$a\vee b$ : plus petit majorant', 'encre', 'm')
def bx(cx, y, w, s, role, size='m'): box(ax, cx - w/2, y, w, 8, role, label=s, size=size)
def panel(cx, lo, w, top, wt, s1, s2, st, title, size='m'):
    for dx in (-lo, lo): line(ax, [(cx + dx, 30), (cx, 48)])
    bx(cx - lo, 22, w, s1, 'sujet', size); bx(cx + lo, 22, w, s2, 'sujet', size); bx(cx, 48, wt, st, 'resultat', size)
    text(ax, cx, 12, title, 'fixe', 's')
panel(15, 6, 9, 0, 11, '4', '6', '12', 'diviseurs : PPCM')
panel(44, 7.5, 12, 0, 24, 'rouge', 'bleu', 'rouge + bleu', 'parties : union', 's')
panel(73, 6, 9, 0, 11, '3', '7', '7', 'réels : plus grand')
save(fig, '79-056')
