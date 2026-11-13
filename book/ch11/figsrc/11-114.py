import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 4.5; y0 = 14; h = 4*u
a = 4; b = 48
poly(ax, [(a, y0), (a+6*u, y0), (a+8*u, y0+h), (a+2*u, y0+h)], 'sujet')
poly(ax, [(a, y0), (a+2*u, y0), (a+2*u, y0+h)], 'varie')
line(ax, [(a+6*u, y0), (a+8*u, y0), (a+8*u, y0+h)], 'fixe', dash=True)
poly(ax, [(b+2*u, y0), (b+8*u, y0), (b+8*u, y0+h), (b+2*u, y0+h)], 'resultat')
poly(ax, [(b+6*u, y0), (b+8*u, y0), (b+8*u, y0+h)], 'varie')
brace(ax, a, a+6*u, y0, 'fixe', 'b = 6')
text(ax, a+4.4*u, y0+h/2, 'h = 4', 'sujet', 's')
text(ax, a+0.75*u, y0+0.85*u, '2', 'varie', 's')
arrow(ax, (a+2*u, y0+h+2), (b+8*u, y0+h+2), 'varie', curve=-0.22)
text(ax, 46, 47, 'on déplace le triangle', 'varie', 's')
text(ax, a+4*u, 4, 'parallélogramme', 'sujet', 's')
text(ax, b+5*u, 4, 'rectangle 6 × 4 = 24', 'resultat', 's')
save(fig, '11-114')
