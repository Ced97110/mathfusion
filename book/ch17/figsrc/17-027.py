import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def dot(x, y, role, full=True, r=1.6):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL["encre"], lw=0.9, zorder=4))
text(ax, 44, 64, r'$x + 7 > 4$', 'sujet', 'l', weight='bold')
text(ax, 2, 52, 'vérifier : essayer 0', 'encre', 'm', ha='left')
f = numberline(ax, 8, 62, 42, -6, 3, labels=False)
dot(f(0), 42, 'resultat', r=2); text(ax, f(0), 36, '0', 'resultat', 's')
text(ax, 2, 26, 'résoudre : toutes les valeurs', 'encre', 'm', ha='left')
f = numberline(ax, 8, 62, 16, -6, 3, labels=False)
line(ax, [(f(-3), 16), (67, 16)], 'resultat', lw=2.2)
dot(f(-3), 16, 'resultat', full=False, r=2); text(ax, f(-3), 10, '−3', 'resultat', 's')
save(fig, '17-027')
