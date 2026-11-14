import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(76)
cx, cy, u = 44, 40, 15
th = np.linspace(0, 2 * math.pi, 600)
line(ax, [(cx + u * (1 + math.cos(t)) * math.cos(t), cy + u * (1 + math.cos(t)) * math.sin(t)) for t in th], 'sujet', lw=1.5)
arrow(ax, (cx - 34, cy), (cx + 36, cy), 'fixe', lw=0.6)
arrow(ax, (cx, cy - 23), (cx, cy + 24), 'fixe', lw=0.6)
disc(ax, cx + 2 * u, cy, 1.3, 'resultat')
disc(ax, cx - 2 * u, cy, 1.3, 'limite', fill=False, lw=1.1)
disc(ax, cx, cy, 0.8, 'fixe')
text(ax, 81, cy + 5, 'A\n(2 ; 0)', 'resultat', 's')
text(ax, 81, cy - 5.5, 'sur la\ncourbe', 'resultat', 's')
text(ax, cx - 2 * u + 3, cy + 4, r'$B\,(-2\,;\,0)$', 'limite', 's')
text(ax, cx - 2 * u + 3, cy - 4, 'hors courbe', 'limite', 's')
text(ax, 44, 71, r'cardioïde $r=1+\cos\theta$', 'sujet', 'm')
text(ax, 44, 12, 'par l’axe des x : oui', 'resultat', 's')
text(ax, 44, 6, 'par le pôle (B) : non', 'limite', 's')
save(fig, '40-127')
