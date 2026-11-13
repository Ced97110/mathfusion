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
box(ax, 3, 4, 40, 40, 'resultat'); box(ax, 46, 4, 39, 40, 'limite')
text(ax, 23, 51, 'possible', 'resultat', 'l'); text(ax, 65.5, 51, 'impossible', 'limite', 'l')
text(ax, 23, 38, r'$d=3$', 'resultat', 'l'); text(ax, 65.5, 38, r'$d=0$', 'limite', 'l')
mtx(ax, 23, 27, [('3', '0'), ('0', '⅓')], 'resultat'); mtx(ax, 65.5, 27, [('0', '0'), ('0', '0')], 'limite')
text(ax, 23, 17, r'$3\times\frac{1}{3}=1$', 'resultat', 'm'); text(ax, 65.5, 17, 'aucun nombre × 0 = 1', 'limite', 's')
text(ax, 23, 9, 'déterminant 1', 'resultat', 's'); text(ax, 65.5, 9, 'déterminant 0', 'limite', 's')
save(fig, '73-153')
