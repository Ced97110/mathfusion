import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
tot = [5, 7, 11, 12]; co = [0, -1, 1, 0]
role = {0: 'fixe', -1: 'varie', 1: 'resultat'}
text(ax, 10, 48, 'totaux', 'sujet', 's'); text(ax, 10, 28, 'coefficients', 'varie', 's')
for i in range(4):
    x = 22 + 16 * i
    box(ax, x, 44, 14, 8, 'sujet', label=r'$g(%d)=%d$' % (i, tot[i]), size='s')
    box(ax, x, 24, 14, 8, role[co[i]], label=str(co[i]).replace('-', '−'))
    arrow(ax, (x + 7, 44), (x + 7, 32.5), 'fixe', lw=0.6)
text(ax, 54, 14, r'$f(2)=-7+11=4$', 'resultat', 'm')
text(ax, 54, 5, 'les autres coefficients : 0', 'fixe', 's')
save(fig, '80-275')
