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

fig, ax = canvas(82)
text(ax, 6, 70, r'$M=$', 'sujet', 'm')
mtx(ax, 22, 70, [('p', 'q'), ('r', 's')], 'sujet')
arrow(ax, (22, 64), (22, 52), 'varie'); text(ax, 28, 58, r'avec $T_{12}(1)$ : $r=0$ et $p=s$', 'varie', 's', ha='left')
mtx(ax, 22, 46, [('p', 'q'), ('0', 'p')], 'varie')
arrow(ax, (22, 40), (22, 28), 'varie'); text(ax, 28, 34, r'avec $T_{21}(1)$ : $q=0$', 'varie', 's', ha='left')
mtx(ax, 22, 22, [('p', '0'), ('0', 'p')], 'resultat')
text(ax, 44, 22, r'$M=p\cdot 1$', 'resultat', 'l', ha='left')
save(fig, '73-157')
