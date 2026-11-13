import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
S2 = math.sqrt(2)
def plane(ax, cx, cy, k, ex=3, ey=None, x0=None, y0=None):
    ey = ey or ex; x0 = -ex if x0 is None else x0; y0 = -ey if y0 is None else y0
    arrow(ax, (cx + x0 * k, cy), (cx + ex * k, cy), 'fixe', lw=0.6)
    arrow(ax, (cx, cy + y0 * k), (cx, cy + ey * k), 'fixe', lw=0.6)
def clipline(ax, cx, cy, k, pts, role, x0, x1, y0, y1):
    seg = []
    for x, y in pts:
        if x0 <= x <= x1 and y0 <= y <= y1: seg.append((cx + x * k, cy + y * k))
        else:
            if len(seg) > 1: line(ax, seg, role, lw=1.1)
            seg = []
    if len(seg) > 1: line(ax, seg, role, lw=1.1)
def ellipse1(ax, cx, cy, k, role):
    t = np.linspace(0, 2 * math.pi, 240)
    line(ax, [(cx + (math.sqrt(.5) * math.cos(q) + S2 * math.sin(q)) / S2 * k, cy + (math.sqrt(.5) * math.cos(q) - S2 * math.sin(q)) / S2 * k) for q in t], role, lw=1.1)
def hyper2(ax, cx, cy, k, role, x0, x1, y0, y1):
    a = math.sqrt(4 / 3); b = 2
    for s in (1, -1):
        pts = [((s * a * math.cosh(q) + b * math.sinh(q)) / S2, (s * a * math.cosh(q) - b * math.sinh(q)) / S2) for q in np.linspace(-6, 6, 3000)]
        clipline(ax, cx, cy, k, pts, role, x0, x1, y0, y1)
fig, ax = canvas(68)
text(ax, 19, 64, 'avec terme croisé', 'sujet', 's'); text(ax, 69, 64, 'seulement des carrés', 'resultat', 's')
box(ax, 2, 44, 34, 14, 'sujet', label=r'$5x^2+6xy+5y^2=4$', size='s')
box(ax, 52, 44, 34, 14, 'resultat', label=r'$a\,X^2+b\,Y^2=4$', size='s')
arrow(ax, (37, 51), (51, 51), 'varie'); text(ax, 44, 55.5, 'comment ?', 'varie', 's')
ellipse1(ax, 44, 21, 11, 'fixe')
arrow(ax, (19, 43), (36, 30), 'fixe', curve=0.2); arrow(ax, (69, 43), (52, 30), 'fixe', curve=-0.2)
text(ax, 44, 4, 'la même courbe', 'fixe', 's')
save(fig, '71-009')
