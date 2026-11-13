import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np

fig, ax = canvas(74)
u, cy = 12, 50
sq, gap = 5, 0.8
for cx, n, vis in ((22, 3, '3 visibles'), (66, 2, '4 visibles')):
    t = np.linspace(0, 2*np.pi, 1400); r = np.cos(n*t)
    rn = np.where(r < 0, r, np.nan); rp = np.where(r >= 0, r, np.nan)
    ax.plot(cx + u*rn*np.cos(t), cy + u*rn*np.sin(t), color=COL['varie'], lw=2.4, zorder=3, solid_capstyle='round')
    ax.plot(cx + u*rp*np.cos(t), cy + u*rp*np.sin(t), color=COL['sujet'], lw=1.2, zorder=3.5, solid_capstyle='round')
    kind = 'impair' if n % 2 else 'pair'
    text(ax, cx, 70, f'n = {n} ({kind})', 'encre', 'm')
    tot = 2*n
    w = tot*sq + (tot - 1)*gap
    x0 = cx - w/2
    for i in range(tot):
        role = 'sujet' if i < n else 'varie'
        box(ax, x0 + i*(sq + gap), 32, sq, sq, role, r=0.3, lw=0.7)
    text(ax, cx, 27, f'{n} + {n} = {tot} tracés', 'encre', 's')
    arrow(ax, (cx, 25.2), (cx, 20.5), 'fixe')
    box(ax, cx - 14, 12, 28, 8, 'resultat', label=vis, size='m')
box(ax, 24, 3.2, 3.2, 3.2, 'sujet', r=0.2, lw=0.6)
text(ax, 28.5, 4.8, 'positifs', 'sujet', 's', ha='left')
box(ax, 50, 3.2, 3.2, 3.2, 'varie', r=0.2, lw=0.6)
text(ax, 54.5, 4.8, 'négatifs', 'varie', 's', ha='left')
save(fig, '40-057')
