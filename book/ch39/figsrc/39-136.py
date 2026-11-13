import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
bx, by, bs = 3, 6, 56
box(ax, bx, by, bs, bs, 'fixe', label=None)
cx, cy, R = bx + bs / 2, by + bs / 2, 17
ax.add_patch(Circle((cx, cy), R, ec=COL['sujet'], fc=FILL['sujet'], lw=1.0, zorder=2))
ax.add_patch(Circle((cx, cy), 1.0, ec=COL['limite'], fc='white', lw=0.8, zorder=3))
def pt(deg, r=R):
    a = math.radians(deg); return (cx + r * math.cos(a), cy + r * math.sin(a))
for deg, role in [(25, 'autre'), (65, 'varie'), (90, 'resultat')]:
    disc(ax, *pt(deg), 1.5, role)
text(ax, pt(25)[0] + 2.5, pt(25)[1] - 3, r'$z$', 'autre', 's')
text(ax, pt(65)[0] + 3.5, pt(65)[1] + 1.5, r'$w$', 'varie', 's')
text(ax, cx, pt(90)[1] + 4, r'$zw$', 'resultat', 's')
text(ax, bx + 4, by + bs - 4, r'$\mathbb{C}^*$', 'fixe', 'l', ha='left')
text(ax, cx, cy - 5, r'$\mathbb{T}$', 'sujet', 'l')
text(ax, 74, 58, r'$\mathbb{C}^*$ : groupe', 'fixe', ha='center')
text(ax, 74, 51, r'$2\times 3=6\neq 0$', 'fixe', 's')
text(ax, 74, 40, r'$\mathbb{T}$ : $|z|=1$', 'sujet', ha='center')
text(ax, 74, 33, r'$1\times 1=1$', 'sujet', 's')
text(ax, 74, 22, 'sous-groupe', 'sujet', 's')
text(ax, 74, 15, r'produit : reste dans $\mathbb{T}$', 'resultat', 's')
save(fig, '39-136')
