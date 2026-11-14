import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(95)
for i in range(5):
    x = 12 + i * 15
    box(ax, x - 5, 70, 10, 9, 'sujet', label='1')
    box(ax, x - 5, 36, 10, 9, 'autre', label='3')
    arrow(ax, (x, 69), (x, 46), 'varie')
brace(ax, 7, 77, 83.5, 'sujet', '5 = 1+1+1+1+1', down=False)
brace(ax, 7, 77, 35, 'autre', '3+3+3+3+3 = 15', down=True)
text(ax, 83, 57.5, 'f', 'varie', 'l', ha='right')
text(ax, 4, 17, 'f(1) = 3 est le seul choix :', 'varie', 's', ha='left')
box(ax, 4, 3, 80, 9, 'resultat', label='f(5) = 15 : position 3')
save(fig, '48-185')
