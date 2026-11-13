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

fig, ax = canvas(76); ya, yb, ym = 58, 18, 38
A_, B_, C_ = 'sujet', 'varie', 'resultat'
term(ax, 5, ym, 'A'); term(ax, 83, ym, 'B')
wire(ax, [(5, ym), (9, ym)]); wire(ax, [(79, ym), (83, ym)])
wire(ax, [(9, ya), (9, yb)]); wire(ax, [(79, ya), (79, yb)])
# haut : a puis (b | c)
wire(ax, [(9, ya), (17.5, ya)]); sw(ax, 22, ya, '$a$', A_)
wire(ax, [(26.5, ya), (32, ya)]); wire(ax, [(32, ya + 5.5), (32, ya - 5.5)])
for yy, l, r in ((ya + 5.5, '$b$', B_), (ya - 5.5, '$c$', C_)):
    wire(ax, [(32, yy), (39.5, yy)]); sw(ax, 44, yy, l, r); wire(ax, [(48.5, yy), (56, yy)])
wire(ax, [(56, ya + 5.5), (56, ya - 5.5)]); wire(ax, [(56, ya), (79, ya)])
# bas : (a, b) | (a, c)
wire(ax, [(9, yb), (13, yb)]); wire(ax, [(13, yb + 5.5), (13, yb - 5.5)])
for yy, l, r in ((yb + 5.5, '$b$', B_), (yb - 5.5, '$c$', C_)):
    wire(ax, [(13, yy), (17.5, yy)]); sw(ax, 22, yy, '$a$', A_); wire(ax, [(26.5, yy), (35.5, yy)])
    sw(ax, 40, yy, l, r); wire(ax, [(44.5, yy), (56, yy)])
wire(ax, [(56, yb + 5.5), (56, yb - 5.5)]); wire(ax, [(56, yb), (79, yb)])
text(ax, 44, 70.5, r'$a\wedge(b\vee c)$', 'encre', 'l'); text(ax, 44, 4, r'$(a\wedge b)\vee(a\wedge c)$', 'encre', 'l')
save(fig, '80-446')
