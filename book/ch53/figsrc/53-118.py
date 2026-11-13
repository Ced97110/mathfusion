import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
vals = [17]
for _ in range(4): vals.append(vals[-1] ** 2 % 55)
assert vals == [17, 14, 31, 26, 16]
for i, v in enumerate(vals):
    x = 3 + i * 17
    box(ax, x, 22, 12, 12, 'sujet', label=str(v), size='l')
    text(ax, x + 6, 16, r'$17^{%d}$' % 2 ** i, 'sujet', 's')
    if i < 4: arrow(ax, (x + 12.5, 28), (x + 16.5, 28), 'varie')
text(ax, 44, 45, 'chaque flèche : au carré', 'varie', 's')
text(ax, 44, 40, 'puis reste par 55', 'varie', 's')
text(ax, 44, 6, r'$(m^{2^k})^2 = m^{2^{k+1}}$', 'encre', 'm')
save(fig, '53-118')
