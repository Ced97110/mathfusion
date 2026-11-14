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

fig, ax = canvas(54)
tt = [(3, 'sujet', r'$T_{12}(a)$', [('1', 'a'), ('0', '1')]),
      (33, 'varie', r'$T_{21}(-a^{-1})$', [('1', '0'), ('−a⁻¹', '1')]),
      (63, 'sujet', r'$T_{12}(a)$', [('1', 'a'), ('0', '1')])]
for x, role, name, rows in tt:
    box(ax, x, 22, 22, 14, role)
    mtx(ax, x + 11, 29, rows, role)
    text(ax, x + 11, 41, name, role, 'm')
text(ax, 28, 29, r'$\times$', 'encre', 'l'); text(ax, 58, 29, r'$\times$', 'encre', 'l')
text(ax, 44, 49.5, r'$w(a)$ = produit de trois cisaillements', 'encre', 's')
text(ax, 44, 17.5, r'milieu : opposé de l’inverse de $a$', 'varie', 's')
text(ax, 44, 11, r'$a=2$ : inverse $\frac{1}{2}$, opposé $-\frac{1}{2}$', 'encre', 's')
text(ax, 44, 4, r'$a=-1$ : inverse $-1$, opposé $1$', 'encre', 's')
save(fig, '73-149')
