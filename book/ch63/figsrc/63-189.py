import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
# les quatre racines de x^4 - 2 forment un carré ; ses 8 symétries = les 8 automorphismes
cx, cy, R = 44, 52, 24
verts = [(cx + R, cy), (cx, cy + R), (cx - R, cy), (cx, cy - R)]
poly(ax, verts, 'sujet')
# axes de réflexion : 2 axes + 2 médiatrices
for a in (0, 90):
    c, s = math.cos(math.radians(a)), math.sin(math.radians(a))
    line(ax, [(cx - (R + 4) * c, cy - (R + 4) * s), (cx + (R + 4) * c, cy + (R + 4) * s)], 'autre', dash=True, lw=0.8)
for a in (45, 135):
    c, s = math.cos(math.radians(a)), math.sin(math.radians(a))
    line(ax, [(cx - (R * 0.72 + 3) * c, cy - (R * 0.72 + 3) * s), (cx + (R * 0.72 + 3) * c, cy + (R * 0.72 + 3) * s)], 'autre', dash=True, lw=0.8)
for v in verts: disc(ax, v[0], v[1], 1.7, 'sujet')
text(ax, cx + R + 3, cy + 3.5, r'$\sqrt[4]{2}$', 'sujet', 's', ha='left')
text(ax, cx + 3, cy + R + 4, r'$i\sqrt[4]{2}$', 'sujet', 's', ha='left')
text(ax, cx - R - 3, cy + 3.5, r'$-\sqrt[4]{2}$', 'sujet', 's', ha='right')
text(ax, cx + 3, cy - R - 4, r'$-i\sqrt[4]{2}$', 'sujet', 's', ha='left')
# rotation d'un quart de tour
th = [math.radians(d) for d in range(10, 80, 5)]
line(ax, [(cx + 9 * math.cos(a), cy + 9 * math.sin(a)) for a in th], 'varie', lw=1.2)
arrow(ax, (cx + 9 * math.cos(math.radians(70)), cy + 9 * math.sin(math.radians(70))), (cx + 9 * math.cos(math.radians(80)) - 0.3, cy + 9 * math.sin(math.radians(80))), 'varie', lw=1.2)
text(ax, 22, 12, '4 rotations', 'varie', 'm')
text(ax, 66, 12, '4 réflexions', 'autre', 'm')
text(ax, 44, 3, r'$4 + 4 = 8$ = degré du corps', 'resultat', 'm')
save(fig, '63-189')
