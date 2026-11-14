import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# the four roots 1, i, -1, -i are four quarter turns on a circle
cx, cy, R = 44, 42, 22
line(ax, [(cx - R - 8, cy), (cx + R + 3, cy)], 'fixe', lw=0.7)
line(ax, [(cx, cy - R - 8), (cx, cy + R + 3)], 'fixe', lw=0.7)
labs = ['$1$', '$i$', '$-1$', '$-i$']
offs = [(7, 0), (0, 6.5), (-7.5, 0), (0, -6.5)]
for k in range(4):
    a = math.radians(90 * k); b = math.radians(90 * (k + 1))
    p = (cx + R * math.cos(a), cy + R * math.sin(a)); q = (cx + R * math.cos(b), cy + R * math.sin(b))
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle='-|>', mutation_scale=7, lw=1.0, color=COL['varie'],
                                 connectionstyle='arc3,rad=0.4142', zorder=4, shrinkA=3, shrinkB=3))
    disc(ax, p[0], p[1], 2.2, 'sujet')
    text(ax, p[0] + offs[k][0], p[1] + offs[k][1], labs[k], 'sujet', 'm')
text(ax, cx + 22, cy + 22, r'$\times i$', 'varie', 'm')
text(ax, 44, 8, 'un quart de tour à chaque pas', 'varie', 's')
save(fig, '62-127')
