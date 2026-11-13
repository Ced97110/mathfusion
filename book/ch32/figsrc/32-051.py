import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
wd, gap = 19, 2
x0 = (W - 4 * wd - 3 * gap) / 2
for n in range(4):
    x = x0 + n * (wd + gap); cx = x + wd / 2
    pair = n % 2 == 0
    role = 'resultat' if pair else 'varie'
    sg = '+' if pair else '−'
    text(ax, cx, 49, f'n = {n}', 'encre', 's')
    box(ax, x, 30, wd, 9, role, label=f'{180 * n}° {sg} 40°', size='s')
    arrow(ax, (cx, 29.5), (cx, 21), role)
    ang = 180 * n + (40 if pair else -40)
    box(ax, x, 11, wd, 9, 'sujet', label=f'{ang}°', size='s')
text(ax, 22, 4, 'pair : on ajoute 40°', 'resultat', 's')
text(ax, 66, 4, 'impair : on retire 40°', 'varie', 's')
save(fig, '32-051')
