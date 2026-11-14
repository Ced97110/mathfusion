import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 70, r'$-(21a^2 + 7a - 18)$', 'sujet', 'l')
terms = [r'$+21a^2$', r'$+7a$', r'$-18$']
res = [r'$-21a^2$', r'$-7a$', r'$+18$']
tags = [r'$+ \to -$', r'$+ \to -$', r'$- \to +$']
for c, t, r, g in zip((15, 44, 73), terms, res, tags):
    box(ax, c - 12, 48, 24, 12, 'varie', label=t)
    arrow(ax, (c - 4, 47), (c - 4, 31), 'varie')
    text(ax, c - 2, 39, g, 'varie', 's', ha='left')
    box(ax, c - 12, 18, 24, 12, 'resultat', label=r)
text(ax, 44, 8, r'$a = 1$ : les deux valent $-10$', 'resultat', 'm')
save(fig, '15-086')
