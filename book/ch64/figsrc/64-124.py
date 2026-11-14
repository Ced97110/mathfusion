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

def cyc(*c):
    return {c[k]: c[(k + 1) % len(c)] for k in range(len(c))}

def square(f):
    return {k: f[f[k]] for k in f}

fig, ax = canvas(96)
ys = [84, 64, 44, 24, 4]
xs = [12 + 10 * k for k in range(5)]
# actions de droite à gauche : (1 2 3), (1 2 4)^2, (1 2 5), (1 2 3)^2
steps = [cyc(1, 2, 3), square(cyc(1, 2, 4)), cyc(1, 2, 5), square(cyc(1, 2, 3))]
st = tracks(ax, xs, ys, steps, {3: 'sujet', 4: 'varie', 5: 'autre'})
labs = [r'1. $(1\,2\,3)$', r'2. $(1\,2\,4)$ deux fois', r'3. $(1\,2\,5)$', r'4. $(1\,2\,3)$ deux fois']
for k, lab in enumerate(labs):
    text(ax, 64, (ys[k] + ys[k + 1]) / 2, lab, 'fixe', 's', ha='left')
text(ax, 64, 84, 'départ', 'fixe', 's', ha='left')
text(ax, 64, 4, r'$(3\,4\,5)$', 'resultat', 's', ha='left')
text(ax, 32, 91.5, '1 et 2 : même place', 'fixe', 's')
text(ax, 64, 9, '1 et 2 reviennent', 'fixe', 's', ha='left')
save(fig, '64-124')

