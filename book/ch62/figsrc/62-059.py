import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 76, 'coefficients d’un reste = degré de $f$', 'encre', 's')
text(ax, 3, 57, r'$f=x^2-2$', 'fixe', 's', ha='left')
text(ax, 3, 51, 'degré 2', 'fixe', 's', ha='left')
for k, l in enumerate([r'$a_0$', r'$a_1x$']):
    box(ax, 32 + k * 25, 52, 22, 11, 'sujet', label=l)
brace(ax, 32, 79, 51, 'sujet', label='2 coefficients', down=True)
text(ax, 3, 27, 'degré 3', 'fixe', 's', ha='left')
text(ax, 3, 33, 'polynôme de', 'fixe', 's', ha='left')
for k, l in enumerate([r'$a_0$', r'$a_1x$', r'$a_2x^2$']):
    box(ax, 32 + k * 18.5, 22, 16, 11, 'sujet', label=l, size='s')
brace(ax, 32, 85.5, 21, 'sujet', label='3 coefficients', down=True)
text(ax, 44, 4, r'$[K:F]=n=\deg f$', 'resultat', 'l')
save(fig, '62-059')
