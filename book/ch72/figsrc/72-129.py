import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(62)
ox, oy, u = 24, 31, 17
poly(ax, [(ox-u, oy-u*0.9), (ox+u, oy-u*0.9), (ox+u, oy+u*0.9), (ox-u, oy+u*0.9)], 'sujet')
for a in range(0, 360, 45):
    t = math.radians(a + 20)
    arrow(ax, (ox, oy), (ox + 12*math.cos(t), oy + 12*math.sin(t)*0.95), 'sujet', lw=0.9)
disc(ax, ox, oy, 1.0, 'encre')
text(ax, ox, oy+u*0.9+4, r'plan $V$', 'sujet', 'm')
text(ax, ox, oy-u*0.9-4, 'tout vecteur : carré > 0', 'sujet', 's')
box(ax, 50, 40, 34, 14, 'fixe', label='0 plan hyperbolique', size='s', dash=True)
text(ax, 67, 59, r'$\nu = 0$', 'sujet', 'l')
box(ax, 50, 8, 34, 14, 'resultat', label=r'$X = V$', size='l')
text(ax, 67, 31, 'noyau = plan entier', 'resultat', 's')
save(fig, '72-129')
