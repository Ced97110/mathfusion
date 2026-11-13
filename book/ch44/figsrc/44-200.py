import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def sq(cx, cy, s, p):
    h = s / 2
    poly(ax, [(cx-h, cy-h), (cx+h, cy-h), (cx+h, cy+h), (cx-h, cy+h)], 'fixe')
    dx, dy = [(-1, -1), (1, -1), (1, 1), (-1, 1)][p]
    ax.add_patch(Circle((cx + dx * h * 0.55, cy + dy * h * 0.55), 1.5, fc=COL['sujet'], ec=COL['sujet'], zorder=4))
text(ax, 22, 57, 'abélien', 'resultat', 'm'); text(ax, 66, 57, 'non abélien', 'limite', 'm')
box(ax, 2, 38, 17, 10, 'sujet', label='3 + 5'); box(ax, 25, 38, 17, 10, 'autre', label='5 + 3')
text(ax, 22, 43, '=', 'resultat', 'l')
box(ax, 14, 18, 16, 10, 'resultat', label='8', size='l')
arrow(ax, (10.5, 37.5), (17, 28.5), 'fixe'); arrow(ax, (33.5, 37.5), (27, 28.5), 'fixe')
box(ax, 46, 38, 17, 10, 'sujet', label='r puis s'); box(ax, 69, 38, 17, 10, 'autre', label='s puis r')
text(ax, 66, 43, r'$\neq$', 'limite', 'l')
sq(54.5, 25, 11, 2); sq(77.5, 25, 11, 0)
arrow(ax, (54.5, 37.5), (54.5, 31.5), 'fixe'); arrow(ax, (77.5, 37.5), (77.5, 31.5), 'fixe')
text(ax, 54.5, 14, 'coin 1 en 3', 'limite', 's'); text(ax, 77.5, 14, 'coin 1 en 1', 'limite', 's')
save(fig, '44-200')
