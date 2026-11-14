import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(66)
cx, cy, R = 44, 30, 22
disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.6)
line(ax, [(cx - R - 4, cy), (cx + R + 4, cy)], 'fixe', lw=0.6)
line(ax, [(cx, cy - R - 3), (cx, cy + R + 3)], 'fixe', lw=0.6)
t = np.linspace(0, np.pi, 60)
ax.plot(cx + (R + 0.0) * np.cos(t), cy + R * np.sin(t), color=COL['varie'], lw=1.6, zorder=3)
arrow(ax, (cx - R + 0.4, cy + 3), (cx - R, cy + 0.5), 'varie', lw=1.2)
disc(ax, cx + R, cy, 1.5, 'fixe')
text(ax, cx + R + 3, cy - 3.5, r'$1$', 'fixe', 's')
disc(ax, cx - R, cy, 2, 'resultat')
text(ax, cx - R - 2, cy - 4, r'$-1$', 'resultat', 'm')
text(ax, cx, cy + R + 6, r'$\pi$ : un demi-tour', 'varie', 's')
text(ax, cx, cy + 6, r'$\cos\pi=-1$', 'encre', 's')
text(ax, cx, cy - 6, r'$\sin\pi=0$', 'encre', 's')
text(ax, 44, 4, r'$e^{i\pi}=\cos\pi+i\sin\pi=-1$', 'resultat', 'm')
save(fig, '66-085')
