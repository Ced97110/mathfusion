import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 74, r'$p=5$ : entiers pairs 2, 4, 6 et $m=60$', 'encre', 's')
ws = [26, 16, 16, 16]
labs = [r'$x^2+60$', r'$x-2$', r'$x-4$', r'$x-6$']
roles = ['varie', 'sujet', 'sujet', 'sujet']
x = 3
for w, lab, role in zip(ws, labs, roles):
    box(ax, x, 50, w, 11, role, label=lab, size='s')
    x += w + 2
text(ax, 16, 45, 'degré 2', 'varie', 's')
text(ax, 55, 45, 'trois de degré 1', 'sujet', 's')
text(ax, 44, 66, 'produit  ' + r'$g$', 'encre', 's')
brace(ax, 3, 83, 41, 'resultat', label=r'degré $2+1+1+1=5$', down=True)
arrow(ax, (44, 28), (44, 22), 'varie')
text(ax, 60, 25, r'retirer 2', 'varie', 's')
box(ax, 14, 8, 60, 13, 'resultat', label=r'$f=g-2$')
save(fig, '65-141')
