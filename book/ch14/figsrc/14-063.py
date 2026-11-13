import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def frac(x, y, top, bot, role_t, role_b, w=18):
    text(ax, x, y + 6, top, role_t, 'm'); line(ax, [(x - w / 2, y), (x + w / 2, y)], 'encre', lw=1.0); text(ax, x, y - 6, bot, role_b, 'm')
text(ax, 44, 66, 'le facteur change de côté', 'varie', 's')
frac(14, 46, r'$x^{-2}$', '1', 'varie', 'fixe'); arrow(ax, (28, 46), (58, 46), 'varie')
frac(72, 46, '1', r'$x^{2}$', 'fixe', 'resultat')
text(ax, 44, 51, 'en bas', 'varie', 's')
frac(14, 16, '1', r'$c^{-6}$', 'fixe', 'varie'); arrow(ax, (28, 16), (58, 16), 'varie')
frac(72, 16, r'$c^{6}$', '1', 'resultat', 'fixe')
text(ax, 44, 21, 'en haut', 'varie', 's')
save(fig, '14-063')
