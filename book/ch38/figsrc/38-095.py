import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

# réseau : deux triangles qui partagent le côté PQ ; Rx = cote droit
NET = [(0, 0), (11, 0), (4, 9), (16, 8)]      # P, Q, R (au-dessus), S (au-dessus de PQ aussi)
def draw(ax, pts, role):
    P, Q, R, S = pts
    poly(ax, [P, Q, R], role)
    poly(ax, [Q, S, R], role)

def place(pts, ang, flip, o):
    a = math.radians(ang); out = []
    for x, y in pts:
        if flip: x = -x
        out.append((o[0] + x * math.cos(a) - y * math.sin(a), o[1] + x * math.sin(a) + y * math.cos(a)))
    return out

fig, ax = canvas(70)
draw(ax, place(NET, 0, False, (6, 38)), 'sujet')
draw(ax, place(NET, 50, False, (38, 30)), 'autre')
draw(ax, place(NET, 0, True, (80, 38)), 'autre')
text(ax, 14, 28, 'réseau', 'sujet', 's')
text(ax, 50, 56, 'tourné', 'autre', 's')
text(ax, 70, 28, 'retourné', 'autre', 's')
arrow(ax, (24, 49), (33, 50), 'varie', curve=-0.3)
text(ax, 44, 66, 'même réseau, autre position', 'encre', 'm')
text(ax, 44, 12, 'mêmes longueurs, mêmes angles', 'varie', 's')
text(ax, 44, 6, 'seule la position change', 'varie', 's')
save(fig, '38-095')
