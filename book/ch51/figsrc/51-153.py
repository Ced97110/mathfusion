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

fig, ax = canvas(70)
u = 15.0; ox, oy = 30.0, 12.0
P = lambda x, y: (ox + x * u, oy + y * u)
p0 = (1.5, 0.5); p1 = (-0.5, 1.5); p2 = (-1.0, 1.5)
n2 = lambda p: p[0] ** 2 + p[1] ** 2
assert (n2(p0), n2(p1), n2(p2)) == (2.5, 2.5, 3.25)
arrow(ax, (ox - 24, oy), (ox + 36, oy), 'fixe', lw=0.6)
arrow(ax, (ox, oy - 3), (ox, oy + 36), 'fixe', lw=0.6)
r = math.sqrt(2.5) * u
ax.add_patch(matplotlib.patches.Arc((ox, oy), 2 * r, 2 * r, theta1=0, theta2=180, ec=COL['fixe'], lw=0.8, ls='--', zorder=1))
arrow(ax, (ox, oy), P(*p0), 'sujet', lw=1.3)
arrow(ax, (ox, oy), P(*p1), 'varie', lw=1.3)
arrow(ax, (ox, oy), P(*p2), 'resultat', lw=1.3)
text(ax, P(*p0)[0] + 4, P(*p0)[1] + 1, r'$u$', 'sujet', 'l')
text(ax, P(*p1)[0] + 5.5, P(*p1)[1] + 3.5, r'$Ru$', 'varie', 'l')
text(ax, P(*p2)[0] - 4, P(*p2)[1] + 3.5, r'$SRu$', 'resultat', 'l')
text(ax, 86, 64, r'$u=(1{,}5\ ;\ 0{,}5)$ : longueur² 2,5', 'sujet', 's', ha='right')
text(ax, 86, 58, r'$Ru=(-0{,}5\ ;\ 1{,}5)$ : 2,5', 'varie', 's', ha='right')
text(ax, 86, 52, r'$SRu=(-1\ ;\ 1{,}5)$ : 3,25', 'resultat', 's', ha='right')
text(ax, 86, 46, 'R garde la longueur, S la change', 'fixe', 's', ha='right')
save(fig, '51-153')
