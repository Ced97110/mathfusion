import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
cx, cy, Rr, r = 44, 66, 24, 3.2

def edge(p, q, d):
    dx, dy = q[0] - p[0], q[1] - p[1]; n = math.hypot(dx, dy)
    return (p[0] + dx / n * d, p[1] + dy / n * d)

labs = [r'$r$', r'$zr$', r'$z^2r$', r'$z^3r$', r'$z^4r$']
ax.add_patch(Circle((cx, cy), Rr, ec=COL['fixe'], fc='none', lw=0.6, zorder=1))
pts = [(cx + Rr * math.cos(math.radians(72 * k)), cy + Rr * math.sin(math.radians(72 * k))) for k in range(5)]
# le renommage envoie r sur z^2 r (exemple k = 2)
arrow(ax, edge(pts[0], pts[2], r), edge(pts[2], pts[0], r), 'varie', curve=-0.25)
for k, p in enumerate(pts):
    role = 'sujet' if k == 0 else ('varie' if k == 2 else 'fixe')
    disc(ax, p[0], p[1], r, role)
    a = math.radians(72 * k)
    text(ax, cx + (Rr + 8.5) * math.cos(a), cy + (Rr + 6) * math.sin(a), labs[k], role, 'm')
text(ax, cx, cy + 4, r'$x^5=2$', 'sujet', 'l')
text(ax, cx, cy - 3, r'5 solutions', 'fixe', 's')
text(ax, 44, 30, r'$\eta(r)=z^kr$ : ici $k=2$', 'varie', 'm')
text(ax, 44, 23, r'$z$ est dans $F$ : $\eta$ le laisse fixe', 'fixe', 's')
text(ax, 44, 16, r'$\eta\mapsto z^k$ plonge le groupe dans $U$', 'varie', 's')
text(ax, 44, 9, r'$U$ cyclique : un sous-groupe est cyclique', 'resultat', 's')
save(fig, '64-153')
