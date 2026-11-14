import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 58, r'$p^{3}$ : $p$ trois fois', 'sujet', 'l')
for i in range(3): disc(ax, 20 + i * 24, 40, 6, 'sujet', label=r'$p$', size='l')
for i in range(2): text(ax, 32 + i * 24, 40, r'$\times$', 'fixe', 'l')
brace(ax, 14, 74, 32, 'sujet', label='3 lettres')
text(ax, 44, 17, r'$p=2$ : $2\times2\times2=8$', 'resultat', 'm')
box(ax, 22, 3, 44, 8, 'sujet', label='exposant 3 = degré 3', size='s')
save(fig, '15-079')
