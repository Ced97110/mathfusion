import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 70, r'$8a^2\,(\,3a^4 - 5a^3 + a\,)$', 'sujet', 'l')
terms = [r'$3a^4$', r'$-5a^3$', r'$a$']
res = [r'$24a^6$', r'$-40a^5$', r'$8a^3$']
for c, t, r in zip((15, 44, 73), terms, res):
    box(ax, c - 12, 46, 24, 12, 'varie', label=t)
    arrow(ax, (c - 4, 45), (c - 4, 31), 'varie')
    text(ax, c - 2, 38, r'$\times 8a^2$', 'varie', 's', ha='left')
    box(ax, c - 12, 18, 24, 12, 'resultat', label=r)
save(fig, '15-083')
