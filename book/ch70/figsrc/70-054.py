import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 70, 'on barre ligne et colonne', 'fixe', 's')
tops = [('1', 16, '−4   0\n2  −4\n= 16', r'$+\,1\times16=16$'),
        ('−4', 44, '2   0\n0  −4\n= −8', r'$-\,(-4)\times(-8)=-32$'),
        ('4', 72, '2  −4\n0   2\n= 4', r'$+\,4\times4=16$')]
for s, xc, minor, term in tops:
    box(ax, xc - 9, 56, 18, 9, 'varie', label=s, size='m')
    arrow(ax, (xc, 55.5), (xc, 49), 'fixe')
    box(ax, xc - 12, 30, 24, 18, 'sujet', label=minor, size='s')
    text(ax, xc, 23, term, 'sujet', 's')
box(ax, 24, 4, 40, 10, 'resultat', label=r'$16-32+16=0$', size='m')
save(fig, '70-054')
