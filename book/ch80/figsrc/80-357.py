import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
xs = [11, 33, 55, 77]
heads = ['0 premier', '1 premier', '2 premiers', '3 premiers']
signs = ['+', '−', '+', '−']
terms = ['30', '15, 10, 6', '5, 3, 2', '1']
for i, x in enumerate(xs):
    text(ax, x, 54, heads[i], 'encre', 's')
    box(ax, x - 5, 36, 10, 9, 'sujet' if signs[i] == '+' else 'varie', label=signs[i], size='l')
    text(ax, x, 27, terms[i], 'encre', 'm')
text(ax, 44, 14, r'signe $=(-1)^k$', 'resultat', 'l')
text(ax, 44, 6, r'$k$ : nombre de premiers choisis', 'fixe', 's')
save(fig, '80-357')
