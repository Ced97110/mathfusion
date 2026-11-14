import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
u = 5; yb = 46
for x, n, lab in [(6, 2, r'$4=2^2$'), (24, 3, r'$9=3^2$'), (47, 5, r'$25=5^2$')]:
    poly(ax, [(x, yb), (x+n*u, yb), (x+n*u, yb+n*u), (x, yb+n*u)], 'sujet')
    for i in range(1, n):
        line(ax, [(x+i*u, yb), (x+i*u, yb+n*u)], 'sujet', lw=0.4)
        line(ax, [(x, yb+i*u), (x+n*u, yb+i*u)], 'sujet', lw=0.4)
    text(ax, x+n*u/2, yb-4.5, lab, 'sujet', 's')
poly(ax, [(6, 12), (22, 12), (22, 28), (6, 28)], 'fixe', fill=False)
poly(ax, [(6, 12), (14, 12), (14, 20), (6, 20)], 'sujet')
text(ax, 10, 16, r'$\frac{1}{4}$', 'sujet', 's')
text(ax, 25, 20, r'$=(\frac{1}{2})^2$', 'sujet', 's', ha='left')
box(ax, 58, 12, 24, 16, role='limite', fill=False, label='2', size='l', dash=True)
text(ax, 70, 7, 'aucune fraction', 'limite', 's')
save(fig, '22-068')
