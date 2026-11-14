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

fig, ax = canvas(52)
mtx(ax, 14, 34, [('0', '2'), ('−½', '0')], 'sujet'); text(ax, 28, 34, r'$\times$', 'encre', 'l')
mtx(ax, 42, 34, [('0', '−1'), ('1', '0')], 'varie'); text(ax, 56, 34, '=', 'encre', 'l')
mtx(ax, 72, 34, [('2', '0'), ('0', '½')], 'resultat')
text(ax, 14, 44, r'$w(2)$', 'sujet', 'm'); text(ax, 42, 44, r'$w(-1)$', 'varie', 'm')
text(ax, 72, 44, r'$\mathrm{diag}(2,\frac{1}{2})$', 'resultat', 'm')
text(ax, 3, 21, 'haut gauche', 'fixe', 's', ha='left'); text(ax, 24, 21, r'$0\times 0+2\times 1=2$', 'resultat', 'm', ha='left')
text(ax, 3, 12, 'bas droite', 'fixe', 's', ha='left'); text(ax, 24, 12, r'$-\frac{1}{2}\times(-1)+0\times 0=\frac{1}{2}$', 'resultat', 'm', ha='left')
text(ax, 44, 3.5, r'déterminant $1\times 1=1$', 'encre', 's')
save(fig, '73-152')
