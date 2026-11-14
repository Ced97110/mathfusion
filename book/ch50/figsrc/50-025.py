import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
disc(ax, 20, 46, 5, 'sujet', label='e', size='l')
text(ax, 28, 46, '{e} : 1 élément', 'sujet', 'm', ha='left')
for cx, p in [(15, '2'), (44, '3'), (73, '5')]:
    box(ax, cx - 13.5, 16, 27, 11, 'resultat', label=f'1 = {p}⁰ : {p}-groupe', size='s')
    arrow(ax, (20 + (cx - 20) * 0.3, 40.5), (cx, 27.8), 'varie')
text(ax, 44, 6.5, r'pour tout $p$ : $1=p^0$', 'encre', 'm')
save(fig, '50-025')
