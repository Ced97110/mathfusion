import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(60)
def panel(x0, deg, qh):
    L = 36; t = math.radians(deg); Q = (x0, 14); R = (x0 + L * math.cos(t), 14 + L * math.sin(t)); Hh = (R[0], 14)
    line(ax, [Q, R], 'fixe'); line(ax, [R, Hh], 'fixe', dash=True)
    line(ax, [Q, Hh], 'varie', lw=2.2)
    text(ax, x0 + (14 if deg == 30 else 8), 17.5, f'{deg}°', 'sujet', 's')
    text(ax, (Q[0] + Hh[0]) / 2, 8, qh, 'varie', 's')
panel(4, 30, 'QH = 0,866'); panel(50, 60, 'QH = 0,5')
text(ax, 44, 45, 'angle plus ouvert : QH plus court', 'varie', 's')
text(ax, 44, 2, '0,75 − 0,25 = 0,5 = cos 60°', 'resultat', 's')
save(fig, '34-060')
