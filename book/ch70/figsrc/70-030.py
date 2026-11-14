import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# 3 x 3 table of coefficients : rows f, yg, g ; columns Y2, Y1, Y0
cx = (36, 56, 76)
rows = [(52, 'sujet', r'$f=0$', ['1', '-3', '2']),
        (36, 'varie', r'$yg=0$', ['1', '-1', '0']),
        (20, 'autre', r'$g=0$', ['0', '1', '-1'])]
for x, n in zip(cx, (r'$Y_2$', r'$Y_1$', r'$Y_0$')):
    text(ax, x, 68, n, 'encre', 'm')
for y, role, lab, vals in rows:
    text(ax, 14, y + 5, lab, role, 'm')
    for x, v in zip(cx, vals):
        box(ax, x - 8, y, 16, 10, role, label=v.replace('-', '$-$') if v.startswith('-') else v, size='m')
box(ax, 28, 4, 56, 10, 'resultat', label=r'$(Y_2,Y_1,Y_0)=(1,1,1)$ convient', size='s')
save(fig, '70-030')
