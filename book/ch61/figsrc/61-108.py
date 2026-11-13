import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'$[E:F]=4$ briques', 'sujet', 'm')
def cells(y, role_of):
    for i in range(4):
        box(ax, 4 + i * 13, y, 12, 10, role_of(i), r=0.4)
cells(40, lambda i: 'resultat')
brace(ax, 4, 28, 51, 'resultat', label='2', down=False)
brace(ax, 30, 54, 51, 'resultat', label='2', down=False)
text(ax, 58, 45, r'$2$ divise $4$', 'resultat', 'm', ha='left')
cells(12, lambda i: 'sujet' if i < 3 else 'limite')
brace(ax, 4, 41, 23, 'sujet', label='3', down=False)
text(ax, 49.5, 8, 'reste 1', 'limite', 's')
text(ax, 58, 17, r'$3$ ne divise pas $4$', 'limite', 's', ha='left')
save(fig, '61-108')
