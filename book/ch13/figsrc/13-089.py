import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
u = 6.0
def couple(y, a, b, name):
    text(ax, 11, y - 3, name, 'encre', 'l')
    text(ax, 37, y, 'j’ai', 'sujet', 's', ha='right')
    text(ax, 37, y - 7, 'je dois', 'varie', 's', ha='right')
    for i in range(a): box(ax, 40 + i * u, y - 2.5, 5, 5, 'sujet', r=0.3)
    for i in range(b): box(ax, 40 + i * u, y - 9.5, 5, 5, 'varie', r=0.3)
couple(60, 3, 5, '(3, 5)')
couple(26, 5, 3, '(5, 3)')
text(ax, 11, 43, '≠', 'limite', 'xl')
text(ax, 62, 43, 'dette 2', 'varie', 'm')
text(ax, 62, 9, 'reste 2', 'resultat', 'm')
save(fig, '13-089')
