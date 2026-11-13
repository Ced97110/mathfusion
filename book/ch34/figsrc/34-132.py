import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 8, 76, 22, 0.8, 1.0, step=0.1, arrow_right=False, size='s')
vals = [(0.866, 'sujet', '0,866', 'cos 30°'), (0.933, 'varie', '0,933', ''), (0.9659, 'resultat', '0,9659', 'cos 15°')]
for v, role, lab, name in vals:
    disc(ax, f(v), 22, 1.6, role)
    text(ax, f(v), 28, lab, role, 's')
    if name: text(ax, f(v), 11, name, role, 's')
arrow(ax, (f(0.866) + 1, 32), (f(0.933) - 1, 32), 'varie', curve=-0.4)
arrow(ax, (f(0.933) + 1, 32), (f(0.9659) - 1, 32), 'varie', curve=-0.4)
text(ax, (f(0.866) + f(0.933)) / 2, 43, '+ 1, puis ÷ 2', 'varie', 's')
text(ax, (f(0.933) + f(0.9659)) / 2 + 3, 39, 'racine', 'varie', 's')
save(fig, '34-132')
