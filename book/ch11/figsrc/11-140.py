import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
x0, k, yt, yb = 6, 18.0, 36, 18
f = lambda v: x0 + v * k
g = lambda v: x0 + v * k / 2.54
box(ax, f(0), 44, f(4) - f(0), 6, 'sujet', label='ruban')
line(ax, [(f(0), yt), (f(4), yt)], 'sujet')
for v in range(5):
    line(ax, [(f(v), yt - 1.2), (f(v), yt + 1.2)], 'sujet')
    text(ax, f(v), yt + 3.8, '4 po' if v == 4 else str(v), 'sujet', 's')
line(ax, [(g(0), yb), (g(10.16), yb)], 'fixe')
for v in range(11):
    line(ax, [(g(v), yb - 1.2), (g(v), yb + 1.2)], 'fixe')
    if v % 2 == 0 and v < 10: text(ax, g(v), yb - 3.8, str(v), 'fixe', 's')
line(ax, [(g(10.16), yb - 1.2), (g(10.16), yb + 1.2)], 'resultat')
text(ax, g(10.16), yb - 3.8, '10,16 cm', 'resultat', 's')
line(ax, [(f(1), yt - 2), (g(2.54), yb + 2)], 'fixe', dash=True)
arrow(ax, (f(4), yt - 2), (g(10.16), yb + 2), 'resultat')
text(ax, 44, 6, '4 po × 2,54 cm/po = 10,16 cm', 'resultat', 's')
save(fig, '11-140')
