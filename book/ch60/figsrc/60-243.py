import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 32, 76, r'$32=2^5$ : 7 partitions de 5', 'sujet', 'm')
parts = [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
u, x0 = 7.6, 25
for k, p in enumerate(parts):
    y = 62 - k * 8.5
    text(ax, 3, y + 3.25, ' + '.join(map(str, p)), 'sujet', 's', ha='left')
    x = x0
    for q in p:
        box(ax, x, y, q * u - 0.8, 6.5, 'sujet')
        x += q * u
line(ax, [(64, 65.5), (66, 65.5), (66, 9.5), (64, 9.5)], 'resultat', lw=1.0)
text(ax, 76, 37.5, r'$P(5)=7$', 'resultat', 'l')
save(fig, '60-243')
