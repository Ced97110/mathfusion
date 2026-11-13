import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np

fig, ax = canvas(70)
u, cy = 18, 36
for cx, n, cap in ((22, 3, 'orange sur le bleu'), (66, 2, 'orange : 2 pétales neufs')):
    t = np.linspace(0, 2*np.pi, 1400); r = np.cos(n*t)
    line(ax, [(cx - 19, cy), (cx + 19, cy)], 'fixe', lw=0.4)
    line(ax, [(cx, cy - 19), (cx, cy + 19)], 'fixe', lw=0.4)
    rn = np.where(r < 0, r, np.nan); rp = np.where(r >= 0, r, np.nan)
    ax.plot(cx + u*rn*np.cos(t), cy + u*rn*np.sin(t), color=COL['varie'], lw=2.6, zorder=3, solid_capstyle='round')
    ax.plot(cx + u*rp*np.cos(t), cy + u*rp*np.sin(t), color=COL['sujet'], lw=1.2, zorder=3.5, solid_capstyle='round')
    text(ax, cx, 62, f'r = cos {n}θ', 'sujet', 'm')
    text(ax, cx, 13, cap, 'varie', 's')
line(ax, [(24, 6), (30, 6)], 'sujet', lw=1.4)
text(ax, 32, 6, 'r ≥ 0', 'sujet', 's', ha='left')
line(ax, [(52, 6), (58, 6)], 'varie', lw=2.4)
text(ax, 60, 6, 'r < 0', 'varie', 's', ha='left')
save(fig, '40-056')
