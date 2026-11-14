import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
for i in range(6):
    x = 6 + i * 13
    if i == 0: box(ax, x, 26, 11, 9, 'sujet', label='0')
    else: box(ax, x, 26, 11, 9, 'fixe', label=str(i), dash=True, fill=False)
brace(ax, 6, 17, 38, 'sujet', label=r'idéal nul $\{0\}$', down=False)
text(ax, 44, 17, r'$0+0=0$ : reste dans $\{0\}$', 'resultat', 's')
text(ax, 44, 8, r'$0\times r=0$ : reste dans $\{0\}$', 'resultat', 's')
save(fig, '52-270')
