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

fig, ax = canvas(80)
def nd(x, y, w, l, e=None): box(ax, x - w / 2, y - 3, w, 6, 'sujet', label=l, size='s')
def ed(p, q): line(ax, [(p[0], p[1] + 3), (q[0], q[1] - 3)], 'fixe', lw=0.9)
N = {'1': (16, 12), '2': (8, 28), '3': (24, 28), '4': (8, 44), '6': (24, 44), '12': (16, 60)}
for a, b in [('1', '2'), ('1', '3'), ('2', '4'), ('2', '6'), ('3', '6'), ('4', '12'), ('6', '12')]: ed(N[a], N[b])
for k, p in N.items(): nd(p[0], p[1], 9, k)
text(ax, 16, 72, 'diviseurs de 12', 'sujet', 's')
M = {'e': (44, 12, r'$\emptyset$'), 'a': (36, 36, r'$\{a\}$'), 'b': (52, 36, r'$\{b\}$'), 'ab': (44, 60, r'$\{a,b\}$')}
for a, b in [('e', 'a'), ('e', 'b'), ('a', 'ab'), ('b', 'ab')]: ed(M[a][:2], M[b][:2])
for k, p in M.items(): nd(p[0], p[1], 11, p[2])
T = [(72, 12, r'$\{0\}$'), (72, 36, 'droites'), (72, 60, 'plan')]
for p, q in zip(T, T[1:]): ed(p, q)
for p in T: nd(p[0], p[1], 14, p[2])
arrow(ax, (85.5, 14), (85.5, 58), 'varie')
save(fig, '80-029')
