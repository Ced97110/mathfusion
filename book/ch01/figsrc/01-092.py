import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(44)
x = lambda v: 8 + (v - 4300) * 0.72
line(ax, [(8, 18), (80, 18)], 'fixe')
for xx in (8, 44, 80):
    line(ax, [(xx, 16.8), (xx, 19.2)], 'fixe', lw=0.8)
text(ax, 8, 12, '4 300', 'fixe', 's')
text(ax, 80, 12, '4 400', 'fixe', 's')
xn = x(4329)
disc(ax, xn, 18, 1.3, 'sujet')
text(ax, xn, 38, 'N = 4 329', 'sujet', 'm')
line(ax, [(xn, 36), (xn, 20)], 'sujet', lw=0.6)
arrow(ax, (8, 25), (xn, 25), 'resultat')
text(ax, 18.4, 29, '29 pas', 'resultat', 's')
arrow(ax, (xn, 25), (80, 25), 'limite')
text(ax, 62, 29, '71 pas', 'limite', 's')
line(ax, [(44, 15), (44, 32)], 'varie', dash=True)
text(ax, 44, 12, '4 350', 'varie', 's')
save(fig, '01-092')
