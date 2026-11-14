import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# characteristic 3, exponent 3 : (a+b)^3 = a^3 + 3 a^2 b + 3 a b^2 + b^3 ; the middle coefficient 3 is 0
text(ax, 44, 65, r'$(a+b)^3$ en caractéristique 3', 'sujet', 'm')
terms = [('sujet', r'$a^3$'), ('varie', r'$3\,a^2b$'), ('varie', r'$3\,ab^2$'), ('sujet', r'$b^3$')]
for k, (role, t) in enumerate(terms):
    box(ax, 3 + k * 21.5, 42, 19.5, 12, role, label=t, size='s', dash=(role == 'varie'))
brace(ax, 25, 65.5, 40, 'varie', label=r'$3 = 0$ : ils disparaissent', size='s')
arrow(ax, (44, 26), (44, 19), 'resultat')
box(ax, 20, 6, 48, 12, 'resultat', label=r'$a^3 + b^3$')
save(fig, '67-072')
