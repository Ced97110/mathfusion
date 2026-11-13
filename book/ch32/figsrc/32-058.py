import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role, head=False, lw=0.9):
    n = 90
    pts = [pol(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw=lw)
fig, ax = canvas(90)
ox, oy, r = 7, 44, 34
hx = ox + 0.5 * r; h = math.sqrt(3) / 2 * r
arc(ax, ox, oy, r, -90, 90, 'fixe')
line(ax, [(3, oy), (42, oy)], 'fixe')
poly(ax, [(ox, oy), (hx, oy), (hx, oy + h)], 'sujet')
poly(ax, [(ox, oy), (hx, oy), (hx, oy - h)], 'resultat')
arc(ax, ox, oy, 5.5, 0, 60, 'sujet'); arc(ax, ox, oy, 5.5, -60, 0, 'resultat')
text(ax, 4.5, oy - 3.3, '$O$', 'fixe', 's'); text(ax, hx + 2.6, oy + 2, '$H$', 'fixe', 's')
text(ax, hx + 2.5, oy + h + 1.5, '$P$', 'sujet', 'm'); text(ax, hx + 3, oy - h - 1.5, "$P'$", 'resultat', 'm')
text(ax, 18.5, oy + 2.3, '0,5', 'sujet', 's'); text(ax, 12, oy + 15, '1', 'sujet', 's')
text(ax, 13.2, oy + 3.6, r'$\theta$', 'sujet', 's'); text(ax, 13.2, oy - 3.6, r'$-\theta$', 'resultat', 's')
box(ax, 47, 62, 39, 10, 'fixe', label='départ : côtés 0,5 et 1', size='s')
box(ax, 47, 40, 39, 10, 'varie', label='mêmes côtés, même angle', size='s')
box(ax, 47, 18, 39, 10, 'resultat', label='arrivée : P′ est à −θ', size='s')
arrow(ax, (66.5, 61.5), (66.5, 50.5), 'fixe'); arrow(ax, (66.5, 39.5), (66.5, 28.5), 'fixe')
save(fig, '32-058')
