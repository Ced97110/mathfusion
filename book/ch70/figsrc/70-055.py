import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 66, 'termes du développement', 'fixe', 's')
for x, s in [(6, r'$ab^2$'), (32, r'$-2ab^2$'), (58, r'$+4a^2c$')]:
    box(ax, x, 50, 24, 10, 'varie', label=s, size='m')
    arrow(ax, (x + 12, 49.5), (44, 43), 'fixe')
box(ax, 22, 33, 44, 10, 'sujet', label=r'$-ab^2+4a^2c$', size='m')
arrow(ax, (44, 32.5), (44, 26), 'fixe')
box(ax, 9, 16, 70, 10, 'resultat', label=r'$Res(f,f′)=-a\,(b^2-4ac)$', size='m')
box(ax, 2, 2, 40, 9, 'fixe', label=r'$a,b,c=1,-4,4$ : $Res=0$', size='s')
box(ax, 46, 2, 40, 9, 'fixe', label=r'$a,b,c=1,-3,2$ : $Res=-1$', size='s')
save(fig, '70-055')
