import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 62, r'$5\times4\times3\times2\times1$', 'sujet', 'xl')
brace(ax, 12, 76, 56, 'sujet', label='5 facteurs', down=True)
arrow(ax, (44, 42), (44, 34), 'varie')
text(ax, 44, 27, r'$5\,!$', 'varie', 16, weight='bold')
text(ax, 44, 17, 'se lit « factorielle 5 »', 'varie', 's')
text(ax, 44, 8, r'$5\,!=120$ ; $n\,!$ pour tout $n$', 'resultat', 's')
save(fig, '44-122')
