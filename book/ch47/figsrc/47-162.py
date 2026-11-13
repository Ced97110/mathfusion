import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 18, 64, r'$N$', 'sujet', 'l'); text(ax, 70, 64, r'$(1\ 2)\,N$', 'resultat', 'l')
text(ax, 44, 64, r'$(1\ 2)\ \times$', 'varie', 'm')
L = ['1', '(1 2 3)', '(1 3 2)']; R = ['(1 2)', '(2 3)', '(1 3)']
for i in range(3):
    y = 46 - i * 17
    box(ax, 4, y - 5, 28, 10, 'sujet', label=L[i], size='m')
    box(ax, 56, y - 5, 28, 10, 'resultat', label=R[i], size='m')
    arrow(ax, (32.5, y), (55.5, y), 'varie')
text(ax, 44, 3, 'les trois échanges', 'resultat', 's')
save(fig, '47-162')
