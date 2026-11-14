import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

EM = {'−': .838, '½': .75, '⅓': .75, ' ': .318, '⁻': .5, '¹': .4}
def wd(s): return sum(EM.get(c, .636) for c in s)
def mtx(ax, cx, cy, rows, role='encre', size='m'):
    fs = SIZE[size]; cols = list(zip(*rows)); cw = [max(wd(c) for c in col) for col in cols]
    lines = []
    for r in rows:
        s = ''
        for j, c in enumerate(r):
            p = int(round((cw[j] - wd(c)) / 2 / .318))
            s += ' ' * p + c + ' ' * p + ('  ' if j < len(r) - 1 else '')
        lines.append(s)
    text(ax, cx, cy, '\n'.join(lines), role, size)
    w = (sum(cw) + .636 * (len(cols) - 1)) * fs * .3528 + 2; h = len(rows) * fs * 1.2 * .3528 + 1
    for sx in (-1, 1):
        x = cx + sx * w / 2
        line(ax, [(x - sx, cy + h / 2), (x, cy + h / 2), (x, cy - h / 2), (x - sx, cy - h / 2)], role, lw=0.8)

fig, ax = canvas(56)
A = [('1', '2'), ('0', '1')]; Bm = [('1', '0'), ('−½', '1')]; C = [('0', '2'), ('−½', '1')]; D = [('0', '2'), ('−½', '0')]
for y, first in ((44, A), (18, C)):
    mtx(ax, 14, y, first, 'sujet' if first is A else 'fixe')
    text(ax, 27, y, r'$\times$', 'encre', 'l')
    mtx(ax, 41, y, Bm if first is A else A, 'varie' if first is A else 'sujet')
    text(ax, 54, y, '=', 'encre', 'l')
mtx(ax, 71, 44, C, 'fixe'); mtx(ax, 71, 18, D, 'resultat')
text(ax, 71, 10, r'$w(2)$', 'resultat', 'm')
text(ax, 14, 37.5, r'$T_{12}(2)$', 'sujet', 's'); text(ax, 41, 37.5, r'$T_{21}(-\frac{1}{2})$', 'varie', 's')
text(ax, 41, 10.5, r'même $T_{12}(2)$', 'sujet', 's')
arrow(ax, (66, 37), (24, 24.5), 'fixe', curve=-0.15)
save(fig, '73-150')
