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

fig, ax = canvas(84)
A = [[1, 2], [3, 4]]; B = [[5, 6], [7, 8]]
P = [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
assert P == [[19, 22], [43, 50]]
text(ax, 44, 79, 'une case du produit à la fois', 'fixe', 's')
pw, ph = 40, 28
for i in range(2):
    for j in range(2):
        x = 2 + j * (pw + 4); y = 40 - i * (ph + 4) + 4
        box(ax, x, y, pw, ph, 'sujet')
        text(ax, x + pw / 2, y + ph - 4.5, f'ligne {i + 1}, colonne {j + 1}', 'sujet', 's')
        a, b = A[i], [B[0][j], B[1][j]]
        text(ax, x + pw / 2, y + ph / 2 - 0.5, rf'${a[0]}\times{b[0]}+{a[1]}\times{b[1]}$', 'encre', 'm')
        text(ax, x + pw / 2, y + 5, f'= {P[i][j]}', 'resultat', 'l', weight='bold')
text(ax, 44, 4, '4 cases, 2 produits et 1 somme chacune', 'fixe', 's')
save(fig, '51-148')
