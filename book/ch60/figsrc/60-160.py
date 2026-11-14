import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
w = 36
brace(ax, 8, 8 + 2 * w, 48, 'sujet', label=r'dimension $n=2$', down=False)
for k in range(2):
    box(ax, 8 + k * w, 36, w, 9, 'sujet', label=f'case {k + 1}', size='s')
for k in range(2):
    box(ax, 8 + k * w, 22, w, 9, 'resultat', label=rf'$d_{k + 1}=\lambda-2$ : degré 1', size='s')
brace(ax, 8, 8 + 2 * w, 20, 'resultat', label=r'degrés : $1+1=2$')
text(ax, 44, 5, r'$f=(\lambda-2)^2$ est de degré $n$', 'resultat', 's')
save(fig, '60-160')
