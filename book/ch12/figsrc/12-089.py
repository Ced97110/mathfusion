import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, r=1.1, hollow=False):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc="white" if hollow else COL[role], lw=0.9, zorder=6))

fig, ax = canvas(74)
y = 40
f = numberline(ax, 6, 70, y, -6, 6, labels=False)
ax.plot([f(0), f(0)], [y - 6, y + 6], color=COL['fixe'], lw=0.7, ls='--', zorder=1)
for v in (-5, -2, 2, 5):
    dot(ax, f(v), y, 'sujet' if v > 0 else 'autre', 1.2)
    text(ax, f(v), y - 4.5, f'{v}'.replace('-', '−'), 'sujet' if v > 0 else 'autre', 's')
text(ax, f(0), y - 4.5, 'O', 'fixe', 's')
arrow(ax, (f(2), y + 3), (f(5), y + 3), 'resultat', curve=-0.4)
text(ax, (f(2) + f(5)) / 2, y + 13, r'$5>2$', 'resultat', 'm')
arrow(ax, (f(-5), y - 9), (f(-2), y - 9), 'resultat', curve=0.4)
text(ax, (f(-5) + f(-2)) / 2, y - 22, r'$-5<-2$'.replace('-', '−') if False else '−5 < −2', 'resultat', 'm')
text(ax, 44, 66, '5 et −5 : même distance de O', 'fixe', 's')
text(ax, 44, 8, 'à gauche de O, l’ordre est retourné', 'varie', 's')
save(fig, '12-089')
