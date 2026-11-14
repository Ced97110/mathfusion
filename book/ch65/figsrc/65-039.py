import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

D0 = -2
fig, ax = canvas(60)
text(ax, 44, 55, r'$D=-2$ au départ, puis on échange', 'encre', 'm', weight='bold')
bw, gap = 17.0, 4.0
x0 = (88 - 4 * bw - 3 * gap) / 2
for k in range(4):
    x = x0 + k * (bw + gap)
    v = D0 * (-1) ** k
    same = (k % 2 == 0)
    role = 'sujet' if same else 'varie'
    box(ax, x, 22, bw, 16, role, label=('%d' % v) if v > 0 else '−%d' % -v, size='l', weight='bold')
    text(ax, x + bw / 2, 44, r'$k=%d$' % k, 'fixe', 's')
    text(ax, x + bw / 2, 15, 'D' if same else '−D', role, 'm', weight='bold')
    if k < 3:
        arrow(ax, (x + bw + 0.4, 30), (x + bw + gap - 0.4, 30), 'fixe', lw=0.8)
text(ax, 44, 6, 'k pair : D reste · k impair : −D', 'resultat', 's')
save(fig, '65-039')
