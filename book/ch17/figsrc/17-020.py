import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
def dot(x, y, role, full=True, r=1.6):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL["encre"], lw=0.9, zorder=4))
f = numberline(ax, 8, 70, 20, 0, 8)
dot(f(3), 20, 'sujet', r=2); dot(f(7), 20, 'autre', r=2)
arrow(ax, (f(7), 24), (f(3), 24), 'resultat', curve=0.4)
text(ax, f(5), 35, '3 est à gauche de 7', 'resultat', 'm')
text(ax, f(5), 44, r'$3 < 7$ : vrai', 'resultat', 'l', weight='bold')
save(fig, '17-020')
