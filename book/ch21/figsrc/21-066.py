import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 22, 48, r'$12$', 'encre', 'l'); text(ax, 66, 48, r'$x^2-1$', 'encre', 'l')
for i, (x, s) in enumerate([(4, '2'), (19, '2'), (34, '3')]):
    box(ax, x, 26, 9, 10, 'sujet', label=s)
    if i < 2: text(ax, x + 12, 31, r'$\times$', 'encre', 'm')
for i, (x, s) in enumerate([(47, r'$x+1$'), (68, r'$x-1$')]):
    box(ax, x, 26, 17, 10, 'sujet', label=s)
text(ax, 62.5, 31, r'$\times$', 'encre', 'm')
brace(ax, 4, 43, 25, 'fixe', 'irréductibles'); brace(ax, 47, 85, 25, 'fixe', 'irréductibles')
save(fig, '21-066')
