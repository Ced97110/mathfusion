import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(74)
R = 17
def axes_at(cx, cy):
    for k in range(3):
        a = math.radians(60 * k)
        line(ax, [(cx - 1.12 * R * math.cos(a), cy - 1.12 * R * math.sin(a)), (cx + 1.12 * R * math.cos(a), cy + 1.12 * R * math.sin(a))], 'fixe', lw=0.5, dash=True)
cx1, cx2, cy = 23, 65, 44
axes_at(cx1, cy); axes_at(cx2, cy)
th = np.linspace(0, 2 * math.pi, 600)
rr = np.cos(3 * th)
line(ax, [(cx1 + R * r * math.cos(t), cy + R * r * math.sin(t)) for r, t in zip(rr, th)], 'sujet', lw=1.5)
tri = [(cx2 + R * math.cos(math.radians(120 * k)), cy + R * math.sin(math.radians(120 * k))) for k in range(3)]
poly(ax, tri, 'autre')
for k in range(3):
    a = math.radians(120 * k)
    disc(ax, cx1 + R * math.cos(a), cy + R * math.sin(a), 1.0, 'varie')
for k in range(3):
    a0, a1 = math.radians(120 * k + 10), math.radians(120 * k + 110)
    p = (cx1 + 1.22 * R * math.cos(a0), cy + 1.22 * R * math.sin(a0))
    q = (cx1 + 1.22 * R * math.cos(a1), cy + 1.22 * R * math.sin(a1))
    arrow(ax, p, q, 'varie', lw=0.9, curve=0.35)
text(ax, cx1, 70, r'rosace $r=\cos 3\theta$', 'sujet', 's')
text(ax, cx2, 70, 'triangle équilatéral', 'autre', 's')
text(ax, cx1, 17, '3 rotations :\n0°, 120°, 240°', 'varie', 's')
text(ax, cx2, 17, '3 reflets\n(axes en pointillés)', 'fixe', 's')
text(ax, 44, 5, 'mêmes symétries : 3 rotations, 3 reflets', 'resultat', 's')
save(fig, '40-122')
