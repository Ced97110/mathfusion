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

fig, ax = canvas(84)
text(ax, 44, 79, r'tout 3-cycle est un produit de $(i\,j\,a)$', 'encre', 's')
rows = [(r'contient $i$ et $j$', r'$(i\,j\,a)^2$'), (r'contient $i$, pas $j$', r'$(i\,j\,b)(i\,j\,a)^2$'),
        (r'contient $j$, pas $i$', r'$(i\,j\,b)^2(i\,j\,a)$'), (r'ni $i$ ni $j$', r'$(i\,j\,a)^2(i\,j\,c)(i\,j\,b)^2(i\,j\,a)$')]
for k, (c, r) in enumerate(rows):
    y = 58 - k * 17
    box(ax, 2, y - 6, 30, 12, 'sujet', label=c, size='s')
    arrow(ax, (32.5, y), (40, y), 'varie')
    box(ax, 40.5, y - 6, 45.5, 12, 'resultat', label=r, size='s')
save(fig, '64-120')
