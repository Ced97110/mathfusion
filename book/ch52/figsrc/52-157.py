import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 40, r'$\bar{\eta}$', 'varie', 22)
arrow(ax, (38, 32), (24, 22), 'varie'); arrow(ax, (50, 32), (64, 22), 'varie')
text(ax, 20, 17, "la lettre η :\nl'origine", 'varie', 's'); text(ax, 66, 17, 'la barre : agit sur\ndes classes', 'varie', 's')
text(ax, 44, 4, r'$\bar{\eta}(a + I) = \eta(a)$', 'resultat', 'm')
save(fig, '52-157')
