import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
u = 10
x0, y0 = 14, 38
poly(ax, [(x0, y0), (x0+4*u, y0), (x0+4*u, y0+3*u), (x0, y0+3*u)], 'sujet')
line(ax, [(x0, y0), (x0+4*u, y0+3*u)], 'varie', lw=1.8)
text(ax, x0 + 2*u, y0 - 3, '4 m', 'sujet', 'm')
text(ax, x0 - 1.5, y0 + 1.5*u, '3 m', 'sujet', 'm', ha='right')
text(ax, x0 + 2.2*u, y0 + 2.2*u, 'câble', 'varie', 'm', va='bottom', ha='right')
f = numberline(ax, 6, 70, 14, 0, 8, step=1, labels=False, arrow_right=False)
text(ax, f(0), 9.5, '0', 'fixe', 's'); text(ax, f(4), 9.5, '4', 'fixe', 's'); text(ax, f(7), 9.5, '7', 'fixe', 's')
line(ax, [(f(4), 14), (f(7), 14)], 'varie', lw=2.4)
text(ax, f(5.5), 19, 'le câble est entre 4 et 7', 'varie', 's')
text(ax, 71, 62, 'plus long que 4', 'fixe', 's'); text(ax, 71, 58.5, 'plus court que 3 + 4', 'fixe', 's')
save(fig, '22-008')
