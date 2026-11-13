import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(ax, x, y, r, role, lw=2.2):
    th = [i * math.pi / 90 for i in range(181)]
    line(ax, [(x + r * math.cos(t), y + r * math.sin(t)) for t in th], role, lw=lw)
fig, ax = canvas(70)
cx, cy, r = 32, 36, 24
disc(ax, cx, cy, r, 'fixe'); ring(ax, cx, cy, r, 'fixe', 1.0)
arrow(ax, (cx - r, cy), (cx + r, cy), 'sujet', lw=1.6, both=True)
disc(ax, cx, cy, 1.1, 'encre'); disc(ax, cx - r, cy, 1.1, 'sujet'); disc(ax, cx + r, cy, 1.1, 'sujet')
text(ax, cx, cy + 4, r'diamètre $d$', 'sujet', 'm', weight='bold')
text(ax, cx, cy - 4.5, 'centre', 'encre', 's')
text(ax, 72, 48, 'extrémité', 'sujet', 's')
arrow(ax, (72, 44), (cx + r + 1, cy + 1.5), 'sujet', lw=0.8, curve=0.2)
text(ax, 14, 8, 'extrémité', 'sujet', 's', ha='left')
arrow(ax, (14, 11), (cx - r - 0.5, cy - 1.5), 'sujet', lw=0.8, curve=-0.2)
save(fig, '11-082')
