import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(ax, x, y, r, role, lw=2.2):
    th = [i * math.pi / 90 for i in range(181)]
    line(ax, [(x + r * math.cos(t), y + r * math.sin(t)) for t in th], role, lw=lw)
fig, ax = canvas(58)
cx, cy, r = 25, 29, 16
disc(ax, cx, cy, r, 'fixe'); ring(ax, cx, cy, r, 'sujet', 2.6)
arrow(ax, (cx - r, cy), (cx + r, cy), 'fixe', lw=0.9, both=True)
text(ax, cx, cy + 3.5, '20 cm', 'fixe', 's')
box(ax, 60, 38, 22, 14, 'sujet', label=r'$C$', size='xl', weight='bold')
arrow(ax, (60, 41), (cx + r * 0.75, cy + r * 0.66 + 1), 'sujet', lw=1.0, curve=0.25)
text(ax, 71, 33, 'le tour du cercle', 'sujet', 's')
text(ax, 71, 21, '≈ 62,8 cm', 'resultat', 'm', weight='bold')
text(ax, 71, 15, 'nombre + unité', 'resultat', 's')
save(fig, '11-091')
