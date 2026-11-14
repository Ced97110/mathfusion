import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 19, 56, 'la lettre', 'sujet', 's'); text(ax, 69, 56, 'version approchée', 'varie', 's')
for y, a, b in [(36, r'$x = 4\,316$', r'$\tilde{x} = 4\,000$'), (12, r'$V$', r'$\tilde{V}$')]:
    box(ax, 3, y, 32, 11, 'sujet', label=a, size='l'); box(ax, 53, y, 32, 11, 'varie', label=b, size='l')
    arrow(ax, (36.5, y + 5.5), (51.5, y + 5.5), 'varie')
    text(ax, 44, y + 9, 'trait', 'varie', 's')
save(fig, '10-027')
