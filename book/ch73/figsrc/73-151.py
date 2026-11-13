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

fig, ax = canvas(50)
O = (30, 16); u = 17
arrow(ax, (10, 16), (54, 16), 'fixe'); arrow(ax, (30, 14), (30, 43), 'fixe')
poly(ax, [(30, 16), (47, 16), (47, 33), (30, 33)], 'sujet')
poly(ax, [(13, 16), (30, 16), (30, 33), (13, 33)], 'resultat')
text(ax, 38.5, 24.5, 'avant', 'sujet', 's'); text(ax, 21.5, 24.5, 'après', 'resultat', 's')
for p in ((47, 16), (30, 33), (13, 16)): disc(ax, p[0], p[1], 1.2, 'varie')
arrow(ax, (47.5, 18), (32, 34.5), 'varie', curve=0.35); arrow(ax, (28, 34.5), (12.5, 18), 'varie', curve=0.35)
text(ax, 47, 11.5, r'$(1,0)$', 'varie', 's'); text(ax, 13, 11.5, r'$(-1,0)$', 'varie', 's'); text(ax, 36, 40, r'$(0,1)$', 'varie', 's')
text(ax, 73, 36, r'$w(-1)=$', 'resultat', 'm'); mtx(ax, 73, 28, [('0', '−1'), ('1', '0')], 'resultat')
text(ax, 73, 20, 'quart de tour', 'resultat', 's')
text(ax, 44, 5, r'$T_{12}(-1)\,T_{21}(1)\,T_{12}(-1)$', 'encre', 's')
save(fig, '73-151')
