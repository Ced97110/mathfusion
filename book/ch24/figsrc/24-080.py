import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
s, cx, y0 = 8.0, 24.0, 14.0
X = lambda v: cx + s * v
Y = lambda v: y0 + s * v
n = 60
pts = [(-2.12 + 4.24 * i / n) for i in range(n + 1)]
line(ax, [(X(t), Y(t * t)) for t in pts], 'sujet', lw=1.3)
text(ax, X(0), Y(2.2), r'$y = x^2$', 'sujet', 's')
for h, lab in [(4, 'deux solutions'), (0, 'une solution'), (-1, 'aucune solution')]:
    line(ax, [(X(-2.8), Y(h)), (X(2.8), Y(h))], 'varie', lw=0.9)
    text(ax, X(2.8) + 2, Y(h), lab, 'varie', 's', ha='left')
    text(ax, X(-2.8), Y(h) - 2.6 if h < 0 else Y(h) + 2.4, r'$y = %d$' % h, 'varie', 's', ha='left')
for sx in (-2, 2):
    disc(ax, X(sx), Y(4), 1.1, 'resultat')
text(ax, X(0), Y(0) + 3, r'$0$', 'resultat', 's')
disc(ax, X(0), Y(0), 1.1, 'resultat')
text(ax, X(-2), Y(4) - 3, r'$-2$', 'resultat', 's')
text(ax, X(2), Y(4) - 3, r'$2$', 'resultat', 's')
save(fig, '24-080')
