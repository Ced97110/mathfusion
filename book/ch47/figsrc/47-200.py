import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 54, r'conjugué de $n=3$ par $g=5$', 'encre', 's')
toks1 = [('$-5$', 'fixe'), ('$+3$', 'sujet'), ('$+5$', 'fixe')]
toks2 = [('$+3$', 'sujet'), ('$-5$', 'fixe'), ('$+5$', 'fixe')]
for k, (t, r) in enumerate(toks1): box(ax, 18 + k*17, 38, 14, 9, r, label=t, size='m')
for k, (t, r) in enumerate(toks2): box(ax, 18 + k*17, 16, 14, 9, r, label=t, size='m')
arrow(ax, (42, 37.5), (25, 25.5), 'varie')
text(ax, 62, 31.5, 'commutatif : on déplace 3', 'varie', 's')
brace(ax, 35, 62, 15.5, 'fixe', label=r'$-5+5=0$')
text(ax, 44, 3, r'reste $3$ : toujours dans $N$', 'resultat', 's')
save(fig, '47-200')
