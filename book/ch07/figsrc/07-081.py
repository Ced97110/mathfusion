import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def seg(ax, x, y, w, h, role, dash=False, filled=True):
    ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role] if filled else "none", lw=0.8, ls="--" if dash else "-", zorder=2))
fig, ax = canvas(62)
x0, pw = 10, 17
text(ax, 44, 56, '3/4 de pizza', 'sujet', 'l')
for i in range(4):
    seg(ax, x0 + i * pw, 40, pw, 9, 'sujet' if i < 3 else 'fixe')
    text(ax, x0 + i * pw + pw / 2, 44.5, '1/4', 'sujet' if i < 3 else 'fixe', 's')
arrow(ax, (44, 39), (44, 30), 'varie')
text(ax, 48, 34.5, 'on donne 3/4', 'varie', 's', ha='left')
for i in range(4):
    seg(ax, x0 + i * pw, 19, pw, 9, 'fixe', dash=True, filled=False)
text(ax, 44, 14, '0 part de taille 1/4', 'fixe', 's')
text(ax, 44, 5.5, '0/4 = 0', 'resultat', 'l', weight='bold')
save(fig, '07-081')
