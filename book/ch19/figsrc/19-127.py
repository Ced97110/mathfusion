import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, ux, uy, x0, x1, y0, y1):
    arrow(ax, (ox + x0 * ux, oy), (ox + x1 * ux + 3, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy + y0 * uy), (ox, oy + y1 * uy + 3), "fixe", lw=0.8)
    return lambda x, y: (ox + x * ux, oy + y * uy)
fig, ax = canvas(64)
def panel(ox, head, dx, dy, c1, c2):
    P = plane(ax, ox, 12, 9, 9, 0, 4, 0, 4)
    line(ax, [P(0.2, 0.4), P(1.9, 3.8)], 'sujet', lw=1.6)
    line(ax, [P(0.8, 1.6), P(1.8, 1.6)], 'varie', lw=1.6); line(ax, [P(1.8, 1.6), P(1.8, 3.6)], 'varie', lw=1.6)
    text(ax, P(1.3, 1.6)[0], P(1.3, 1.6)[1] - 3, dx, 'varie', 's')
    text(ax, P(1.8, 2.6)[0] + 1.5, P(1.8, 2.6)[1], dy, 'varie', 's', ha='left')
    text(ax, ox + 18, 59, head, 'sujet', 's', weight='bold')
    text(ax, ox + 18, 52, c1, 'resultat', 'm', weight='bold')
panel(4, 'prix : € par cahier', '+1 cahier', '+2 €', 'pente 2', '')
panel(48, 'vitesse : km par heure', '+1 h', '+60 km', 'pente 60', '')
save(fig, '19-127')
