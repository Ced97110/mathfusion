import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def width(s):
    t = ax.text(0, 0, s, fontsize=SIZE['xl'])
    fig.canvas.draw()
    bb = t.get_window_extent()
    (a, _), (b, _) = ax.transData.inverted().transform([(bb.x0, 0), (bb.x1, 0)])
    t.remove()
    return b - a
def word(y, s, k, role):
    w = width(s)
    x = 44 - w / 2
    text(ax, x, y, s, role, 'xl', ha='left')
    cx = x + (width(s[:k]) + width(s[:k + 1])) / 2 - 1.6
    box(ax, cx - 2.8, y - 5, 5.6, 10, 'varie', fill=False, lw=1.0)
    return cx
text(ax, 3, 58, 'Léa envoie', 'sujet', 'm', ha='left')
cx1 = word(48, 'DOJHEUH', 4, 'sujet')
text(ax, 3, 28, 'Hugo reçoit', 'sujet', 'm', ha='left')
cx2 = word(18, 'DOJHFUH', 4, 'sujet')
arrow(ax, (cx1, 42.5), (cx2, 23.5), 'varie')
text(ax, cx1 + 7, 33, 'bruit', 'varie', 'm', ha='left')
text(ax, 44, 8, 'aucun espion : le message a changé', 'encre', 's')
text(ax, 44, 3, 'Hugo ne sait pas quelle lettre', 'encre', 's')
save(fig, '53-192')
