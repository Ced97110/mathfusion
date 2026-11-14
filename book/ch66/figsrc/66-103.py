import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
tx, ty, tr = 65, 34, 16
arch = [(tx + tr * math.cos(math.radians(t)), ty + tr * math.sin(math.radians(t))) for t in range(0, 181, 6)]
poly(ax, [(tx - tr, 6)] + [(tx + tr, 6)] + arch, 'fixe')
n = 17
pts = [(tx + 11 * math.cos(math.radians(90 + k * 360 / n)), 33 + 11 * math.sin(math.radians(90 + k * 360 / n))) for k in range(n)]
poly(ax, pts, 'sujet')
text(ax, tx, 15, '17 côtés', 'sujet', 'm')
text(ax, tx, 2.5, 'à graver sur sa tombe', 'fixe', 's')
text(ax, 22, 40, 'Gauss', 'encre', 'l', weight='bold')
text(ax, 22, 32, '19 ans, en 1796', 'encre', 'm')
text(ax, 22, 25, 'construit le 17-gone', 'sujet', 'm')
arrow(ax, (38, 29), (46, 29), 'varie')
save(fig, '66-103')
