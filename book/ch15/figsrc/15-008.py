import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
for i in range(5):
    box(ax, 9 + 14 * i, 30, 14, 8, 'sujet', label=r'$x$'); box(ax, 9 + 14 * i, 10, 14, 8, 'sujet', label=r'$x$')
brace(ax, 9, 51, 39, 'sujet', r'$3x$', down=False); brace(ax, 51, 79, 39, 'sujet', r'$2x$', down=False)
brace(ax, 9, 79, 9, 'sujet', r'$5x$')
line(ax, [(79, 18), (79, 30)], 'resultat', dash=True)
text(ax, 77, 24, 'même fin', 'resultat', 's', ha='right')
save(fig, '15-008')
