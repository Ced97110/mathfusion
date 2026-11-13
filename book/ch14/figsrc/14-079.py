import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def row(y, a, b, note):
    box(ax, 4, y, 36, 12, 'sujet', label=a, size='m')
    arrow(ax, (42, y + 6), (54, y + 6), 'varie')
    box(ax, 56, y, 28, 12, 'resultat', label=b, size='m')
    text(ax, 44, y - 7, note, 'varie', 's')
row(42, r'$2{,}9\times10^{7}$', '29 000 000', '7 rangs à droite, 8 chiffres')
row(16, r'$4{,}21\times10^{-5}$', '0,0000421', '5 rangs à gauche, 4 zéros')
save(fig, '14-079')
