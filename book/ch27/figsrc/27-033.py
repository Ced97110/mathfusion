import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
K = 4.0
def tri(ox, oy, a, b, c, role, flip=False):
    """Triangle de côtés a (base), b, c ; sommet gauche en (ox, oy)."""
    cx = (a * a + b * b - c * c) / (2 * a); cy = math.sqrt(b * b - cx * cx)
    pts = [(ox, oy), (ox + a * K, oy), (ox + cx * K, oy + cy * K)]
    if flip: pts = [(2 * ox + a * K - x, y) for x, y in pts]
    poly(ax, pts, role)
    return pts
def sides(pts, vals, role):
    cen = (sum(p[0] for p in pts) / 3, sum(p[1] for p in pts) / 3)
    for (p, q), v in zip([(0, 1), (1, 2), (2, 0)], vals):
        mx, my = (pts[p][0] + pts[q][0]) / 2, (pts[p][1] + pts[q][1]) / 2
        d = math.hypot(mx - cen[0], my - cen[1]); k = 2.6 / d
        text(ax, mx + (mx - cen[0]) * k, my + (my - cen[1]) * k, v, role, 's')
# gauche : 3, 4, 5 et 3, 4, 5
p1 = tri(6, 30, 4, 3, 5, 'sujet'); sides(p1, ['4', '5', '3'], 'sujet')
p2 = tri(6, 6, 4, 3, 5, 'sujet', flip=True); sides(p2, ['4', '3', '5'], 'sujet')
text(ax, 22, 56, '3 côtés égaux : même forme', 'resultat', 's')
line(ax, [(44, 2), (44, 52)], 'fixe', 0.6, dash=True)
# droite : 3, 4, 5 et 3, 4, 6
q1 = tri(52, 30, 4, 3, 5, 'sujet'); sides(q1, ['4', '5', '3'], 'sujet')
q2 = tri(52, 6, 4, 3, 6, 'limite'); sides(q2, ['4', '6', '3'], 'limite')
text(ax, 66, 56, '2 côtés égaux : pas assez', 'limite', 's')
save(fig, '27-033')
