import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 23, 60, r'signe $+$', 'sujet', 'm'); text(ax, 65, 60, r'signe $-$', 'autre', 'm')
plus = [r'$2\times3\times4=24$', r'$0\times0\times0=0$', r'$1\times1\times1=1$']
moins = [r'$1\times3\times0=0$', r'$0\times1\times4=0$', r'$2\times0\times1=0$']
for i in range(3):
    box(ax, 4, 46 - 11 * i, 38, 9, 'sujet', label=plus[i], size='s')
    box(ax, 46, 46 - 11 * i, 38, 9, 'autre', label=moins[i], size='s')
box(ax, 4, 6, 80, 12, 'resultat', label=r'$\det A=24+1=25$', size='l', weight='bold')
save(fig, '76-106')
