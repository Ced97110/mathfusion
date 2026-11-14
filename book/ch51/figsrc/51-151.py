import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

FS = ' '  # figure space: same width as a digit

def mat(ax, cx, cy, rows, role='sujet', size='m', n=2, sep=2, ls=2.2, col_roles=None, d=1):
    """Matrix drawn as aligned text with brackets. Returns (cell(i, j) -> (x, y), (x0, x1, y0, y1))."""
    fs = SIZE[size] * 25.4 / 72
    cw = 0.636 * fs
    px = (n + sep) * cw
    py = 1.05 * fs * (0.767 * ls + 0.194)
    nr, nc = len(rows), len(rows[0])
    cell = lambda i, j: (cx + (j - (nc - 1) / 2) * px, cy + ((nr - 1) / 2 - i) * py)
    fmt = lambda v: str(v).replace('-', '−').rjust(n, FS)
    if col_roles is None:
        t = text(ax, cx - (n - d) * cw / 2, cy, '\n'.join((FS * sep).join(fmt(v) for v in r) for r in rows), role, size)
        t.set_linespacing(ls)
    else:
        for j in range(nc):
            t = text(ax, cell(0, j)[0] - (n - d) * cw / 2, cy, '\n'.join(fmt(r[j]) for r in rows), col_roles[j], size)
            t.set_linespacing(ls)
    w = (nc - 1) * px + n * cw + 2.4
    h = nr * py + 0.6
    x0, x1, y0, y1 = cx - w / 2, cx + w / 2, cy - h / 2, cy + h / 2
    for xs, d in ((x0, 1.2), (x1, -1.2)):
        line(ax, [(xs + d, y1), (xs, y1), (xs, y0), (xs + d, y0)], role, lw=0.9)
    return cell, (x0, x1, y0, y1)

def hl(ax, x0, x1, y0, y1, role='varie'):
    """Dashed highlight frame."""
    box(ax, x0, y0, x1 - x0, y1 - y0, role, fill=False, lw=1.0, r=0.6, dash=True)

fig, ax = canvas(78)
u = 14.0; ox, oy = 28.0, 12.0
P = lambda x, y: (ox + x * u, oy + y * u)
S = lambda p: (2 * p[0], p[1])
R = lambda p: (-p[1], p[0])
p0 = (1.5, 0.5)
assert S(p0) == (3.0, 0.5) and R(S(p0)) == (-0.5, 3.0)
assert R(p0) == (-0.5, 1.5) and S(R(p0)) == (-1.0, 1.5)
arrow(ax, (ox - 18, oy), (ox + 46, oy), 'fixe', lw=0.6)
arrow(ax, (ox, oy - 5), (ox, oy + 52), 'fixe', lw=0.6)
def step(a, b, role, curve=0.0):
    pa, pb = P(*a), P(*b)
    d = math.hypot(pb[0] - pa[0], pb[1] - pa[1])
    k = 1.8 / d
    arrow(ax, (pa[0] + (pb[0] - pa[0]) * k, pa[1] + (pb[1] - pa[1]) * k),
          (pb[0] - (pb[0] - pa[0]) * k, pb[1] - (pb[1] - pa[1]) * k), role, lw=1.0, curve=curve)
# wrong reading : S then R
step(p0, S(p0), 'limite'); step(S(p0), R(S(p0)), 'limite')
# right reading : R then S
step(p0, R(p0), 'resultat'); step(R(p0), S(R(p0)), 'resultat')
disc(ax, *P(*p0), 1.4, 'fixe')
disc(ax, *P(*S(p0)), 1.2, 'limite')
disc(ax, *P(*R(p0)), 1.2, 'resultat')
disc(ax, *P(*R(S(p0))), 1.6, 'limite')
disc(ax, *P(*S(R(p0))), 1.6, 'resultat')
text(ax, P(*p0)[0] - 1, P(*p0)[1] - 4.2, r'$u\ (1{,}5\ ;\ 0{,}5)$', 'fixe', 's')
text(ax, P(*S(p0))[0] + 1, P(*S(p0))[1] + 3.6, r'$(3\ ;\ 0{,}5)$', 'limite', 's', ha='left')
text(ax, P(*R(S(p0)))[0] + 3, P(*R(S(p0)))[1] + 3.2, r'$(-0{,}5\ ;\ 3)$', 'limite', 's', ha='left')
text(ax, P(*S(R(p0)))[0] - 2, P(*S(R(p0)))[1] - 4, r'$(-1\ ;\ 1{,}5)$', 'resultat', 's', ha='right')
text(ax, 86, 72, 'S d’abord, puis R : pas SR', 'limite', 's', ha='right')
text(ax, 86, 66.5, 'SR : R d’abord, puis S', 'resultat', 's', ha='right')
text(ax, 36, 21.6, '1 : R', 'resultat', 's')
text(ax, 17.5, 36.5, '2 : S', 'resultat', 's')
text(ax, 61, 15.8, '1 : S', 'limite', 's')
text(ax, 52, 40, '2 : R', 'limite', 's')
save(fig, '51-151')
