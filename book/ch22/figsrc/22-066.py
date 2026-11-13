import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 6.4; x0, y0 = 6, 14
R = lambda a, b, c, d: [(x0+a*u, y0+b*u), (x0+c*u, y0+b*u), (x0+c*u, y0+d*u), (x0+a*u, y0+d*u)]
poly(ax, R(0, 0, 3, 3), 'sujet'); poly(ax, R(3, 3, 7, 7), 'autre')
poly(ax, R(3, 0, 7, 3), 'varie'); poly(ax, R(0, 3, 3, 7), 'varie')
text(ax, x0+1.5*u, y0+1.5*u, r'$a^2=9$', 'sujet', 's')
text(ax, x0+5*u, y0+5*u, r'$b^2=16$', 'autre', 's')
text(ax, x0+5*u, y0+1.5*u, r'$ab=12$', 'varie', 's')
text(ax, x0+1.5*u, y0+5*u, r'$ab=12$', 'varie', 's')
brace(ax, x0, x0+3*u, y0, 'sujet', label=r'$a=3$')
brace(ax, x0+3*u, x0+7*u, y0, 'autre', label=r'$b=4$')
xr = x0 + 7*u + 4
text(ax, xr, 48, r'$(a+b)^2=49$', 'encre', 's', ha='left')
text(ax, xr, 38, r'$a^2+b^2=25$', 'encre', 's', ha='left')
text(ax, xr, 28, r'écart : $2ab=24$', 'varie', 's', ha='left')
save(fig, '22-066')
