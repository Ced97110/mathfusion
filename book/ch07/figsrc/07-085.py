import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def seg(ax, x, y, w, h, role, dash=False, filled=True):
    ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role] if filled else "none", lw=0.8, ls="--" if dash else "-", zorder=2))
fig, ax = canvas(80)
text(ax, 10, 75, 'tu as 1 part de 1/4', 'sujet', 'm', ha='left')
seg(ax, 10, 60, 14, 9, 'sujet')
text(ax, 17, 64.5, '1/4', 'sujet', 's')
text(ax, 22, 52, 'le signe − : retirer 3 parts', 'varie', 's', ha='left')
roles = ['varie', 'limite', 'limite']
for i in range(3):
    seg(ax, 10 + i * 16, 34, 14, 9, roles[i], dash=i > 0)
    text(ax, 17 + i * 16, 38.5, '1/4', roles[i], 's')
arrow(ax, (17, 60), (17, 43.5), 'sujet')
text(ax, 58, 38.5, 'pas de part', 'limite', 's', ha='left')
text(ax, 22, 14, r'$\frac{1-3}{4}$', 'encre', 'xl')
arrow(ax, (22, 21), (26, 33), 'limite')
text(ax, 36, 14, '= pas encore de réponse', 'limite', 's', ha='left')
save(fig, '07-085')
