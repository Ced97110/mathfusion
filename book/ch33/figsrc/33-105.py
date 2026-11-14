import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, R = 28, 33, 24
def arc(a0, a1, r=R, n=60): return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
line(ax, arc(90, 270), 'autre', lw=2.0)
line(ax, arc(-90, 90), 'sujet', lw=2.0)
h = 0.5 * R
Pg = (cx - R * math.cos(math.radians(30)), cy + h); Pd = (cx + R * math.cos(math.radians(30)), cy + h)
rx = cx + R + 17
line(ax, [(rx, cy - R), (rx, cy + R)], 'fixe', lw=0.7)
line(ax, [(Pg[0], cy + h), (rx, cy + h)], 'fixe', lw=0.8, dash=True)
disc(ax, Pg[0], Pg[1], 1.8, 'autre'); disc(ax, Pd[0], Pd[1], 1.8, 'sujet'); disc(ax, rx, cy + h, 1.8, 'fixe')
text(ax, Pg[0] + 6, cy + h - 5, 'gauche', 'autre', 's'); text(ax, Pd[0] - 6, cy + h - 5, 'droite', 'sujet', 's')
text(ax, rx + 7, cy + h, '0,5', 'encre', 'm')
text(ax, cx, cy - R - 4, 'seule la hauteur est gardée', 'encre', 's')
text(ax, Pg[0] - 0.5, cy + h + 4, '150°', 'autre', 's'); text(ax, Pd[0] + 6, cy + h - 4.5, '30°', 'sujet', 's')
arrow(ax, (rx - 2, cy + h + 2), (Pd[0] + 2, cy + h + 2), 'resultat', curve=-0.35)
text(ax, cx + 6, cy + R + 3, 'arcsin choisit la droite', 'resultat', 's')
save(fig, '33-105')
