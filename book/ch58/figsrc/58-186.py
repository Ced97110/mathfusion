import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# degré au plus 1 : deux nombres par polynôme (constante et coefficient de x)
text(ax, 47, 66, 'polynômes de degré au plus 1', 'encre', 's')
text(ax, 46, 58, 'terme constant', 'varie', 's')
text(ax, 73, 58, r'coefficient de $x$', 'sujet', 's')
data = [(r'$3 + 5x$', '3', '5'), (r'$2 - x$', '2', '−1'), (r'$7$', '7', '0')]
y = 44
for lab, c0, c1 in data:
    text(ax, 14, y + 4.5, lab, 'encre', 'm')
    box(ax, 34, y, 24, 9, 'varie', label=c0, size='m', r=0.5)
    box(ax, 61, y, 24, 9, 'sujet', label=c1, size='m', r=0.5)
    y -= 12
brace(ax, 34, 85, 17, 'resultat', label='2 nombres : dim = 2, non 1', down=True, depth=2.4)
save(fig, '58-186')
