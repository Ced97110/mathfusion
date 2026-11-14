import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
f = numberline(ax, 6, 76, 60, 1, 2, step=0.1, every=5, arrow_right=False)
for v, role, s, ha in ((1.4, 'sujet', '1,4 → 1,96', 'right'), (1.5, 'varie', '1,5 → 2,25', 'left')):
    ax.plot([f(v)]*2, [57.5, 62.5], color=COL[role], lw=1.6, zorder=3)
    text(ax, f(v) + (1 if ha == 'left' else -1), 65.5, s, role, 's', ha=ha)
g = numberline(ax, 6, 76, 24, 1.40, 1.43, step=0.01, arrow_right=False)
for v, role, s in ((1.41, 'sujet', '1,9881 < 2'), (1.42, 'varie', '2,0164 > 2')):
    ax.plot([g(v)]*2, [21.5, 26.5], color=COL[role], lw=1.6, zorder=3)
    text(ax, g(v), 30, s, role, 's')
for xa, xb in ((f(1.4), g(1.40)), (f(1.5), g(1.43))):
    line(ax, [(xa, 52), (xb, 27)], 'fixe', lw=0.6, dash=True)
brace(ax, g(1.41), g(1.42), 14, 'resultat', label='le côté est ici', down=True, size='s')
text(ax, 44, 40, 'agrandissement', 'encre', 'm')
save(fig, '22-004')
