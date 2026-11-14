import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)

def card(x0, role, head, k, verdict, vrole):
    text(ax, x0 + 20, 62, head, role, 'm', weight='bold')
    box(ax, x0 + 2, 44, 36, 10, role, label=r'$f=x^2+t$')
    arrow(ax, (x0 + 20, 43.5), (x0 + 20, 36), role)
    box(ax, x0 + 2, 26, 36, 10, role, label=k)
    arrow(ax, (x0 + 20, 25.5), (x0 + 20, 18), vrole)
    box(ax, x0 + 2, 4, 36, 13, vrole, label=verdict, size='s')

card(2, 'sujet', 'caractéristique 0', r'$2\times1=2\neq0$', 'jamais de racine\nmultiple', 'resultat')
card(46, 'autre', 'caractéristique 2', r'$2\times1=0$', 'racine double\npossible', 'limite')
save(fig, '62-105')
