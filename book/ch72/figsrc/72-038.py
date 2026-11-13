import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def ax2(ax, cx, cy, r):
    arrow(ax, (cx - r, cy), (cx + r, cy), 'fixe', lw=0.6)
    arrow(ax, (cx, cy - r), (cx, cy + r), 'fixe', lw=0.6)

for cx, t in ((22, 'anisotrope'), (66, 'pas anisotrope')):
    ax2(ax, cx, 34, 17)
    text(ax, cx, 57, t, 'sujet' if cx < 40 else 'limite', 'm')
arrow(ax, (22, 34), (22 + 9, 34 + 12), 'sujet', lw=1.2)
arrow(ax, (22, 34), (22, 34 + 8), 'sujet', lw=1.2)
text(ax, 36, 49, '25', 'sujet', 's'); text(ax, 18, 42, '4', 'sujet', 's')
text(ax, 22, 12, 'carré toujours > 0', 'sujet', 's')
line(ax, [(52, 20), (80, 48)], 'limite', lw=1.4)
arrow(ax, (66, 34), (66 + 9, 34 + 12), 'sujet', lw=1.2)
text(ax, 66, 12, 'une droite de carré 0', 'limite', 's')
text(ax, 22, 6, r'(3, 4) et (0, 2)', 'fixe', 's')
text(ax, 66, 6, 'plan de la seconde mesure', 'fixe', 's')
save(fig, '72-038')
