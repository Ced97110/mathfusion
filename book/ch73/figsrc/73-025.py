import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 6.5; oy = 14
def axes(ox, w):
    line(ax, [(ox - 5, oy), (ox + w, oy)], 'fixe', lw=0.5)
    line(ax, [(ox, oy - 2), (ox, oy + 2.8 * u)], 'fixe', lw=0.5)
def dot(x, y, role):
    ax.add_patch(Circle((x, y), 1.0, fc=COL[role], ec=COL[role], zorder=6))
# gauche : cisaillement, se défait
ox = 7; axes(ox, 30)
a = (ox + 2 * u, oy + 2 * u); b = (ox + 4 * u, oy + 2 * u)
dot(*a, 'sujet'); dot(*b, 'varie')
arrow(ax, (a[0] + 1.5, a[1] + 1.5), (b[0] - 1.5, b[1] + 1.5), 'varie', curve=-0.5)
arrow(ax, (b[0] - 1.5, b[1] - 1.5), (a[0] + 1.5, a[1] - 1.5), 'resultat', curve=-0.5)
text(ax, a[0], a[1] + 6.5, '(2, 2)', 'sujet', 's')
text(ax, b[0] + 1, b[1] + 6.5, '(4, 2)', 'varie', 's')
text(ax, 22, 46, 'cisaillement', 'resultat', 's')
text(ax, 22, 5.5, 'on revient : réversible', 'resultat', 's')
# droite : écrasement, ne se défait pas
ox = 57; axes(ox, 28)
p2 = (ox + 3 * u, oy + 2 * u); p1 = (ox + 3 * u, oy + 1 * u); p0 = (ox + 3 * u, oy)
dot(*p2, 'sujet'); dot(*p1, 'sujet'); dot(*p0, 'limite')
arrow(ax, (p2[0] + 1.2, p2[1] - 1.2), (p0[0] + 1.2, p0[1] + 1.4), 'limite', curve=-0.6)
arrow(ax, (p1[0], p1[1] - 1.4), (p0[0], p0[1] + 1.4), 'limite')
text(ax, p2[0] - 9, p2[1] + 0.5, '(3, 2)', 'sujet', 's')
text(ax, p1[0] - 9, p1[1] - 1.5, '(3, 1)', 'sujet', 's')
text(ax, p0[0] + 8, p0[1] - 3.4, '(3, 0)', 'limite', 's')
text(ax, 66, 46, 'écrasement', 'limite', 's')
text(ax, 66, 5.5, 'quel départ ? on ne sait pas', 'limite', 's') if False else text(ax, 68, 5.5, 'deux départs : impossible', 'limite', 's')
save(fig, '73-025')
