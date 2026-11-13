import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
SQ3 = math.sqrt(3)
OFF = {'100': (0, 3.4), '010': (0, -3.4), '001': (0, -3.4), '110': (-4.8, 0.6), '101': (4.8, 0.6), '011': (0, -3.4), '111': (3.8, -2.6)}
def fano(ax, cx, y0, s, lines=None, pts=None, names=None, inner=None, pr=1.3):
    A = (cx, y0 + s * SQ3 / 2); B = (cx - s / 2, y0); C = (cx + s / 2, y0)
    mid = lambda p, q: ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    G = (cx, y0 + s * SQ3 / 6)
    P = {'100': A, '010': B, '001': C, '110': mid(A, B), '101': mid(A, C), '011': mid(B, C), '111': G}
    ends = {'AB': (A, B), 'AC': (A, C), 'BC': (B, C), 'mA': (A, P['011']), 'mB': (B, P['101']), 'mC': (C, P['110'])}
    lines = lines or {}
    for n, (p, q) in ends.items():
        v = lines.get(n, ('fixe', 0.7))
        if v is None: continue
        line(ax, [p, q], v[0], lw=v[1], dash=len(v) > 2 and v[2])
    v = lines.get('O', ('fixe', 0.7))
    if v is not None:
        ax.add_patch(Circle(G, s * SQ3 / 6, fill=False, ec=COL[v[0]], lw=v[1], ls='--' if len(v) > 2 and v[2] else '-', zorder=3))
    pts = pts or {}
    for k, p in P.items():
        r = pts.get(k, 'fixe')
        ax.add_patch(Circle(p, pr, ec=COL[r], fc=FILL[r], lw=0.8, zorder=4))
    for k, t in (inner or {}).items():
        r = pts.get(k, 'fixe')
        ax.add_patch(Circle(P[k], 2.4, ec=COL[r], fc=FILL[r], lw=0.8, zorder=4)); text(ax, P[k][0], P[k][1], t, r, 's')
    for k, v in (names or {}).items():
        t, r = (k, v) if isinstance(v, str) else v
        text(ax, P[k][0] + OFF[k][0], P[k][1] + OFF[k][1], t, r, 's')
    return P
def sw(ax, x, y, closed, role, label=None, dy=-5.2):
    disc(ax, x - 5, y, 0.9, 'fixe'); disc(ax, x + 5, y, 0.9, role)
    line(ax, [(x - 5, y), (x + 5, y)] if closed else [(x - 5, y), (x + 3.2, y + 4.5)], role, lw=1.6)
    if label: text(ax, x, y + dy, label, role, 'm')
def dig(ax, x, y, ch, role, w=6.5):
    box(ax, x, y, w, 6.5, role, label=ch)

fig, ax = canvas(54)
text(ax, 44, 48, 'même lettre : même état', 'encre', 'l')
xs = [9, 23, 37, 51, 65, 79]; labs = [r'$a$'] * 3 + [r'$b$'] * 2 + [r"$b'$"]; rl = ['fixe'] * 3 + ['varie'] * 2 + ['sujet']
for x, l, r, c in zip(xs, labs, rl, [True] * 5 + [False]): sw(ax, x, 34, c, r, l)
line(ax, [(51, 38.5), (51, 40.5), (65, 40.5), (65, 38.5)], 'varie')
brace(ax, 4, 42, 24, 'fixe', r'3 fois $a$'); brace(ax, 46, 70, 24, 'varie', r'2 fois $b$'); brace(ax, 74, 84, 24, 'sujet', r"1 fois $b'$")
save(fig, '80-026')
