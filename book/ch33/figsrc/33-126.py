import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(62)
u = 7; W0 = (10, 8)
line(ax, [(W0[0], W0[1]), (W0[0]+6.6*u, W0[1])], 'fixe', lw=1.2)
line(ax, [(W0[0], W0[1]), (W0[0], W0[1]+5.6*u)], 'fixe', lw=2.0)
arc = [(W0[0]+5*u*math.cos(a), W0[1]+5*u*math.sin(a)) for a in [i*math.pi/2/40 for i in range(41)]]
line(ax, arc, 'resultat', dash=True)
foot = (W0[0]+3*u, W0[1]); top = (W0[0], W0[1]+4*u)
line(ax, [foot, top], 'sujet', lw=2.0)
disc(ax, foot[0], foot[1], 1.2, 'sujet')
f6 = (W0[0]+6*u, W0[1]); disc(ax, f6[0], f6[1], 1.4, 'limite')
for m in (0, 3, 5, 6):
    ax.plot([W0[0]+m*u]*2, [W0[1]-1, W0[1]+1], color=COL['fixe'], lw=0.8, zorder=3)
    text(ax, W0[0]+m*u, W0[1]-4, str(m), 'fixe', 's')
text(ax, W0[0], W0[1]+5.6*u+3, 'mur', 'fixe', 's')
text(ax, 25, 25, 'échelle', 'sujet', 's', ha='left'); text(ax, 25, 21.5, '5 m', 'sujet', 's', ha='left')
text(ax, 48, W0[1]+10, 'pied à 6 m :', 'limite', 's', ha='left'); text(ax, 48, W0[1]+6.5, 'trop loin', 'limite', 's', ha='left')
text(ax, 38, W0[1]+34, 'portée 5 m', 'resultat', 's', ha='left')
save(fig, '33-126')
