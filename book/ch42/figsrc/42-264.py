import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
wb, gap = 15, 6.5; x0 = (88 - (4 * wb + 3 * gap)) / 2
cx = [x0 + i * (wb + gap) + wb / 2 for i in range(4)]
for i, c in enumerate(cx):
    box(ax, c - wb / 2, 36, wb, 12, 'sujet', label=rf'$S_{i+1}$')
    box(ax, c - wb / 2, 14, wb, 10, 'resultat', label=['2', '5', '7', '1'][i])
    arrow(ax, (c, 36), (c, 24.5), 'varie')
    if i < 3: text(ax, c + wb / 2 + gap / 2, 42, r'$\times$', 'sujet', 'l')
brace(ax, cx[0] - wb / 2, cx[3] + wb / 2, 50, 'sujet', label='ensemble produit', down=False)
brace(ax, cx[0] - wb / 2, cx[3] + wb / 2, 14, 'resultat', label='4-uplet (2, 5, 7, 1)')
save(fig, '42-264')
