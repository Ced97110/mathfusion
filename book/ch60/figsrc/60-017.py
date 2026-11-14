import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 3.4
def bar(y, n, g):
    x = 2.0
    for k in range(n):
        if k and k % g == 0: x += 1.2
        full = k < (n // g) * g
        box(ax, x, y, u - 0.4, 4.4, 'sujet' if full else 'varie', r=0.4)
        x += u
def line_(y, n, g, eq, lab, res_y, res):
    bar(y, n, g)
    text(ax, 28.5, y + 2.2, eq, 'encre', 's', ha='left')
    text(ax, 47.5, y + 2.2, lab, 'varie', 's', ha='left')
    arrow(ax, (69.5, y + 2.2), (72, res_y), 'varie', lw=0.8)
for (ys, n, res) in ((56, 7, '(3, 1)'), (28, 5, '(1, 2)')):
    ya, yb = ys, ys - 10
    ym = (ya + yb) / 2 + 2.2
    box(ax, 72, ym - 4.5, 14, 9, 'resultat', label=res, size='s')
    g4 = (n - n % 4) // 4
    line_(ya, n, 4, f'{n} = {g4} × 4 + {n % 4}', f'par 4 : ligne {n % 4}', ym, res)
    g3 = (n - n % 3) // 3
    line_(yb, n, 3, f'{n} = {g3} × 3 + {n % 3}', f'par 3 : colonne {n % 3}', ym, res)
save(fig, '60-017')
