import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
s = 4.5
x = 6
for n, role, lab in ((3, 'sujet', '9'), (4, 'varie', '16'), (5, 'resultat', '25')):
    box(ax, x, 22, n * s, n * s, role, label=lab, size='l')
    text(ax, x + n * s / 2, 16, {3: '(3, 0)', 4: '(0, 4)', 5: '(3, 4)'}[n], role, 's')
    x += n * s + 11
text(ax, 6 + 13.5 + 5.5, 22 + 9, '+', 'encre', 'l')
text(ax, 6 + 13.5 + 18 + 16.5, 22 + 9, '=', 'encre', 'l')
text(ax, 44, 48, 'carré de la somme', 'resultat', 'm')
text(ax, 44, 6, 'termes croisés : 0', 'fixe', 's')
save(fig, '72-045')
