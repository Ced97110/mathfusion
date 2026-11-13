import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = lambda v: 8 + (v + 20) / 45 * 64
text(ax, 44, 46, r'$\tilde{V} = 2\,000$ ;  $V = 2\,004$ ;  $E = -4$', 'resultat', 'm')
line(ax, [(8, 22), (72, 22)], 'fixe')
line(ax, [(f(0), 17), (f(0), 36)], 'fixe', dash=True)
text(ax, f(0), 14, '0', 'fixe', 'm')
for n, v in [('684', -16), ('293', -7), ('706', 6), ('321', 21)]:
    disc(ax, f(v), 22, 1.5, 'sujet')
    text(ax, f(v), 28, f'{n} : {v:+d}'.replace('-', '−'), 'sujet', 's')
text(ax, 44, 7, 'écarts des deux côtés de 0', 'fixe', 's')
save(fig, '10-078')
