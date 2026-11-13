import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
B = lambda a, b: r'$\binom{%s}{%s}$' % (a, b)
text(ax, 30, 70, B('n','k-1'), 'sujet', 'm'); text(ax, 58, 70, B('n','k'), 'sujet', 'm')
text(ax, 44, 70, '+', 'encre', 'm'); text(ax, 44, 56, B('n+1','k'), 'sujet', 'm')
arrow(ax, (32,67.5), (42,58.5), 'varie'); arrow(ax, (56,67.5), (46,58.5), 'varie')
line(ax, [(6,47),(82,47)], 'fixe', dash=True)
text(ax, 44, 43, 'même forme, autres nombres', 'fixe', 's')
cases = [(15,(3,1,3),(3,2,3),(4,2,6)), (44,(4,1,4),(4,2,6),(5,2,10)), (73,(5,2,10),(5,3,10),(6,3,20))]
for c,(n1,k1,v1),(n2,k2,v2),(n3,k3,v3) in [(a[0],a[1],a[2],a[3]) for a in cases]:
    text(ax, c-6, 32, B(n1,k1)+'=%d'%v1, 'sujet', 's')
    text(ax, c+7, 32, B(n2,k2)+'=%d'%v2, 'sujet', 's')
    text(ax, c, 20, B(n3,k3)+' = %d'%v3, 'resultat', 's', weight='bold')
    arrow(ax, (c-5,29.5), (c-1,22.5), 'varie'); arrow(ax, (c+6,29.5), (c+1,22.5), 'varie')
save(fig, '01-179')
