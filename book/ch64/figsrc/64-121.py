import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tracks(ax, xs, ys, fs, hl, lab_mid=False):
    n = len(xs); st = [{s: s for s in range(1, n + 1)}]
    for f in fs: st.append({s: f.get(p, p) for s, p in st[-1].items()})
    for s in range(1, n + 1):
        for t in range(len(ys) - 1):
            x0, y0 = xs[st[t][s] - 1], ys[t]; x1, y1 = xs[st[t + 1][s] - 1], ys[t + 1]
            d = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / d, (y1 - y0) / d
            a = 2.9 if (t == 0 or lab_mid) else 1.0; b = 2.9 if (t == len(ys) - 2 or lab_mid) else 1.0
            line(ax, [(x0 + ux * a, y0 + uy * a), (x1 - ux * b, y1 - uy * b)], hl.get(s, "fixe"), lw=1.8 if s in hl else 0.8)
    for t in range(len(ys)):
        for s in range(1, n + 1):
            x = xs[st[t][s] - 1]; role = hl.get(s, "fixe")
            if t in (0, len(ys) - 1) or lab_mid: disc(ax, x, ys[t], 2.6, role, label=str(s), size="s")
            else: disc(ax, x, ys[t], 1.0, role)
    return st

fig, ax = canvas(62)
R = 10
def tri(cx, cy):
    return [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in (90, -30, 210)]
def seg(P, i, j, role, lw=1.2):
    (x0, y0), (x1, y1) = P[i], P[j]
    d = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / d, (y1 - y0) / d
    arrow(ax, (x0 + ux * 3.4, y0 + uy * 3.4), (x1 - ux * 3.4, y1 - uy * 3.4), role, lw=lw)
L = tri(20, 32); Rr = tri(68, 32)
for P, role in ((L, 'sujet'), (Rr, 'resultat')):
    for p, n in zip(P, (1, 2, 3)): disc(ax, p[0], p[1], 2.8, role, label=str(n), size='s')
seg(L, 0, 1, 'varie', 1.6); seg(L, 1, 2, 'varie', 1.6); seg(L, 2, 0, 'sujet')
seg(Rr, 0, 2, 'resultat', 1.6); seg(Rr, 2, 1, 'resultat'); seg(Rr, 1, 0, 'resultat')
text(ax, 44, 32, '=', 'encre', 'xl')
text(ax, 20, 52, r'$(1\,2\,3)$ deux fois', 'sujet', 's')
text(ax, 68, 52, r'$(1\,3\,2)$', 'resultat', 's')
text(ax, 20, 11, '1 va en 2, puis en 3', 'varie', 's')
text(ax, 68, 11, '1 va en 3', 'resultat', 's')
save(fig, '64-121')
