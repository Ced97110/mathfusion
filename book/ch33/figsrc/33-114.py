import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(50)
O = (10, 8); R = 34; t = math.atan(3/4)
arcpts = [(O[0] + R*math.cos(a), O[1] + R*math.sin(a)) for a in [i*math.pi/2/40 for i in range(41)]]
poly(ax, [O] + arcpts, 'fixe')
line(ax, [O, (O[0]+R, O[1])], 'fixe', lw=1.0); line(ax, [O, (O[0], O[1]+R)], 'fixe', lw=1.0)
line(ax, [O, (O[0]+R*math.cos(t), O[1]+R*math.sin(t))], 'sujet', lw=1.6)
line(ax, [(O[0]+9*math.cos(a), O[1]+9*math.sin(a)) for a in [i*t/20 for i in range(21)]], 'varie', lw=1.0)
text(ax, O[0]+13, O[1]+3.5, r'$\theta$', 'varie', 'm')
text(ax, O[0]+R, O[1]-3, '0°', 'fixe', 's'); text(ax, O[0]+1, O[1]+R+3, '90°', 'fixe', 's')
text(ax, 62, 40, r'$\theta=\arctan\frac{3}{4}$', 'sujet', 'm')
text(ax, 62, 33, r'$\frac{3}{4}>0$', 'fixe', 'm')
text(ax, 62, 17, 'angle aigu :', 'resultat', 's'); text(ax, 62, 13, 'entre 0° et 90°', 'resultat', 's')
save(fig, '33-114')
