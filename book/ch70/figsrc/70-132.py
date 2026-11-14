import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
oy = 30
panels = [(4, r'$2x+6=0$', r'$a\neq0$', r'$x=-3$', 'resultat'),
          (32, r'$0x+5=0$', r'$a=0$, $b\neq0$', 'aucune\nsolution', 'fixe'),
          (60, r'$0x+0=0$', r'$a=0$, $b=0$', r'tout $x$', 'resultat')]
for k, (px, title, cond, res, rr) in enumerate(panels):
    x0 = px + 20.8
    X = lambda x: x0 + 5.2 * x
    line(ax, [(px, oy), (px + 26, oy)], 'fixe', lw=0.8)
    if k == 0:
        line(ax, [(X(x), oy + 2.2 * (2 * x + 6)) for x in (-4, 1)], 'sujet', lw=1.4)
        disc(ax, X(-3), oy, 1.3, 'resultat')
    elif k == 1:
        line(ax, [(X(-4), oy + 11), (X(1), oy + 11)], 'sujet', lw=1.4)
    else:
        line(ax, [(px, oy), (px + 26, oy)], 'resultat', lw=2.6)
    text(ax, px + 13, oy + 28, title, 'sujet', 's')
    text(ax, px + 13, oy + 23, cond, 'fixe', 's')
    text(ax, px + 13, oy - 8, res, rr, 's')
save(fig, '70-132')
