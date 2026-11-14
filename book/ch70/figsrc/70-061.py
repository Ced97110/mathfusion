import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, r'$g=4y^3+2y+9$', 'encre', 'l')
terms = [(8, 30, r'$4\,y^3$', 'sujet'), (42, 22, r'$+\,2\,y$', 'fixe'), (68, 16, r'$+\,9$', 'fixe')]
for x, w, lab, role in terms:
    box(ax, x, 30, w, 11, role, label=lab, size='l')
arrow(ax, (16, 19.5), (18.5, 29.5), 'sujet')
arrow(ax, (32, 19.5), (28.5, 29.5), 'fixe')
text(ax, 15, 15.5, r'$b_m=4$', 'sujet', 'm', weight='bold')
text(ax, 33, 15.5, r'$m=3$', 'fixe', 'm')
text(ax, 44, 6, r'coefficient de tête de $g$', 'sujet', 's')
save(fig, '70-061')
