import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
a = [2, 3]; b = [4, 5]
p = [a[0]*b[0], a[0]*b[1] + a[1]*b[0], a[1]*b[1]]
assert p == [8, 22, 15]
text(ax, 44, 57, r'$(2,3)\times(4,5)$', 'encre', 'm')
text(ax, 44, 50, r'on garde les couples $j+k=i$', 'fixe', 's')
forms = [r'$a_0b_0$', r'$a_0b_1+a_1b_0$', r'$a_1b_1$']
nums = [r'$2\times4$', r'$2\times5+3\times4$', r'$3\times5$']
for i in range(3):
    y = 34 - i * 14
    text(ax, 9, y + 4, f'rang {i}', 'fixe', 's')
    text(ax, 33, y + 4, forms[i], 'sujet', 'm')
    text(ax, 58, y + 4, nums[i], 'varie', 'm')
    arrow(ax, (68, y + 4), (72, y + 4), 'fixe')
    box(ax, 72, y, 14, 8, 'resultat', label=str(p[i]), size='m')
text(ax, 44, 4, r'produit : $(8,\,22,\,15)$', 'resultat', 'm')
save(fig, '54-091')
