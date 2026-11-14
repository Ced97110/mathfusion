import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(80)
X0, BW, BH = 4, 64, 8
data = [(3, 7, r'$m = 3$ : mots de 7 bits', '43 %', 58),
        (4, 15, r'$m = 4$ : code $(15, 11)$', '27 %', 36),
        (10, 1023, r'$m = 10$ : code $(1023, 1013)$', '1 %', 14)]
for m, n, lab, pct, y in data:
    cw = BW * m / n
    ax.add_patch(Rectangle((X0 + cw, y), BW - cw, BH, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
    ax.add_patch(Rectangle((X0, y), cw, BH, ec=COL['varie'], fc=COL['varie'], lw=0.8, zorder=3))
    text(ax, X0, y + BH + 3, lab, 'encre', 's', ha='left')
    text(ax, X0 + BW + 3, y + BH / 2, pct, 'varie', 'm', ha='left')
text(ax, 84, 74, 'bits de contrôle', 'varie', 's', ha='right')
ax.add_patch(Rectangle((8, 3.5), 3, 3, ec=COL['varie'], fc=COL['varie'], lw=0.5))
text(ax, 13, 5, 'contrôle', 'encre', 's', ha='left')
ax.add_patch(Rectangle((40, 3.5), 3, 3, ec=COL['sujet'], fc=FILL['sujet'], lw=0.5))
text(ax, 45, 5, 'utiles', 'encre', 's', ha='left')
save(fig, '68-154')
