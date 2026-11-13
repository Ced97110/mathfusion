import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(44)
arrow(ax, (9, 24), (83, 24), 'fixe', both=True)
for x, lab in ((16, '−1 000 000'), (30, '−1 000'), (44, '0'), (58, '1 000'), (72, '1 000 000')):
    line(ax, [(x, 22.8), (x, 25.2)], 'fixe'); text(ax, x, 19.5, lab, 'fixe', 's')
text(ax, 5, 24, '−∞', 'varie', 'l'); text(ax, 85, 24, '+∞', 'sujet', 'l')
text(ax, 18, 34, 'sous tout nombre\nnégatif choisi', 'varie', 's'); text(ax, 70, 34, 'au-dessus de tout\nnombre choisi', 'sujet', 's')
text(ax, 44, 8, '∞ n’est pas un nombre précis', 'fixe', 's')
save(fig, '30-057')
