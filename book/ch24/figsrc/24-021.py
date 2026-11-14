import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(70)
cA, cB, cy, R = 30, 58, 38, 20
d = cB - cA; h = (R**2 - (d/2)**2) ** 0.5; xm = (cA + cB) / 2
ang = np.arctan2(h, d/2)
tA = np.linspace(-ang, ang, 30); tB = np.linspace(np.pi - ang, np.pi + ang, 30)
poly(ax, [(cA + R*np.cos(t), cy + R*np.sin(t)) for t in tA] + [(cB + R*np.cos(t), cy + R*np.sin(t)) for t in np.linspace(np.pi - ang, np.pi + ang, 30)], 'resultat')
disc(ax, cA, cy, R, 'sujet', fill=False, lw=1.1)
disc(ax, cB, cy, R, 'autre', fill=False, lw=1.1)
text(ax, cA - 3, 63, r'$x+y=5$', 'sujet', 'm')
text(ax, cB + 3, 63, r'$2x+y=8$', 'autre', 'm')
text(ax, 22, 44, r'$(1,\,4)$', 'sujet', 's')
text(ax, 22, 34, r'$(2,\,3)$', 'sujet', 's')
text(ax, 22, 25, '…', 'sujet', 'm')
text(ax, 66, 38, '…', 'autre', 'm')
text(ax, xm, cy, r'$(3,\,2)$', 'resultat', 's', weight='bold')
text(ax, xm, 9, 'couple commun', 'resultat', 's')
arrow(ax, (xm, 13), (xm, 24.5), 'resultat', lw=0.9)
save(fig, '24-021')
