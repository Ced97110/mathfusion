import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
expr = [r'$((ab)c)d$', r'$(a(bc))d$', r'$(ab)(cd)$', r'$a((bc)d)$', r'$a(b(cd))$']
bw, g = 16, 1.5; x0 = (88 - (5 * bw + 4 * g)) / 2
for k, e in enumerate(expr):
    x = x0 + k * (bw + g); box(ax, x, 38, bw, 10, 'sujet', label=e, size='s')
    arrow(ax, (x + bw / 2, 37.5), (44 + (k - 2) * 4, 20.5), 'sujet')
box(ax, 30, 8, 28, 12, 'resultat', label=r'$abcd$', size='l')
text(ax, 44, 3.5, 'un seul résultat', 'resultat', 's')
text(ax, 44, 52.5, '5 écritures différentes', 'sujet', 's')
save(fig, '45-100')
