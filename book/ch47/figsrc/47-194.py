import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
x0 = 30; cw = 13; ch = 10; ys = [26, 12]
box(ax, x0 + 3 * cw - 1.5, ys[1] - 2.5, cw + 2, 2 * ch + 4 + 12.5 + 6, 'resultat', fill=False, lw=1.8)
for k in range(4):
    text(ax, x0 + k*cw + cw/2, 42, rf'$x^{k+1}$', 'resultat' if k == 3 else 'fixe', 's' if k < 3 else 'l', weight='bold' if k == 3 else 'normal')
rows = [('3 : ordre 4', 'sujet', [3, 9, 7, 1]), ('9 : ordre 2', 'autre', [9, 1, 9, 1])]
for (lab, r, vals), yy in zip(rows, ys):
    text(ax, 14, yy + ch/2, lab, r, 's')
    for k, v in enumerate(vals):
        rr = 'resultat' if k == 3 else r
        box(ax, x0 + k*cw, yy, cw - 1, ch, rr, label=str(v), size='m', lw=2.0 if k == 3 else 0.8)
save(fig, '47-194')
