import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
u = 11
def panel(x0, role, a, b, area, tag, ok):
    oy = 14
    poly(ax, [(x0, oy), (x0 + a[0]*u, oy + a[1]*u), (x0 + (a[0]+b[0])*u, oy + (a[1]+b[1])*u), (x0 + b[0]*u, oy + b[1]*u)], role)
    arrow(ax, (x0, oy), (x0 + a[0]*u, oy + a[1]*u), 'sujet', lw=1.3)
    arrow(ax, (x0, oy), (x0 + b[0]*u, oy + b[1]*u), 'sujet', lw=1.3)
    text(ax, x0 + (a[0]+b[0])*u/2, oy + (a[1]+b[1])*u/2, f'{area}', role, 'l')
    return oy
panel(10, 'limite', (1, 0), (0, 2), 2, '', False)
panel(56, 'resultat', (1, 0), (0, 1), 1, '', True)
text(ax, 22, 48, 'liste 1', 'fixe', 'm'); text(ax, 62, 48, 'liste 2', 'fixe', 'm')
text(ax, 22, 6, r'$B = 2$ : pas symplectique', 'limite', 's')
text(ax, 66, 6, r'$B = 1$ : symplectique', 'resultat', 's')
text(ax, 22, 40, r'$(1,0)$ et $(0,2)$', 'sujet', 's')
text(ax, 66, 40, r'$(1,0)$ et $(0,1)$', 'sujet', 's')
line(ax, [(44, 8), (44, 46)], 'fixe', dash=True)
save(fig, '75-034')
