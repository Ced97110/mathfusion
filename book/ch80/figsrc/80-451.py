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

fig, ax = canvas(78); V, W_, Wp = 'sujet', 'varie', 'limite'
y = 58
ins, outs = series(ax, y, [(('$a$', '$b$'), (V, W_)), (('$a$', "$b'$"), (V, Wp))], cxs=(26, 58), xa=6, xb=82)
term(ax, 6, y); term(ax, 82, y)
text(ax, 44, 71, '4 interrupteurs', 'encre', 'm')
arrow(ax, (44, 46), (44, 35), 'varie', lw=1.4); text(ax, 48, 40.5, 'A3', 'varie', 'm', ha='left')
y = 22; term(ax, 6, y); term(ax, 82, y)
wire(ax, [(6, y), (14, y)]); wire(ax, [(14, y + 6), (14, y - 6)]); wire(ax, [(74, y + 6), (74, y - 6)]); wire(ax, [(74, y), (82, y)])
wire(ax, [(14, y + 6), (39.5, y + 6)]); sw(ax, 44, y + 6, '$a$', V); wire(ax, [(48.5, y + 6), (74, y + 6)])
wire(ax, [(14, y - 6), (29.5, y - 6)]); sw(ax, 34, y - 6, '$b$', W_); wire(ax, [(38.5, y - 6), (49.5, y - 6)])
sw(ax, 54, y - 6, "$b'$", Wp); wire(ax, [(58.5, y - 6), (74, y - 6)])
text(ax, 44, 6, '3 interrupteurs', 'encre', 'm')
save(fig, '80-451')
