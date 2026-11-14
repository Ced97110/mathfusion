import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = numberline(ax, 7, 77, 34, -2, 5, labels=False, arrow_right=True)
names = {-2: '0,01', -1: '0,1', 0: '1', 1: '10', 2: '100'}
for v in range(-2, 6):
    lab = names.get(v, rf'$10^{{{v}}}$')
    text(ax, f(v), 30.2, lab, 'fixe', 's')
for v in range(-2, 5):
    arrow(ax, (f(v) + 1.5, 40), (f(v + 1) - 1.5, 40), 'varie', curve=-0.6)
text(ax, 42, 49, 'chaque arc : $\\times10$', 'varie', 'm')
p = 4 + math.log10(3.2)
disc(ax, f(p), 34, 1.4, 'sujet')
line(ax, [(f(p), 32.5), (f(p), 22)], 'sujet', dash=True)
text(ax, f(p), 18, r'$P=3{,}2\times10^{4}$', 'sujet', 'm')
text(ax, 44, 6, 'mêmes longueurs entre crans', 'fixe', 's')
save(fig, '14-080')
