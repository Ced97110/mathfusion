import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
perms = [('231', '+', 'resultat'), ('312', '+', 'resultat'), ('123', '+', 'resultat'),
         ('132', '-', 'varie'), ('213', '-', 'varie'), ('321', '-', 'varie')]
ys = []
for k, (p, s, role) in enumerate(perms):
    y = 61 - k * 9; ys.append(y)
    lab = rf'$e_{{{p}}}=+e_{{123}}$' if s == '+' else rf'$e_{{{p}}}=-e_{{123}}$'
    box(ax, 2, y - 3.5, 40, 7.5, role, label=lab, size='s')
    arrow(ax, (43, y), (60, 33), role, lw=0.8)
box(ax, 2, 61 - 6 * 9 - 3.5, 40, 7.5, 'limite', label=r'$e_{112}=0$', size='s')
box(ax, 61, 25, 25, 17, 'sujet', label=r'$e_{123}$', size='l')
text(ax, 73.5, 21, '1 seule dimension', 'sujet', 's')
save(fig, '76-069')
