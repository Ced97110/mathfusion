import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
y = 16
f = numberline(ax, 8, 76, y, -5, 5, 1, labels=False)
for v, t in [(-4, '−4'), (0, '0'), (4, '4')]:
    text(ax, f(v), y - 3.4, t, 'fixe', 's')
disc(ax, f(-4), y, 1.6, 'resultat'); disc(ax, f(4), y, 1.6, 'resultat')
box(ax, 34, 42, 16, 9, 'sujet', label='16', size='l')
arrow(ax, (f(-4), y + 3), (34, 44), 'varie', curve=-0.35)
arrow(ax, (f(4), y + 3), (50, 44), 'varie', curve=0.35)
text(ax, 17, 36, r'$(-4)^2 = 16$', 'varie', 's')
text(ax, 67, 36, r'$4^2 = 16$', 'varie', 's')
brace(ax, f(-4), f(4), y - 6, 'resultat', label='opposés')
save(fig, '22-025')
