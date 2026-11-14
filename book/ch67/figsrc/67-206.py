import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 64, r'$f(x)=x^{6}+22x^{5}+21x^{4}+12x^{3}-37x^{2}-29x-15$', 'sujet', 'm')
arrow(ax, (44, 58), (44, 44.5), 'varie')
text(ax, 48, 51, 'degré 6', 'varie', 's', ha='left')
for i in range(6):
    disc(ax, 14 + 12 * i, 30, 5, 'autre', label=rf'$r_{{{i + 1}}}$')
brace(ax, 8, 80, 37, 'autre', label='six racines complexes', down=False)
text(ax, 44, 14, 'Galois permute les 6 racines', 'encre', 'm')
save(fig, '67-206')
