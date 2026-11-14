import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
labs = [r'$x_1$', r'$x_2$', r'$x_3$', '…', r'$x_{100}$']
ws = [12, 12, 12, 7, 18]; xs = []; cur = 5.0
for l, wd in zip(labs, ws):
    xs.append(cur)
    if l != '…': box(ax, cur, 8, wd, 11, 'fixe', label=l)
    else: text(ax, cur + wd / 2, 13.5, l, 'fixe', 'l')
    cur += wd + 3.5
box(ax, 22, 38, 44, 13, 'sujet', label=r'$x_i$ : la lettre numéro $i$', size='m')
for l, x, wd in zip(labs, xs, ws):
    if l == '…': continue
    arrow(ax, (44 + (x + wd / 2 - 44) * 0.25, 38), (x + wd / 2, 20.5), 'varie')
text(ax, 44, 29, r'$i$ prend tous les numéros', 'varie', 's')
save(fig, '49-021')
