import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
text(ax, 44, 90, r'$\tau_{u,c}(x) = x + c\,B(x,u)\,u$', 'sujet', 'l')
text(ax, 44, 80, r'$x=(1,1),\ u=(1,0),\ c=-2$', 'encre', 's')
steps = [('sujet', r'$B(x,u)=1\times0-1\times1=-1$', "d'abord"), ('varie', r'$c\,B=-2\times(-1)=2$', 'puis'),
         ('varie', r'$2\times u=(2,0)$', 'puis'), ('resultat', r'$x+(2,0)=(3,1)$', 'enfin')]
for i, (role, lab, st) in enumerate(steps):
    y = 56 - i * 18
    box(ax, 20, y, 66, 11, role, label=lab, size='s')
    text(ax, 10, y + 5.5, st, role, 's')
    if i < 3: arrow(ax, (53, y - 0.5), (53, y - 6.5), 'encre')
save(fig, '75-071')
