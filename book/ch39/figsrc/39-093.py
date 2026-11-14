import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
R = 9.5
def P(cx, cy, d): return (cx + R * math.cos(math.radians(d)), cy + R * math.sin(math.radians(d)))
def circle(cx, cy, role):
    ax.add_patch(Circle((cx, cy), R, ec=COL[role], fc='none', lw=1.3 if role == 'sujet' else 0.7, ls='-' if role == 'sujet' else '--', zorder=2))
    disc(ax, cx, cy, 0.6, 'fixe')
cy = 32
# panel 1: same circle
cx = 15; circle(cx, cy, 'sujet'); line(ax, [(cx, cy), P(cx, cy, 90)], 'sujet', lw=1.0)
text(ax, cx + 3.5, cy + 4.5, '2', 'sujet', 's')
text(ax, cx, 14, 'même cercle,', 'sujet', 's'); text(ax, cx, 9.5, 'rayon 2', 'sujet', 's')
# panel 2: start angle
cx = 44; circle(cx, cy, 'fixe'); disc(ax, *P(cx, cy, 0), 1.5, 'resultat')
line(ax, [(cx, cy), P(cx, cy, 0)], 'fixe', lw=0.8)
text(ax, P(cx, cy, 0)[0] + 2, P(cx, cy, 0)[1] + 3.5, '$z_0$', 'resultat', 's')
text(ax, cx, 14, 'départ', 'resultat', 's'); text(ax, cx, 9.5, 'à 0°', 'resultat', 's')
# panel 3: step
cx = 73; circle(cx, cy, 'fixe')
for d in (0, 120, 240): disc(ax, *P(cx, cy, d), 1.5, 'varie' if d else 'resultat')
for d in (0, 120):
    pts = [P(cx, cy, d + 6 + 108 * i / 20) for i in range(21)]
    line(ax, pts, 'varie', lw=1.0); arrow(ax, pts[-3], pts[-1], 'varie', lw=1.0)
text(ax, cx - 1, cy + 14, '+ 120°', 'varie', 's')
text(ax, cx, 14, 'pas', 'varie', 's'); text(ax, cx, 9.5, 'de 120°', 'varie', 's')
text(ax, 44, 51, 'racines cubiques de 8', 'encre', 's')
save(fig, '39-093')
