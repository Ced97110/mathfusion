import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, 'somme sur les diviseurs de $n$'.replace('$n$', r'$n$'), 'sujet', 's')
box(ax, 4, 54, 80, 14, 'sujet', label=r'$q^n=\sum_{d\mid n}d\,N(d,q)$')
arrow(ax, (44, 52), (44, 34), 'varie', lw=1.3)
text(ax, 48, 43, 'inversion de Möbius', 'varie', 's', ha='left')
box(ax, 4, 16, 80, 16, 'resultat', label=r'$N(n,q)=\frac{1}{n}\sum_{d\mid n}\mu(n/d)\,q^d$')
text(ax, 44, 8, 'formule de Gauss', 'resultat', 's')
save(fig, '67-230')
