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

fig, ax = canvas(58)
text(ax, 9, 36, 'avant', 'encre', 'm'); text(ax, 9, 12, 'après', 'encre', 'm')
c1 = (28, 52, 76); R1 = [(r'$a\vee b$', 'sujet'), (r'$a\vee b$', 'sujet'), (r"$a\vee b'$", 'autre')]
for c, (l, r) in zip(c1, R1): box(ax, c - 10, 32, 20, 8, r, label=l)
for xx in (40, 64): text(ax, xx, 36, r'$\wedge$', 'encre', 'l')
brace(ax, 18, 62, 41.5, 'sujet', down=False, label='deux blocs identiques')
box(ax, 30, 8, 20, 8, 'sujet', label=r'$a\vee b$'); box(ax, 66, 8, 20, 8, 'autre', label=r"$a\vee b'$")
text(ax, 58, 12, r'$\wedge$', 'encre', 'l')
arrow(ax, (28, 32), (36, 16.5), 'varie'); arrow(ax, (52, 32), (44, 16.5), 'varie'); arrow(ax, (76, 32), (76, 16.5), 'fixe')
text(ax, 60, 24, r'$x\wedge x=x$', 'varie', 'm'); text(ax, 77.5, 24, 'reste', 'fixe', 's', ha='left')
save(fig, '80-450')
