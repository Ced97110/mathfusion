import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def seg(ax, x, y, w, h, role, dash=False, filled=True):
    ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role] if filled else "none", lw=0.8, ls="--" if dash else "-", zorder=2))
fig, ax = canvas(54)
x0, pw = 6, 2.4
seg(ax, x0, 34, 30 * pw, 8, 'fixe', filled=False)
for i in range(1, 30): line(ax, [(x0 + i * pw, 34), (x0 + i * pw, 36 if i % 5 else 37.5)], 'fixe', lw=0.4)
marks = [(10, '1/3', 'autre'), (12, '2/5', 'sujet'), (15, '1/2', 'autre')]
for n, lab, role in marks:
    line(ax, [(x0 + n * pw, 34), (x0 + n * pw, 42)], role, lw=1.6)
    text(ax, x0 + n * pw, 31, str(n), role, 's'); text(ax, x0 + n * pw, 25.5, lab, role, 's', weight='bold')
text(ax, x0, 31, '0', 'fixe', 's'); text(ax, x0 + 30 * pw, 31, '30', 'fixe', 's')
brace(ax, x0 + 10 * pw, x0 + 15 * pw, 43, 'resultat', '2/5 entre 1/3 et 1/2', down=False)
text(ax, 44, 12, 'barre de 1 : 30 parts égales', 'fixe', 's')
save(fig, '07-091')
