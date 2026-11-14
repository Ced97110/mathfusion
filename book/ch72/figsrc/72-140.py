import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 62, '1. un produit existe', 'sujet', 'm')
for i in range(5):
    box(ax, 4 + i * 13.5, 44, 11, 11, 'sujet', label=r'$S$', size='m')
text(ax, 76, 49.5, '… ?', 'sujet', 'l', ha='left')
text(ax, 44, 38, 'récurrence : longueur inconnue', 'sujet', 's')
text(ax, 44, 28, r'2. au plus $n$ réflexions', 'autre', 'm')
for i in range(4):
    box(ax, 12 + i * 15, 10, 12, 11, 'autre', label=r'$S$', size='m')
brace(ax, 12, 69, 9, 'autre', label=r'$n$', down=True)
text(ax, 44, 2.5, 'argument d’Artin', 'autre', 's') if False else None
save(fig, '72-140')
