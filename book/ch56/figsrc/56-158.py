import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
Z = [r'$\mathbb{Z}$', r'$\mathbb{Z}[x_1]$', r'$\mathbb{Z}[x_1,x_2]$', r'$\mathbb{Z}[x_1,\ldots,x_r]$']
F = [r'$F$', r'$F[x_1]$', r'$F[x_1,x_2]$', r'$F[x_1,\ldots,x_r]$']
adds = [r'$+x_1$', r'$+x_2$', r'$+x_r$']
h, gap = 11, 7.5
for col, (labs, x0) in enumerate([(Z, 2), (F, 46)]):
    for k, lab in enumerate(labs):
        y = 72 - k * (h + gap) - h + 11
        box(ax, x0, y - 11 + 0, 40, h, 'sujet' if k == 0 else 'resultat', label=lab, size='s')
        if k < 3:
            arrow(ax, (x0 + 20, y - 11), (x0 + 20, y - 11 - gap + 0.3), 'varie')
            if col == 0:
                text(ax, x0 + 23, y - 11 - gap / 2, adds[k], 'varie', 's', ha='left')
save(fig, '56-158')
