import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 16, 56, 56, 11, 'sujet', label='compter des facteurs', size='l')
xs = [15, 44, 73]
tops = [r'$2^{5}\times2^{3}=2^{8}$', r'$2^{0}=1,\ 2^{-1}=\frac{1}{2}$', r'$10^{21}$']
labs = ['règles des exposants', 'exposants négatifs', 'notation scientifique']
sub = ['5 + 3 = 8 facteurs', '0 facteur : 1', '21 facteurs 10']
for x, t, l, sb in zip(xs, tops, labs, sub):
    arrow(ax, (44 + (x - 44) * 0.45, 56), (x, 44), 'varie')
    box(ax, x - 14, 27, 28, 16, 'resultat', label=t, size='s')
    text(ax, x, 21, sb, 'fixe', 's')
    text(ax, x, 9, l, 'varie', 's')
save(fig, '14-005')
