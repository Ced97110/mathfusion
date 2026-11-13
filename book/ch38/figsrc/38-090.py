import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def sphere_pt(lon, lat):
    lo, la = math.radians(lon), math.radians(lat)
    return (math.cos(la) * math.sin(lo), math.sin(la), math.cos(la) * math.cos(lo))

def geodesic(p, q, n=30):
    d = sum(a * b for a, b in zip(p, q)); w = math.acos(d)
    out = []
    for i in range(n + 1):
        t = i / n
        c1 = math.sin((1 - t) * w) / math.sin(w); c2 = math.sin(t * w) / math.sin(w)
        out.append(tuple(c1 * a + c2 * b for a, b in zip(p, q)))
    return out

fig, ax = canvas(72)
# gauche : petit triangle plat
poly(ax, [(6, 16), (30, 16), (14, 40)], 'sujet')
text(ax, 18, 8, 'terrain de quelques km', 'sujet', 's')
text(ax, 18, 47, r'$180°$', 'sujet', 'm')
# droite : très grand triangle tracé sur une sphère (vue de face)
c, R = (62.0, 34.0), 22.0
disc(ax, c[0], c[1], R, 'fixe')
V = [sphere_pt(-34, -18), sphere_pt(34, -18), sphere_pt(0, 36)]
proj = lambda P: (c[0] + R * P[0], c[1] + R * P[1])
for i in range(3):
    seg = geodesic(V[i], V[(i + 1) % 3])
    line(ax, [proj(P) for P in seg], 'autre', lw=1.5)
fill = []
for i in range(3):
    fill += [proj(P) for P in geodesic(V[i], V[(i + 1) % 3])]
poly(ax, fill, 'autre')
for P in V:
    x, y = proj(P); disc(ax, x, y, 1.0, 'autre')
text(ax, 62, 8, 'très grand triangle', 'autre', 's')
text(ax, 62, 64, 'somme des angles > 180°', 'autre', 'm')
save(fig, '38-090')
