import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
u = 14; y0 = 32; x0 = 36
arrow(ax, (6, y0), (82, y0), 'fixe', lw=0.9); text(ax, 78, y0 - 3, 'réels', 'fixe', 's')
for s, role, lab in [(-1, 'sujet', r'$H(x,y)=-i$'), (1, 'autre', r'$H(y,x)=i$')]:
    disc(ax, x0, y0 + s * u, 2.2, role)
    text(ax, x0 + 5, y0 + s * u, lab, role, 'm', ha='left')
arrow(ax, (x0, y0 - u + 4), (x0, y0 + u - 4), 'varie', both=True)
text(ax, x0 - 4, y0 + 7, 'conjugués', 'varie', 's', ha='right')
text(ax, x0 - 4, y0 - 8, 'échange', 'varie', 's', ha='right')
text(ax, 20, 58, r'$x=(1,\,0)$, $y=(i,\,0)$', 'encre', 's')
save(fig, '75-150')
