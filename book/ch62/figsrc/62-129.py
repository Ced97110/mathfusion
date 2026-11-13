import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# p = 5 : roots 1, z, z^2, z^3, z^4 on a circle, each one is the previous times z
cx, cy, R = 44, 44, 22
labs = [r'$1$', r'$z$', r'$z^2$', r'$z^3$', r'$z^4$']
for k in range(5):
    a = math.radians(72 * k); b = math.radians(72 * (k + 1))
    p = (cx + R * math.cos(a), cy + R * math.sin(a)); q = (cx + R * math.cos(b), cy + R * math.sin(b))
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle='-|>', mutation_scale=7, lw=1.0, color=COL['varie'],
                                 connectionstyle='arc3,rad=0.325', zorder=4, shrinkA=3, shrinkB=3))
    disc(ax, p[0], p[1], 2.2, 'varie' if k == 1 else 'sujet')
    text(ax, cx + (R + 7) * math.cos(a), cy + (R + 6) * math.sin(a), labs[k], 'varie' if k == 1 else 'sujet', 'm')
text(ax, cx, cy, r'$\times z$', 'varie', 'm')
text(ax, 44, 8, r'tout vient d’un seul nombre $z$', 'encre', 's')
save(fig, '62-129')
