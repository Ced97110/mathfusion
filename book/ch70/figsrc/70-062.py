import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, r'$f=2y^4-y+1$', 'encre', 'l')
terms = [(8, 30, r'$2\,y^4$', 'sujet'), (42, 22, r'$-\,y$', 'fixe'), (68, 16, r'$+\,1$', 'fixe')]
for x, w, lab, role in terms:
    box(ax, x, 22, w, 11, role, label=lab, size='l')
brace(ax, 8, 84, 34.5, 'fixe', label='3 termes', down=False)
arrow(ax, (18, 13.5), (26, 21.5), 'sujet')
text(ax, 22, 9, r'$n=4$ : le plus grand', 'sujet', 'm', weight='bold')
text(ax, 22, 4.5, 'exposant de $y$', 'sujet', 's')
save(fig, '70-062')
