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

fig, ax = canvas(86)
T = ['100 110 010', '100 101 001', '010 011 001', '100 111 011', '010 111 101', '001 111 110', '110 101 011']
R = ['fixe'] * 3 + ['sujet'] * 3 + ['varie']
text(ax, 72, 82, '3 points', 'resultat', 's')
for i, (t, r) in enumerate(zip(T, R)):
    y = 74 - 9 * i
    line(ax, [(22, y), (30, y)], r, lw=1.8); box(ax, 34, y - 3.2, 24, 6.4, r, label=t, size='s')
    for x in (66, 72, 78): disc(ax, x, y, 1.6, 'resultat')
text(ax, 3, 65, 'côtés', 'fixe', 's', ha='left'); text(ax, 3, 38, 'médianes', 'sujet', 's', ha='left'); text(ax, 3, 20, 'cercle', 'varie', 's', ha='left')
save(fig, '80-038')
