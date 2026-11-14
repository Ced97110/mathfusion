import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ox, oy = 44, 38
Y = lambda y: ox + 14 * y
V = lambda v: oy + 7 * v
# g = 0 : the zero polynomial lies on the whole axis
line(ax, [(Y(-1.9), V(0)), (Y(1.9), V(0))], 'autre', lw=2.2)
# f = y^2 - 1 plotted against y
line(ax, [(Y(t / 20), V((t / 20) ** 2 - 1)) for t in range(-34, 35)], 'sujet', lw=1.3)
for s in (-1, 1):
    disc(ax, Y(s), V(0), 1.3, 'resultat')
text(ax, Y(1) , oy - 3.6, r'$y=1$', 'resultat', 's')
text(ax, Y(-1), oy - 3.6, r'$y=-1$', 'resultat', 's')
brace(ax, Y(-1), Y(1), oy - 7, 'resultat', 'racines communes')
text(ax, Y(-1.7) - 2, V(1.89), r'$f=y^2-1$', 'sujet', 's', ha='right')
text(ax, Y(1.9) + 1.5, V(0) + 2.5, r'$g=0$', 'autre', 's', ha='left')
box(ax, 14, 3, 60, 10, 'resultat', label=r'$\mathrm{Res}(f,g)=0^{2}=0$', size='m')
save(fig, '70-121')
