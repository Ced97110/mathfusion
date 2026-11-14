import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import itertools, math
_T = [(1,2,4),(2,3,5),(3,4,6),(4,5,7),(5,6,1),(6,7,2),(7,1,3)]
_LINES = [(0,3,1),(1,4,2),(2,5,0),(0,6,4),(1,6,5),(2,6,3),(3,4,5)]
def _assign():
    for perm in itertools.permutations(range(1, 8)):
        if {perm[0], perm[3], perm[1]} != {1, 2, 4}: continue
        if all(any({perm[a] for a in L} == set(t) for L in _LINES) for t in _T): return perm
_PERM = _assign()
def fano_pos(cx, cy, R):
    V = [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in (90, 210, 330)]
    mid = lambda p, q: ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    pts = V + [mid(V[0], V[1]), mid(V[1], V[2]), mid(V[2], V[0]), (cx, cy)]
    return {_PERM[i]: pts[i] for i in range(7)}, pts
def _arr(ax, p, q, role='varie', rad=0.0, lw=1.0):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle='-|>', mutation_scale=7, lw=lw, color=COL[role],
                 connectionstyle=f'arc3,rad={rad}', zorder=4, shrinkA=5.5, shrinkB=5.5))
def fano(ax, cx, cy, R, hi=(), arrows='all', labels=True, roles=None):
    P, pts = fano_pos(cx, cy, R)
    roles = roles or {}
    lines = {}
    for L in _LINES:
        lines[frozenset(_PERM[a] for a in L)] = L
    hiset = {frozenset(t) for t in hi}
    def draw_line(L, role, lw):
        if L == (3, 4, 5):
            ax.add_patch(Circle((cx, cy), R / 2, ec=COL[role], fc='none', lw=lw, zorder=1.5 if role != 'fixe' else 1))
        else:
            line(ax, [pts[L[0]], pts[L[2]]], role, lw=lw)
    for key, L in lines.items():
        if key not in hiset: draw_line(L, 'fixe', 0.8)
    for key, L in lines.items():
        if key in hiset: draw_line(L, 'sujet', 1.4)
    for t in _T:
        key = frozenset(t); L = lines[key]
        if arrows == 'none' or (arrows == 'hi' and key not in hiset): continue
        nxt = {t[0]: t[1], t[1]: t[2], t[2]: t[0]}
        labs = [_PERM[a] for a in L]
        if L == (3, 4, 5):
            s = sorted(labs, key=lambda l: math.atan2(P[l][1] - cy, P[l][0] - cx))
            fwd = nxt[s[0]] == s[1]
            seq = s if fwd else s[::-1]
            for i in range(3):
                _arr(ax, P[seq[i]], P[seq[(i + 1) % 3]], rad=0.577 if fwd else -0.577)
            if not fwd: pass
        else:
            dx, dy = pts[L[2]][0] - pts[L[0]][0], pts[L[2]][1] - pts[L[0]][1]
            s = sorted(labs, key=lambda l: P[l][0] * dx + P[l][1] * dy)
            fwd = nxt[s[0]] == s[1]
            n = math.hypot(dx, dy); off = 1.8 if arrows == 'hi' else 0.0
            ox, oy = -dy / n * off, dx / n * off
            sh = lambda q: (q[0] + ox, q[1] + oy)
            if fwd: _arr(ax, sh(P[s[0]]), sh(P[s[1]])); _arr(ax, sh(P[s[1]]), sh(P[s[2]]))
            else: _arr(ax, sh(P[s[1]]), sh(P[s[0]])); _arr(ax, sh(P[s[2]]), sh(P[s[1]]))
    for i in range(7):
        l = _PERM[i]; x, y = pts[i]
        rr = roles.get(l, 'resultat')
        ax.add_patch(Circle((x, y), 1.7, ec=COL[rr], fc=FILL[rr], lw=0.8, zorder=4.6))
        if labels:
            if i == 6: tx, ty = x + 3.6, y - 0.6
            else:
                d = math.hypot(x - cx, y - cy); tx, ty = x + (x - cx) / d * 3.6, y + (y - cy) / d * 3.6
            t = text(ax, tx, ty, r'$e_{%d}$' % l, 'encre', 's')
            if i == 6: t.set_bbox(dict(fc='white', ec='none', pad=0.3))
    return P
fig, ax = canvas(70)
text(ax, 21, 62, 'plan ordinaire', 'encre', 'm'); text(ax, 21, 57, 'infinité de points', 'fixe', 's')
pts = [(7 + 7 * i, 18 + 7 * j) for i in range(5) for j in range(5)]
line(ax, [(4, 24), (38, 41)], 'sujet', lw=1.4)
for (x, y) in pts:
    role = 'varie' if (x, y) in ((7 + 7 * 0, 25), (7 + 7 * 4, 39)) else 'fixe'
    disc(ax, x, y, 1.5 if role == 'varie' else 0.9, role)
text(ax, 66, 62, 'plan de Fano', 'encre', 'm'); text(ax, 66, 57, '7 points, 7 droites', 'fixe', 's')
fano(ax, 66, 31, 19, hi=[(1, 2, 4)], arrows='none', roles={1: 'varie', 2: 'varie'})
text(ax, 44, 5, 'deux points : une seule droite', 'sujet', 's')
save(fig, '78-139')
