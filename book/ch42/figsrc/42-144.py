import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
def cercle(cx, role, dash=False):
    ax.add_patch(Circle((cx, 28), 10, ec=COL[role], fc=FILL[role] if not dash else 'none', lw=1.0, ls='--' if dash else '-', zorder=2))
cercle(14, 'sujet'); cercle(44, 'autre', True); cercle(74, 'resultat')
text(ax, 14, 42, r'$A$', 'sujet', 'l')
text(ax, 44, 42, r'$\varnothing$', 'autre', 'l')
text(ax, 74, 42, r'$A$', 'resultat', 'l')
for cx, role in [(14, 'sujet'), (74, 'resultat')]:
    text(ax, cx - 4, 28, '2', role, 'l'); text(ax, cx + 4, 28, '5', role, 'l')
text(ax, 29, 28, r'$\cup$', 'varie', 'l')
text(ax, 59, 28, '=', 'resultat', 'l', weight='bold')
text(ax, 44, 13, 'aucun élément', 'autre', 's')
text(ax, 74, 13, '2 et 5, rien de plus', 'resultat', 's')
save(fig, '42-144')
