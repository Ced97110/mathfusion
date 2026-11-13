import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(60)
k = 12; O = (46, 28)
f = lambda v: O[0] + v*k
cp = [(O[0]+k*math.cos(a), O[1]+k*math.sin(a)) for a in [i*2*math.pi/100 for i in range(101)]]
poly(ax, cp, 'sujet'); line(ax, cp, 'sujet')
line(ax, [(f(-3.3), O[1]), (f(2.3), O[1])], 'fixe')
for v in range(-3, 3):
    ax.plot([f(v)]*2, [O[1]-1.2, O[1]+1.2], color=COL['fixe'], lw=0.8, zorder=3)
    text(ax, f(v) + (-2.2 if v == -1 else 2.2 if v == 1 else 0), O[1]-4.5, f'{v}'.replace('-', '−'), 'fixe', 's')
for v in (-1, 1): disc(ax, f(v), O[1], 1.3, 'resultat')
for v in (-3, 2):
    line(ax, [(f(v), O[1]+9), (f(v), O[1]-1)], 'limite', dash=True)
    text(ax, f(v), O[1]+12, 'aucun point', 'limite', 's')
brace(ax, f(-1), f(1), O[1]+k+4, 'resultat', label='cosinus : de −1 à 1', down=False)
save(fig, '33-125')
