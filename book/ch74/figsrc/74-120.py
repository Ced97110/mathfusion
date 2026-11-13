import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def mat(x0, y0, d, role, hd, res1, res2, rrole, cw=14, ch=11):
    for i in range(2):
        for j in range(2):
            if i == j:
                box(ax, x0 + j * cw, y0 + (1 - i) * ch, cw, ch, role, label=d[i], size='m')
            else:
                box(ax, x0 + j * cw, y0 + (1 - i) * ch, cw, ch, 'fixe', label=r'$\ast$', size='m')
    text(ax, x0 + cw, y0 + 2 * ch + 5, hd, role, 's')
    text(ax, x0 + cw, y0 - 5, res1, rrole, 's')
    text(ax, x0 + cw, y0 - 11, res2, rrole, 's')
mat(5, 24, ['1/2', '1/2'], 'sujet', 'rotation de 60°', r'trace $=\frac{1}{2}+\frac{1}{2}=1$', r'$=2\cos 60°$ : vrai', 'resultat')
mat(49, 24, ['1/2', '−1/2'], 'autre', 'miroir pour 60°', r'trace $=\frac{1}{2}-\frac{1}{2}=0$', r'$\neq 2\cos 60°$', 'limite')
text(ax, 44, 3, r'$\ast$ : cases qui ne servent pas à la trace', 'fixe', 's')
save(fig, '74-120')
