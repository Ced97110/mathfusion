import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ox, oy = 22, 40
Y = lambda y: ox + 10 * y
V = lambda v: oy + 6 * v
line(ax, [(ox - 20, oy), (ox + 20, oy)], 'fixe', lw=0.7)
line(ax, [(ox, oy - 12), (ox, oy + 16)], 'fixe', lw=0.7)
line(ax, [(Y(t / 20), V((t / 20) ** 2 - 1)) for t in range(-32, 33)], 'sujet', lw=1.3)
disc(ax, ox, V(-1), 1.4, 'resultat')
text(ax, ox + 2.5, V(-1) - 0.3, r'$-p(x)$', 'resultat', 's', ha='left')
disc(ax, ox, oy, 1.1, 'varie')
text(ax, ox + 2.5, oy + 3, r'$s=0$', 'varie', 's', ha='left')
text(ax, ox, 66, r'$f=y^2-p(x)$', 'sujet', 'm')
box(ax, 46, 56, 40, 9, 'sujet', label=r'$g=2y$ : $b_1=2$, $s=0$', size='s')
box(ax, 46, 42, 40, 9, 'fixe', label=r'$n=2$ : degré de $f$ en $y$', size='s')
box(ax, 46, 28, 40, 9, 'fixe', label=r'$\mathrm{Res}=b_1^{\,n}\,f(x,s)$', size='s')
box(ax, 46, 12, 40, 11, 'resultat', label=r'$2^2\times(-p)=-4p(x)$', size='s')
for y0 in (56, 42, 28):
    arrow(ax, (66, y0), (66, y0 - 5), 'varie', lw=1.0)
save(fig, '70-139')
