import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 19, 46, r'paire de $R\times M$', 'fixe', 's')
text(ax, 72, 46, 'résultat dans M', 'fixe', 's')
for y, a, x, res in [(26, '3', '(2 ; 1)', '(6 ; 3)'), (10, '2', '(1 ; 4)', '(2 ; 8)')]:
    box(ax, 1, y - 1.5, 37, 12, 'fixe', fill=False, dash=True)
    box(ax, 3, y, 10, 9, 'varie', label=a)
    box(ax, 15, y, 21, 9, 'sujet', label=x)
    arrow(ax, (40, y + 4.5), (58, y + 4.5), 'resultat')
    text(ax, 49, y + 8, 'action', 'resultat', 's')
    box(ax, 60, y, 26, 9, 'resultat', label=res)
text(ax, 44, 3, '× construit des paires', 'fixe', 's')
save(fig, '57-076')
