import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'$s=2$ : coefficients 3 puis 1', 'encre', 'm')
def squares(n, y, role):
    for i in range(n):
        box(ax, 46 + i * 8, y - 3.5, 7, 7, role, r=0.5)
text(ax, 5, 42, r'$3\times n_1=3\times1$', 'sujet', 'm', ha='left')
squares(3, 42, 'sujet')
text(ax, 5, 28, r'$1\times n_2=1\times2$', 'varie', 'm', ha='left')
squares(2, 28, 'varie')
line(ax, [(5, 20), (83, 20)], 'fixe')
text(ax, 5, 11, r'$N=3+2=5$', 'resultat', 'l', ha='left', weight='bold')
squares(5, 11, 'resultat')
save(fig, '60-218')
