import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(84)
cx, cy, R = 44, 46, 21
def P(k, r=R):
    a = math.radians(90 - 90 * k); return (cx + r * math.cos(a), cy + r * math.sin(a))
roles = {0: 'resultat', 1: 'sujet', 2: 'fixe', 3: 'varie'}
r = 12
pts = [(cx + r * math.cos(math.radians(t)), cy + r * math.sin(math.radians(t))) for t in range(0, -268, -3)]
line(ax, pts, 'varie', lw=1.1)
arrow(ax, pts[-1], (cx + r * math.cos(math.radians(-270)), cy + r * math.sin(math.radians(-270))), 'varie')
text(ax, cx, cy, r'$+3$', 'varie', 'l')
for k in range(4):
    x, y = P(k); disc(ax, x, y, 5.5, roles[k], label=str(k), size='l')
text(ax, 79, cy, r'$a=1$', 'sujet', 'm')
text(ax, 9.5, cy, r'$-a=3$', 'varie', 'm')
text(ax, cx, 77.5, r'neutre $0$', 'resultat', 'm')
text(ax, cx, 12, r'$a+(-a)=0$', 'encre', 'l')
text(ax, cx, 5, '1 + 3 = 4, reste 0', 'fixe', 's')
save(fig, '45-145')
