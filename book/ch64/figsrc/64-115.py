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

fig, ax = canvas(60)
ys = [52, 30, 8]
xs = [26, 42]
tracks(ax, xs, ys, [{1: 2, 2: 1}, {1: 2, 2: 1}], {1: 'sujet', 2: 'autre'}, True)
text(ax, 56, 52, 'départ', 'encre', 's', ha='left')
text(ax, 56, 41, 'échange de 1 et 2', 'varie', 's', ha='left')
text(ax, 56, 19, 'encore 1 et 2', 'varie', 's', ha='left')
text(ax, 56, 8, '= identité', 'resultat', 's', ha='left')
save(fig, '64-115')
