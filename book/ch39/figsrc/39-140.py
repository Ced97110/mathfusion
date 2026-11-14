import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cx, cy, R = 30, 36, 26
def pt(deg, r=R):
    a = math.radians(deg); return (cx + r * math.cos(a), cy + r * math.sin(a))
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.6, zorder=1, ls='--'))
arrow(ax, (cx - R - 2, cy), (cx + R + 4, cy), 'fixe', lw=0.5)
vs = [pt(72 * k) for k in range(5)]
poly(ax, vs, 'sujet', fill=True, lw=1.0)
for k, p in enumerate(vs):
    disc(ax, p[0], p[1], 1.3, 'varie' if k == 1 else 'sujet')
t = [math.radians(72 * k / 20) for k in range(21)]
line(ax, [(cx + 9 * math.cos(v), cy + 9 * math.sin(v)) for v in t], 'varie', lw=0.9)
line(ax, [pt(72), (pt(72)[0], cy)], 'varie', lw=0.7, dash=True)
line(ax, [(cx, cy), (pt(72)[0], cy)], 'resultat', lw=1.6)
text(ax, cx + 13, cy + 4.5, '72°', 'varie', 's')
text(ax, cx + 6, cy - 3.5, r'$\cos 72^\circ$', 'resultat', 's')
text(ax, pt(0)[0] + 2, cy - 3.5, r'$1$', 'fixe', 's', ha='left')
text(ax, 72, 62, r'$5$ sommets', 'sujet', 's')
text(ax, 72, 54, r'$360^\circ\div5=72^\circ$', 'varie', 's')
text(ax, 72, 42, r'$+\;-\;\times\;\div\;\sqrt{\ }$', 'fixe')
text(ax, 72, 34, 'règle et compas', 'fixe', 's')
text(ax, 72, 20, r'$\cos 72^\circ$ par', 'resultat', 's')
text(ax, 72, 14, 'racines carrées ?', 'resultat', 's')
save(fig, '39-140')
