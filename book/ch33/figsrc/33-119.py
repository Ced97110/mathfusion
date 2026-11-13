import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
text(ax, 44, 38, r'$\cos(\arctan t)=\frac{1}{\sqrt{1+t^2}}$', 'sujet', 'm')
vals = [r'$\frac{4}{3}$', r'$\frac{16}{9}$', r'$\frac{25}{9}$', r'$\frac{5}{3}$', r'$\frac{3}{5}$']
ops = [r'$t^2$', '+ 1', r'$\sqrt{\ }$', r'$1\ ÷$']
roles = ['sujet', 'fixe', 'fixe', 'fixe', 'resultat']
w = 12; g = 6
for i, v in enumerate(vals):
    x = 2 + i*(w+g)
    box(ax, x, 12, w, 12, roles[i], label=v)
    if i < 4:
        arrow(ax, (x+w+0.5, 18), (x+w+g-0.5, 18), 'varie')
        text(ax, x+w+g/2, 28, ops[i], 'varie', 's')
text(ax, 8, 6, r'$t=\frac{4}{3}$', 'sujet', 's'); text(ax, 80, 6, r'$\cos=\frac{3}{5}$', 'resultat', 's')
save(fig, '33-119')
