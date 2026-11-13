import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(ax, x, y, r, role, lw=2.2):
    th = [i * math.pi / 90 for i in range(181)]
    line(ax, [(x + r * math.cos(t), y + r * math.sin(t)) for t in th], role, lw=lw)
fig, ax = canvas(70)
cx, cy, r = 30, 36, 24
disc(ax, cx, cy, r, 'fixe'); ring(ax, cx, cy, r, 'fixe', 1.0)
line(ax, [(cx - r, cy), (cx, cy)], 'fixe', lw=1.0, dash=True)
arrow(ax, (cx, cy), (cx + r - 0.6, cy), 'sujet', lw=1.8)
disc(ax, cx, cy, 1.3, 'encre'); disc(ax, cx + r, cy, 1.1, 'sujet')
text(ax, cx + r / 2, cy + 4, r'rayon $r$ = 3 m', 'sujet', 'm', weight='bold')
text(ax, cx, cy - 4.5, 'piquet', 'encre', 's')
text(ax, cx - r / 2, cy + 4, '3 m', 'fixe', 's')
brace(ax, cx - r, cx + r, 5, 'resultat', label=r'diamètre $d$ = 6 m', down=False)
save(fig, '11-083')
