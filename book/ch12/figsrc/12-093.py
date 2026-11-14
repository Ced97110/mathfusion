import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, r=1.1, hollow=False):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc="white" if hollow else COL[role], lw=0.9, zorder=6))

fig, ax = canvas(52)
y = 24
f = numberline(ax, 8, 66, y, 0, 7, labels=False)
for v in (0, 3, 5):
    text(ax, f(v), y - 4.5, str(v), 'fixe' if v == 0 else ('sujet' if v == 3 else 'resultat'), 'm')
dot(ax, f(3), y, 'sujet', 1.5); dot(ax, f(5), y, 'resultat', 1.5)
arrow(ax, (f(3) + 1.5, y + 3), (f(5) - 1.5, y + 3), 'varie', curve=-0.5)
text(ax, (f(3) + f(5)) / 2, y + 11, '+ 2', 'varie', 'm')
text(ax, f(3), y + 7, 'départ', 'sujet', 's', ha='right') if False else None
text(ax, 44, 46, '3 + 2 : un seul point d’arrivée', 'resultat', 'm')
text(ax, 44, 8, 'ce point porte un réel', 'resultat', 's')
save(fig, '12-093')
