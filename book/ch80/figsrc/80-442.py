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
fig, ax = canvas(60)
pos = list(itertools.product((1, 0), repeat=3))[::-1]
x0, p, s = 26, 7.6, 5.4
text(ax, 54, 55, 'les 8 positions', 'encre', 'm')
rows = {'a': 47, 'b': 40, 'c': 33}
for name, yy in rows.items(): text(ax, 12, yy, f'${name}$', 'encre', 'm')
text(ax, 12, 21, 'haut', 'encre', 's'); text(ax, 12, 12, 'bas', 'encre', 's')
npass = 0
for i, (a, b, c) in enumerate(pos):
    cx = x0 + i * p
    for v, name in zip((a, b, c), 'abc'):
        yy = rows[name]
        box(ax, cx - s / 2, yy - s / 2, s, s, 'sujet' if v else 'fixe', fill=bool(v), r=0.5)
    ok = a and (b or c); npass += bool(ok)
    for yy in (21, 12): disc(ax, cx, yy, 2.5, 'resultat' if ok else 'fixe', fill=bool(ok))
box(ax, 4, 2.2, 4, 4, 'sujet', r=0.4); text(ax, 10, 4.2, 'fermé', 'sujet', 's', ha='left')
box(ax, 26, 2.2, 4, 4, 'fixe', fill=False, r=0.4); text(ax, 32, 4.2, 'ouvert', 'fixe', 's', ha='left')
disc(ax, 52, 4.2, 2, 'resultat'); text(ax, 56, 4.2, f'passe : {npass} sur 8', 'resultat', 's', ha='left')
save(fig, '80-442')
