import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(ax, x, y, r, role, lw=2.2):
    th = [i * math.pi / 90 for i in range(181)]
    line(ax, [(x + r * math.cos(t), y + r * math.sin(t)) for t in th], role, lw=lw)
fig, ax = canvas(64)
cx, cy, r = 44, 28, 25
disc(ax, cx, cy, r, 'fixe'); ring(ax, cx, cy, r, 'fixe', 1.0)
arrow(ax, (cx, cy), (cx - r + 0.6, cy), 'sujet', lw=1.8)
arrow(ax, (cx, cy), (cx + r - 0.6, cy), 'sujet', lw=1.8)
disc(ax, cx, cy, 1.3, 'encre')
text(ax, cx - r / 2, cy + 4, r'$r$ = 5 cm', 'sujet', 's'); text(ax, cx + r / 2, cy + 4, r'$r$ = 5 cm', 'sujet', 's')
text(ax, cx, cy - 4.5, 'centre', 'encre', 's')
brace(ax, cx - r, cx + r, cy + r + 2, 'fixe', label=r'$d$ = 10 cm', down=False)
text(ax, cx, cy - 12, r'$r$ = $d$ $\div$ 2 = 5 cm', 'resultat', 'm', weight='bold')
save(fig, '11-093')
