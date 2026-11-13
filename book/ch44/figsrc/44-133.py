import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
xs = [13, 33, 53, 73]; s = 14
for k, x in enumerate(xs):
    a = 90 * k; c = math.cos(math.radians(a)); sn = math.sin(math.radians(a))
    P = lambda dx, dy: (x + dx * c - dy * sn, 30 + dx * sn + dy * c)
    poly(ax, [P(-s/2, -s/2), P(s/2, -s/2), P(s/2, s/2), P(-s/2, s/2)], 'sujet')
    px, py = P(-s/2 + 2.6, s/2 - 2.6); disc(ax, px, py, 1.9, 'varie')
    text(ax, x, 15, f'{a}°', 'sujet', 'm')
brace(ax, 4, 82, 12, 'sujet', depth=1.6)
text(ax, 44, 4, '4 rotations remettent le carré en place', 'sujet', 's')
text(ax, 44, 47, r'$R_n$ : $n$ rotations, ici $n = 4$', 'sujet', 'm')
save(fig, '44-133')
