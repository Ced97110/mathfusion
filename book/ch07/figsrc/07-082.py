import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def seg(ax, x, y, w, h, role, dash=False, filled=True):
    ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role] if filled else "none", lw=0.8, ls="--" if dash else "-", zorder=2))
fig, ax = canvas(60)
text(ax, 22, 54, r'$0/4$', 'resultat', 'l', weight='bold')
text(ax, 66, 54, r'$4/0$', 'limite', 'l', weight='bold')
for i in range(4):
    seg(ax, 4 + i * 9, 30, 9, 11, 'fixe', filled=False)
text(ax, 22, 24, '4 parts, on en prend 0', 'resultat', 's')
text(ax, 22, 16, 'permis', 'resultat', 'm', weight='bold')
seg(ax, 48, 30, 36, 11, 'limite', dash=True, filled=False)
line(ax, [(48, 30), (84, 41)], 'limite', lw=1.2)
line(ax, [(48, 41), (84, 30)], 'limite', lw=1.2)
text(ax, 66, 24, '0 part : rien à prendre', 'limite', 's')
text(ax, 66, 16, 'interdit', 'limite', 'm', weight='bold')
save(fig, '07-082')
