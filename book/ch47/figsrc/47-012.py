import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 10, 52, r'$H$', 'sujet', 'l'); text(ax, 10, 16, r'$1+H$', 'varie', 'l')
for i in range(4):
    x = 30 + i * 15
    box(ax, x - 6, 46, 12, 10, 'sujet', label=str(3 * i), size='l')
    box(ax, x - 6, 10, 12, 10, 'varie', label=str(3 * i + 1), size='l')
    arrow(ax, (x, 45), (x, 21), 'fixe', both=True)
text(ax, 37.5, 33, '+ 1', 'fixe', 'm')
brace(ax, 24, 84, 58, 'sujet', '4 nombres', down=False)
brace(ax, 24, 84, 8, 'varie', '4 nombres', down=True)
save(fig, '47-012')
