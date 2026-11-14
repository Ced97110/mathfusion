import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
EM = ' '
text(ax, 20, 72, r'$\mathbb{C}\otimes\mathbb{H}$ : dim. 4', 'sujet', 's')
text(ax, 66, 72, r'$M_2(\mathbb{C})$ : dim. 4', 'autre', 's')
for k, s in enumerate([r'$a\cdot1$', r'$b\cdot i$', r'$c\cdot j$', r'$d\cdot k$']):
    box(ax, 4, 56 - k * 10, 32, 9, 'sujet', label=s, size='m')
arrow(ax, (38, 43), (46, 43), 'varie'); text(ax, 42, 48, 'envoie', 'varie', 's')
text(ax, 66, 49, r'$a+bi$' + EM + r'$c+di$', 'autre', 's')
text(ax, 66, 38, r'$-c+di$' + EM + r'$a-bi$', 'autre', 's')
for sgn in (-1, 1):
    x = 66 + sgn * 19
    line(ax, [(x - sgn * 1.5, 56), (x, 56), (x, 31), (x - sgn * 1.5, 31)], 'autre', lw=0.9)
box(ax, 4, 5, 80, 14, 'resultat', label=r'matrice nulle $\Rightarrow\ a=b=c=d=0$', size='s')
arrow(ax, (66, 30), (66, 20), 'resultat')
save(fig, '77-146')
