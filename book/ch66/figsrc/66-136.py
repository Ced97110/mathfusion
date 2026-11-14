import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(64)
k = 14
disc(ax, 18, 36, k, 'sujet')
line(ax, [(18, 36), (18 + k, 36)], 'sujet')
text(ax, 25, 33, 'rayon 1', 'sujet', 's')
text(ax, 18, 43, r'aire $\pi$', 'sujet', 'm')
sd = math.sqrt(math.pi) * k
poly(ax, [(66 - sd / 2, 36 - sd / 2), (66 + sd / 2, 36 - sd / 2), (66 + sd / 2, 36 + sd / 2), (66 - sd / 2, 36 + sd / 2)], 'autre')
text(ax, 66, 36, r'aire $\pi$', 'autre', 'm')
text(ax, 66, 56, r'côté $\sqrt{\pi}\approx1{,}7725$', 'autre', 's')
text(ax, 42.5, 36, '=', 'encre', 'l')
text(ax, 44, 13, r'$\pi\approx3{,}1416$', 'fixe', 'm')
text(ax, 44, 5, r'$\sqrt{\pi}$ non constructible', 'limite', 'm')
save(fig, '66-136')
