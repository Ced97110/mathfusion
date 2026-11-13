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

fig, ax = canvas(68)
A_, B_, C_ = (44, 50), (24, 16), (64, 16)
poly(ax, [A_, B_, C_], 'fixe', fill=False, lw=1.2)
for p in (A_, B_, C_): disc(ax, p[0], p[1], 1.6, 'sujet')
def trio(cx, y, t):
    for i, d in enumerate(t): dig(ax, cx - 10.5 + 7.2 * i, y, d, 'varie' if d == '1' else 'fixe')
trio(44, 55, '100'); trio(24, 4, '010'); trio(64, 4, '001')
text(ax, 70, 38, 'un seul 1 par étiquette', 'varie', 's')
save(fig, '80-034')
