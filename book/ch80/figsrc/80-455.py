import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def sw(ax, cx, cy, lab, role='sujet', w=9, h=5, dash=False, fill=True):
    box(ax, cx - w / 2, cy - h / 2, w, h, role, fill=fill, label=lab, size='m', dash=dash, r=0.6)

def wire(ax, pts, role='fixe', lw=1.0):
    line(ax, pts, role, lw=lw)

def term(ax, x, y, lab=None, dy=-3.8):
    disc(ax, x, y, 1.1, 'encre')
    if lab: text(ax, x, y + dy, lab, 'encre', 'm')

def par_block(ax, cx, y, labs, roles, w=9, off=5.2, half=8):
    for i, (l, r) in enumerate(zip(labs, roles)):
        yy = y + off if i == 0 else y - off
        sw(ax, cx, yy, l, r, w)
        wire(ax, [(cx - half, yy), (cx - w / 2, yy)]); wire(ax, [(cx + w / 2, yy), (cx + half, yy)])
    wire(ax, [(cx - half, y + off), (cx - half, y - off)]); wire(ax, [(cx + half, y + off), (cx + half, y - off)])
    return cx - half, cx + half

def series(ax, y, specs, cxs=(18, 44, 70), xa=4, xb=84, **kw):
    ins, outs = [], []
    for cx, (labs, roles) in zip(cxs, specs):
        i, o = par_block(ax, cx, y, labs, roles, **kw); ins.append(i); outs.append(o)
    wire(ax, [(xa, y), (ins[0], y)])
    for o, i in zip(outs, ins[1:]): wire(ax, [(o, y), (i, y)])
    wire(ax, [(outs[-1], y), (xb, y)])
    return ins, outs

AB = ('$a$', "$b$")
def m3(ax, cx, cy, dx=15, dy=12, r=3.3, roles=None):
    roles = roles or dict(x='sujet', y='varie', z='autre')
    P = {'0': (cx, cy - dy), '1': (cx, cy + dy), 'x': (cx - dx, cy), 'y': (cx, cy), 'z': (cx + dx, cy)}
    def cut(p, q):
        d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
        return (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r)
    for m in 'xyz':
        for e in '01':
            a, b = cut(P[e], P[m]); line(ax, [a, b], 'fixe', lw=1.0)
    for k, p in P.items():
        disc(ax, p[0], p[1], r, roles.get(k, 'fixe'), label=f'${k}$', size='m')
    return P

import itertools
fig, ax = canvas(64)
H = ['$a$', '$b$', "$b'$", r'$a\vee b$', r"$a\vee b'$", r'$a\vee b$', 'lampe']
cw, pitch = 9.6, 10.8
X = [4 + i * pitch + (2.5 if i >= 3 else 0) + (2.5 if i >= 6 else 0) for i in range(7)]
for x, h in zip(X, H): text(ax, x + cw / 2, 47.5, h, 'encre', 's')
for k in range(3): text(ax, X[3 + k] + cw / 2, 54, f'bloc {k + 1}', 'sujet', 's')
text(ax, X[6] + cw / 2, 54, 'résultat', 'resultat', 's', weight='bold')
for r, (a, b) in enumerate(itertools.product((0, 1), repeat=2)):
    bp = 1 - b; b1 = a | b; b2 = a | bp; b3 = a | b; lamp = b1 & b2 & b3
    y = 40 - 8.6 * r
    for x, v in zip(X, (a, b, bp, b1, b2, b3, lamp)):
        box(ax, x, y - 3.5, cw, 7, 'resultat' if v else 'fixe', label=str(v), size='m', lw=1.8 if x == X[6] else 0.8, weight='bold' if x == X[6] else 'normal')
text(ax, 4, 8, '1 : fermé, ou allumée', 'encre', 's', ha='left'); text(ax, 4, 3.4, '0 : ouvert, ou éteinte', 'encre', 's', ha='left')
save(fig, '80-455')
