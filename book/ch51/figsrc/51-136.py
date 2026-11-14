import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, r'intègre $\Rightarrow$ 0 ou premier', 'sujet', 'm')
items = [(2, r'$\mathbb{Z}/7$', 'intègre : oui', 'char $=7$', '7 est premier', 'resultat'),
         (31, r'$\mathbb{Z}$', 'intègre : oui', 'char $=0$', '0 convient', 'resultat'),
         (60, r'$\mathbb{Z}/6$', 'intègre : non', 'char $=6$', "6 n'est ni 0 ni premier", 'limite')]
for x, name, st, ch, note, role in items:
    box(ax, x, 12, 26, 30, role)
    text(ax, x + 13, 37, name, role, 'l')
    text(ax, x + 13, 28, st, role, 's')
    text(ax, x + 13, 19, ch, role, 'm', weight='bold')
    text(ax, x + 13, 6, note, role, 's')
save(fig, '51-136')
