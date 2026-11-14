import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
base, H, w = 14, 30, 11
def rect(x, y0, y1, role):
    poly(ax, [(x, y0), (x + w, y0), (x + w, y1), (x, y1)], role)
# swatches
poly(ax, [(14, 72.5), (18, 72.5), (18, 76.5), (14, 76.5)], 'sujet')
text(ax, 20, 74.5, 'nombre exact', 'sujet', 's', ha='left')
poly(ax, [(50, 72.5), (54, 72.5), (54, 76.5), (50, 76.5)], 'autre')
text(ax, 56, 74.5, r'$2^{n}/n$', 'autre', 'm', ha='left')
groups = [(14, 3, 4, 'n = 4', 'écart : un tiers'), (54, 9, 10.667, 'n = 6', 'écart : moins d’un cinquième')]
for x, ex, q, nl, gl in groups:
    hq = H * q / ex
    rect(x, base, base + H, 'sujet')
    rect(x + w + 2, base, base + H, 'autre')
    rect(x + w + 2, base + H, base + hq, 'varie')
    text(ax, x + w / 2, base + H + 3, str(ex), 'sujet', 'm')
    text(ax, x + w + 2 + w / 2, base + hq + 3, ('10,7' if q > 10 else '4'), 'autre', 'm')
    text(ax, x + w + 1, base - 5, nl, 'encre', 'm')
    text(ax, x + w + 1, 64, gl, 'varie', 's')
line(ax, [(6, base), (82, base)], 'fixe')
text(ax, 44, 3.5, 'exact ramené à même hauteur', 'fixe', 's')
save(fig, '67-198')
