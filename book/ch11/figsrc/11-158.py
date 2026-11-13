import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
def row(y, left, right, fwd, back, name):
    text(ax, 44, y + 29, name, 'encre', 's')
    box(ax, 4, y + 5, 20, 11, 'varie', label=left, size='m')
    box(ax, 64, y + 5, 20, 11, 'sujet', label=right, size='m')
    arrow(ax, (25, y + 13), (63, y + 13), 'fixe'); text(ax, 44, y + 18, fwd, 'fixe', 's')
    arrow(ax, (63, y + 8), (25, y + 8), 'resultat'); text(ax, 44, y + 3.5, back, 'resultat', 's')
row(40, 'd = ?', 'C = 62,8', r'$C=3{,}14\times d$', r'$62{,}8\div 3{,}14 = 20$', 'cercle')
row(5, 'l = ?', 'A = 96', r'$12\times l = A$', r'$96\div 12 = 8$', 'rectangle de longueur 12')
save(fig, '11-158')
