import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r'$x^j\times x^k=x^{j+k}$', 'sujet', 'l')
text(ax, 44, 52, r'$(1+2x)(3+4x)$', 'encre', 'm')
cx = [22, 48]; cy = [28, 14]; cw, ch = 24, 12
heads_c = ['3', '4x']; heads_r = ['1', '2x']
for i, h in enumerate(heads_c):
    text(ax, cx[i] + cw / 2, 46, h, 'autre', 'm')
for j, h in enumerate(heads_r):
    text(ax, 12, cy[j] + ch / 2, h, 'sujet', 'm')
prods = [[r'$1\times3=3$', r'$1\times4x=4x$'], [r'$2x\times3=6x$', r'$2x\times4x=8x^2$']]
ranks = [[0, 1], [1, 2]]
for j in range(2):
    for i in range(2):
        rk = ranks[j][i]
        role = 'varie' if rk == 1 else 'fixe'
        box(ax, cx[i], cy[j], cw, ch, role)
        text(ax, cx[i] + cw / 2, cy[j] + 8, prods[j][i], 'encre', 's')
        text(ax, cx[i] + cw / 2, cy[j] + 3, f'rang {rk}', role, 's')
text(ax, 44, 7, r'$3+(4x+6x)+8x^2=3+10x+8x^2$', 'resultat', 's')
save(fig, '54-092')
