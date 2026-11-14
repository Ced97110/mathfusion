import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 22, 74, r'dans $S$ : relation', 'fixe', 's'); text(ax, 66, 74, r'dans $T$ : égalité', 'resultat', 's')
rows = [(58, r'$a\,E_f\,a$', r'$f(a)=f(a)$'),
        (40, r'$a\,E_f\,b\Rightarrow b\,E_f\,a$', r'$f(a)=f(b)\Rightarrow f(b)=f(a)$'),
        (22, r'$aE_fb,\ bE_fc\Rightarrow aE_fc$', r'$f(a)=f(b),\ f(b)=f(c)$ ' + '\n' + r'$\Rightarrow f(a)=f(c)$')]
for y, l, r in rows:
    box(ax, 2, y - 6, 38, 12, 'sujet'); text(ax, 21, y, l, 'sujet', 's')
    arrow(ax, (41, y), (46, y), 'varie')
    box(ax, 47, y - 6, 39, 12, 'resultat'); text(ax, 66.5, y, r, 'resultat', 's')
text(ax, 44, 8, '« = » a ces trois propriétés', 'encre', 'm', weight='bold')
save(fig, '43-085')
