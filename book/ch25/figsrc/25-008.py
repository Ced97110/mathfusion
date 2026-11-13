import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, c, r, a0, a1, role, lw=0.9):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 120)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 120))) for i in range(121)]
    line(ax, pts, role, lw)

fig, ax = canvas(78)
line(ax, [(4, 10), (86, 10)], 'fixe', lw=0.8)
line(ax, [(10, 10), (10, 16)], 'varie', lw=1.8); line(ax, [(10, 10), (13, 10)], 'sujet', lw=2.0)
line(ax, [(40, 10), (40, 70)], 'varie', lw=1.8); line(ax, [(40, 10), (70, 10)], 'sujet', lw=2.0)
line(ax, [(10, 16), (13, 10)], 'encre', dash=True, lw=0.7); line(ax, [(40, 70), (70, 10)], 'encre', dash=True, lw=0.7)
text(ax, 10, 22, 'bâton 2 m', 'varie', 's')
text(ax, 12, 5, 'ombre 1 m', 'sujet', 's')
text(ax, 55, 5, 'ombre 70 m', 'sujet', 's')
text(ax, 40, 74.5, 'pyramide', 'varie', 's')
text(ax, 24, 45, 'même rapport : 2', 'fixe', 's')
text(ax, 64, 56, '2 × 70 = 140 m', 'resultat', 'm')
save(fig, '25-008')
