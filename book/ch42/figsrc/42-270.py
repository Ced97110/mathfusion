import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cs = [16, 36, 56, 76]; hs = [1, 3, 3, 1]
for i, (c, h) in enumerate(zip(cs, hs)):
    for k in range(h): box(ax, c - 3.5, 24 + k * 8.5, 7, 7, 'sujet', r=0.5)
    text(ax, c, 54, rf'$\binom{{3}}{{{i}}}$', 'sujet', 'm')
    text(ax, c, 20, f'{i} objet' + ('s' if i > 1 else ''), 'sujet', 's')
brace(ax, 10, 82, 16, 'resultat', label=r'$1 + 3 + 3 + 1 = 8$')
text(ax, 44, 4, r'$(1 + 1)^3 = 2^3 = 8$', 'resultat', 'm')
save(fig, '42-270')
