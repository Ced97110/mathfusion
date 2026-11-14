import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def row(y, closed, labx, note, labs):
    f = numberline(ax, 8, 62, y, 0, 4, labels=labs, arrow_right=False)
    arrow(ax, (f(2), y), (84, y), 'sujet', lw=2.2)
    ax.add_patch(Circle((f(2), y), 1.9, ec=COL['sujet'], fc=COL['sujet'] if closed else 'white', lw=1.2, zorder=4))
    text(ax, 24, y + 15, labx, 'sujet', 'l')
    text(ax, f(2), y + 8, note, 'resultat' if closed else 'limite', 's')
    return f
f = row(54, False, r'$x > 2$', 'vide : 2 ne convient pas', True)
g = row(20, True, r'$x \geq 2$', 'plein : 2 convient', False)
text(ax, g(2), 12.5, '2', 'sujet', 's')
save(fig, '17-014')
