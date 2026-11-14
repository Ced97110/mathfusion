import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# les trois racines de x^3 - 2 : r, jr, j^2 r (rayon = racine cubique de 2, échelle 17 mm)
cx, cy, R = 30, 44, 21
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.6, ls='--', zorder=1))
arrow(ax, (cx - R - 6, cy), (cx + R + 7, cy), 'fixe', lw=0.7)
line(ax, [(cx, cy - R - 5), (cx, cy + R + 5)], 'fixe', lw=0.7)
ax.plot([cx - R - 6, cx + R + 6], [cy, cy], color=COL['resultat'], lw=3.2, alpha=0.35, zorder=1, solid_capstyle='butt')
pts = [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in (0, 120, 240)]
disc(ax, pts[0][0], pts[0][1], 2.0, 'resultat')
disc(ax, pts[1][0], pts[1][1], 2.0, 'limite'); disc(ax, pts[2][0], pts[2][1], 2.0, 'limite')
text(ax, pts[0][0] - 1, pts[0][1] + 5, r'$r$', 'resultat', 'm')
text(ax, pts[1][0] - 4, pts[1][1] + 3, r'$jr$', 'limite', 'm')
text(ax, pts[2][0] - 4, pts[2][1] - 3, r'$j^2 r$', 'limite', 'm')
text(ax, cx - R - 3, cy + 4, r'$\mathbb{R}$', 'resultat', 's')
x0 = 64
text(ax, x0, 70, r'$\mathbb{Q}(r)$ est dans $\mathbb{R}$', 'resultat', 's')
text(ax, x0, 60, r'$\eta(r)$ est une racine', 'encre', 's')
text(ax, x0, 54, r'de $x^3 - 2$ dans $\mathbb{Q}(r)$', 'encre', 's')
text(ax, x0, 44, r'$\eta(r) = r$', 'resultat', 'm')
# 1 automorphisme contre 3 de degré
for i in range(3):
    box(ax, x0 - 12 + i * 8, 22, 8, 7, 'sujet' if i == 0 else 'fixe', fill=True)
box(ax, x0 - 12, 10, 8, 7, 'resultat')
text(ax, x0 + 15, 25.5, r'$[\mathbb{Q}(r) : \mathbb{Q}] = 3$', 'sujet', 's', ha='left') if False else None
text(ax, x0 - 12, 31.5, 'degré 3', 'sujet', 's', ha='left')
text(ax, x0 - 12, 19.5, '1 automorphisme', 'resultat', 's', ha='left')
text(ax, 44, 4, r'$1 < 3$', 'limite', 'l')
save(fig, '63-178')
