import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def seg(ax, x, y, w, h, role, dash=False, filled=True):
    ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role] if filled else "none", lw=0.8, ls="--" if dash else "-", zorder=2))
fig, ax = canvas(64)
def col(x, y, s, role, size='l'):
    for i, ch in enumerate(s):
        if ch != ' ': text(ax, x + i * 3.6, y, ch, role if not isinstance(role, list) else role[i], size)
text(ax, 18, 57, 'en colonnes', 'fixe', 's'); text(ax, 66, 57, 'en fractions', 'fixe', 's')
col(7, 46, '0,25', 'sujet'); col(7, 35, '0,30', ['autre', 'autre', 'autre', 'varie'])
line(ax, [(5, 29), (24, 29)], 'fixe'); text(ax, 3.6, 35, '+', 'fixe', 'l')
col(7, 22, '0,55', 'resultat')
for y in (46, 35, 22): text(ax, 36, y, '=', 'fixe', 'l')
text(ax, 62, 46, '25/100', 'sujet', 'l'); text(ax, 62, 35, '30/100', 'autre', 'l')
line(ax, [(48, 29), (76, 29)], 'fixe'); text(ax, 46, 35, '+', 'fixe', 'l')
text(ax, 62, 22, '55/100', 'resultat', 'l')
text(ax, 44, 9, 'le 0 ajouté donne des centièmes', 'varie', 's')
save(fig, '07-086')
