import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(44)
y = 22
f = numberline(ax, 6, 70, y, -3, 4)
for v, s in ((0.5, r'$1/2$'), (math.sqrt(2), r'$\sqrt{2}$'), (math.pi, r'$\pi$')):
    disc(ax, f(v), y, 1.9, 'varie'); text(ax, f(v), y + 5, s, 'varie', 'm')
text(ax, 44, 36, 'points entre les traits', 'varie', 's')
brace(ax, f(-3), f(4), y - 7, 'fixe', label='8 repères numérotés')
save(fig, '12-012')
