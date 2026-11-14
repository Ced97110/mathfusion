import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(62)
k = 10
disc(ax, 16, 46, k, 'sujet')
line(ax, [(16, 46), (16 + k, 46)], 'sujet')
text(ax, 20, 43, 'rayon 1', 'sujet', 's')
arrow(ax, (16, 35), (16, 22), 'varie')
text(ax, 20, 29, 'dérouler', 'varie', 's', ha='left')
x0 = 12; L = 2 * math.pi * k; xm = x0 + L / 2
line(ax, [(x0, 18), (x0 + L, 18)], 'sujet', lw=1.8)
for x in (x0, xm, x0 + L):
    line(ax, [(x, 16.5), (x, 19.5)], 'sujet', lw=1.0)
text(ax, xm, 23, r'$2\pi\approx6{,}283$', 'sujet', 's')
brace(ax, x0, xm, 15, 'fixe', label=r'$\pi\approx3{,}1416$')
brace(ax, xm, x0 + L, 15, 'fixe', label=r'$\pi\approx3{,}1416$')
text(ax, 62, 50, r'$2\pi$ non constructible', 'limite', 's')
save(fig, '66-138')
