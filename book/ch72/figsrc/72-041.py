import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
def ax2(ax, cx, cy, r):
    arrow(ax, (cx - r, cy), (cx + r, cy), 'fixe', lw=0.6)
    arrow(ax, (cx, cy - r), (cx, cy + r), 'fixe', lw=0.6)

cx, cy, s = 30, 12, 8
arrow(ax, (cx - 4, cy), (cx + 52, cy), 'sujet', lw=1.4)
arrow(ax, (cx, cy - 4), (cx, cy + 56), 'autre', lw=1.4)
arrow(ax, (cx, cy), (cx + 3 * s, cy + 5 * s * 1.0), 'varie', lw=1.6)
line(ax, [(cx + 3 * s, cy), (cx + 3 * s, cy + 5 * s)], 'fixe', dash=True)
line(ax, [(cx, cy + 5 * s), (cx + 3 * s, cy + 5 * s)], 'fixe', dash=True)
disc(ax, cx + 3 * s, cy, 1.2, 'sujet'); disc(ax, cx, cy + 5 * s, 1.2, 'autre')
text(ax, cx + 3 * s + 14, cy + 5 * s + 3, '(3, 5)', 'varie', 'm')
text(ax, cx + 3 * s, cy - 5, r'(3, 0) $\in U$', 'sujet', 's')
text(ax, cx + 16, cy + 5 * s + 8, r'(0, 5) $\in U^\perp$', 'autre', 's') if False else text(ax, cx + 14, cy + 5 * s + 9, r'(0, 5) $\in U^\perp$', 'autre', 's')
text(ax, cx + 46, cy + 5, r'$U$', 'sujet', 'm'); text(ax, cx - 5, cy + 54, r'$U^\perp$', 'autre', 'm')
save(fig, '72-041')
