import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
def row(y, expr, vpt, labp, note, rolep):
    f = numberline(ax, 8, 66, y, -4, 5, labels=False, arrow_right=False)
    arrow(ax, (f(vpt), y), (84, y), 'sujet', lw=2.2)
    ax.add_patch(Circle((f(vpt), y), 1.9, ec=COL['sujet'], fc='white', lw=1.2, zorder=4))
    text(ax, f(vpt), y - 5, labp, rolep, 's')
    text(ax, 24, y + 14, expr, 'sujet', 'l')
    text(ax, 66, y + 14, note, 'fixe', 's')
    return f
row(58, r'$x > 2$', 2, '2', 'point sur le 2 écrit', 'sujet')
f = row(20, r'$x + 7 > 4$', -3, '−3', 'point sur −3, pas 4', 'varie')
text(ax, f(4), 14, '4', 'fixe', 's')
save(fig, '17-016')
