import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, r'$(x-2)(x-3)(x-4)$', 'sujet', 'l')
arrow(ax, (44, 53), (44, 45), 'varie')
text(ax, 62, 49, 'développer', 'varie', 's')
cs = [11, 32, 53, 74]
terms = [r'$x^3$', r'$-9x^2$', r'$+26x$', r'$-24$']
subs = ['1', r'$2+3+4=9$', r'$6+8+12=26$', r'$2\times3\times4=24$']
for c, t, s in zip(cs, terms, subs):
    box(ax, c - 9.5, 30, 19, 12, 'autre', label=t)
    arrow(ax, (c, 30), (c, 22), 'resultat')
    box(ax, c - 9.5, 8, 19, 14, 'resultat', label=s, size='s')
save(fig, '55-071')
