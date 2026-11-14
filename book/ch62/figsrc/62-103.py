import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# f = (x-1)(x-2)(x-3); f' = sum of three products; evaluated at x = 1
text(ax, 44, 58, r'$f^{\prime}$ en $x=1$ : trois termes', 'encre', 'm')
exprs = [r'$(x-2)(x-3)$', r'$(x-1)(x-3)$', r'$(x-1)(x-2)$']
vals = [r'$(-1)(-2)=2$', r'$0\times(-2)=0$', r'$0\times(-1)=0$']
roles = ['sujet', 'fixe', 'fixe']
xs = [3, 32, 61]
for i in range(3):
    box(ax, xs[i], 38, 24, 10, roles[i], label=exprs[i])
    arrow(ax, (xs[i] + 12, 37.5), (xs[i] + 12, 30), roles[i])
    box(ax, xs[i], 20, 24, 10, roles[i], label=vals[i], size='s')
text(ax, 29.5, 43, '+', 'encre', 'l'); text(ax, 58.5, 43, '+', 'encre', 'l')
box(ax, 12, 3, 64, 12, 'resultat', label=r'$f^{\prime}(1)=2+0+0\neq0$')
save(fig, '62-103')
