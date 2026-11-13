import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
X = lambda a: 8 + 0.2 * a; Y = lambda t: 34 + 5.5 * t
line(ax, [(X(0), 34), (X(360) + 4, 34)], 'fixe', lw=0.8)
for a in (90, 270): line(ax, [(X(a), 8), (X(a), 60)], 'limite', dash=True)
def branch(a0, a1, role):
    pts = [(X(a), Y(math.tan(math.radians(a)))) for a in [a0 + (a1 - a0) * i / 60 for i in range(61)]]
    line(ax, [p for p in pts if 8 <= p[1] <= 60], role, lw=1.6)
branch(0, 87.5, 'sujet'); branch(92.5, 267.5, 'sujet'); branch(272.5, 360, 'sujet')
line(ax, [(X(0), Y(1)), (X(225), Y(1))], 'resultat', dash=True)
for a in (45, 225): disc(ax, X(a), Y(1), 1.4, 'resultat')
text(ax, X(45), Y(1) + 3.5, '45°', 'resultat', 's'); text(ax, X(225) - 3, Y(1) + 3.5, '225°', 'resultat', 's')
arrow(ax, (X(90), 4), (X(270), 4), 'varie', both=True); text(ax, 44, 7.5, '180°', 'varie', 's')
for a in (90, 270): text(ax, X(a), 63.5, f'{a}°', 'limite', 's')
for a in (0, 180, 360): text(ax, X(a), 29.5, f'{a}°', 'fixe', 's')
save(fig, '25-138')
