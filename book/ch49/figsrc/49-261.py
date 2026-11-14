import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
def panel(y, used, name, wire_role):
    # y: centre of panel; used: indices (0=a,1=b,2=c) of the two wires into AND, in port order
    labels = ['a', 'b', 'c']
    ys = [y + 12, y, y - 12]
    box(ax, 44, y - 8, 16, 16, 'sujet', label='ET', size='m')
    ports = [y + 4, y - 4]
    for i, yy in enumerate(ys):
        text(ax, 5, yy, labels[i], 'encre', 'm')
    for p, i in enumerate(used):
        line(ax, [(9, ys[i]), (30, ys[i]), (44, ports[p])], wire_role, lw=1.2)
    for i in range(3):
        if i not in used:
            line(ax, [(9, ys[i]), (30, ys[i])], 'fixe', lw=0.8, dash=True)
            ax.plot([32], [ys[i]], marker='x', color=COL['limite'], ms=3, zorder=4)
    arrow(ax, (60, y), (68, y), 'resultat', lw=1.2)
    text(ax, 69, y, name, 'resultat', 'm', ha='left')
panel(72, [0, 1], r'$f=a$ ET $b$', 'sujet')
panel(30, [1, 2], r'$g=b$ ET $c$', 'varie')
text(ax, 44, 52, 'même circuit, fils rebranchés', 'varie', 's')
save(fig, '49-261')
