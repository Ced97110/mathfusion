import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(66)
ox, oy, u = 13, 31, 6.5
th = np.linspace(0, 2 * math.pi, 600)
def curve(f, role, lw):
    line(ax, [(ox + u * f(t) * math.cos(t), oy + u * f(t) * math.sin(t)) for t in th], role, lw=lw)
curve(lambda t: 3 * (1 + math.cos(t)), 'autre', 1.3)
curve(lambda t: 1 + math.cos(t - math.pi / 2), 'varie', 1.5)
curve(lambda t: 1 + math.cos(t), 'sujet', 1.5)
arrow(ax, (ox - 4, oy), (ox + 42, oy), 'fixe', lw=0.5)
arrow(ax, (ox, oy - 27), (ox, oy + 27), 'fixe', lw=0.5)
disc(ax, ox + 2 * u, oy, 1.1, 'sujet')
disc(ax, ox, oy + 2 * u, 1.1, 'varie')
disc(ax, ox + 6 * u, oy, 1.1, 'autre')
text(ax, 72, 56, 'r = f(θ) = 1 + cos θ\nsommet : (2 ; 0°)', 'sujet', 's')
text(ax, 72, 38, 'tourner de π/2 :\nr = f(θ − π/2)\nsommet : (2 ; 90°)', 'varie', 's')
text(ax, 72, 20, 'agrandir par 3 :\nr = 3 f(θ)\nsommet : (6 ; 0°)', 'autre', 's')
save(fig, '40-129')
