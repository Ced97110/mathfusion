import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'$x^2-4=(x+2)(x-2)$', 'sujet', 'm')
W, H = 20, 10
xs = [8, 36, 64]
ys_top, ys_bot = 52, 28
box(ax, xs[0], ys_top, W, H, 'resultat', label=r'$x+2$')
box(ax, xs[1], ys_top, W, H, 'fixe', label=r'$x-2$', dash=True)
box(ax, xs[2], ys_top, W, H, 'fixe', label=r'$x+3$', dash=True)
box(ax, xs[1], ys_bot, W, H, 'fixe', label=r'$x-2$', dash=True)
box(ax, xs[2], ys_bot, W, H, 'fixe', label=r'$x+3$', dash=True)
text(ax, 32, ys_top + 5, r'$\times$', 'encre', 'm')
text(ax, 60, ys_top + 5, r'$\times$', 'encre', 'm')
text(ax, 60, ys_bot + 5, r'$\times$', 'encre', 'm')
line(ax, [(4, 45), (84, 45)], 'encre', lw=1.0)
text(ax, 44, 20, 'les mêmes en haut et en bas : retirés', 'fixe', 's')
box(ax, 26, 3, 36, 11, 'resultat', label=r'$x+2$', size='l')
save(fig, '21-063')
