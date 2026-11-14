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

fig, ax = canvas(54)
bw, bh, by = 17.5, 10, 24
xs = [0.5 + i * 22.8 for i in range(4)]
pts = [r'$(1{,}5\,;\,0{,}5)$', r'$(3\,;\,0{,}5)$', r'$(-0{,}5\,;\,3)$', r'$(-3\,;\,-0{,}5)$']
roles = ['fixe', 'fixe', 'fixe', 'resultat']
# values : S(1,5 ; 0,5) = (3 ; 0,5) ; R(3 ; 0,5) = (-0,5 ; 3) ; R(-0,5 ; 3) = (-3 ; -0,5)
S = lambda p: (2 * p[0], p[1]); R = lambda p: (-p[1], p[0])
p = (1.5, 0.5); chain = [p]
for f in (S, R, R):
    chain.append(f(chain[-1]))
assert chain[-1] == (-3.0, -0.5) and chain[2] == (-0.5, 3.0)
for x, l, r in zip(xs, pts, roles):
    box(ax, x, by, bw, bh, r, label=l, size='s')
for k, (f, role) in enumerate((('S', 'sujet'), ('R', 'autre'), ('R', 'autre'))):
    xa, xb = xs[k] + bw, xs[k + 1]
    arrow(ax, (xa + 0.4, by + bh / 2), (xb - 0.4, by + bh / 2), role, lw=1.0)
    text(ax, (xa + xb) / 2, by + bh / 2 + 3, f'${f}$', role, 'm')
c = [x + bw / 2 for x in xs]
brace(ax, c[0], c[2], by + bh + 4, 'varie', 'S et R groupés', down=False)
brace(ax, c[1], c[3], by - 4, 'varie', 'R et R groupés', down=True)
text(ax, 44, 8, 'même suite de gestes, même arrivée', 'resultat', 's')
save(fig, '51-160')
