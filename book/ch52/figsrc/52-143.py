import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 25, 66, r'$\nu$ puis l’opération', 'sujet', 's'); text(ax, 73, 66, r'opération puis $\nu$', 'autre', 's')
rows = [(r'$\nu(5)+\nu(6)=\bar{3}$', r'$\nu(11)=\bar{3}$'), (r'$\nu(5)\,\nu(6)=\bar{2}$', r'$\nu(30)=\bar{2}$'), (r'$\nu(1)=1+I$', r'unité de $R/I$')]
for i, (a, b) in enumerate(rows):
    y = 52 - i * 17
    box(ax, 2, y - 6, 44, 12, 'sujet', label=a, size='s')
    box(ax, 56, y - 6, 30, 12, 'autre' if i < 2 else 'resultat', label=b, size='s')
    text(ax, 51, y, r'$=$', 'resultat', 'l')
text(ax, 44, 6, 'mêmes résultats : +, ×, 1', 'resultat', 's')
save(fig, '52-143')
