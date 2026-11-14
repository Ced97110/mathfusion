import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'$p=2$ ; $a=3=1+1+1$', 'encre', 'm', weight='bold')
xs = [4, 33, 62]
for i, x in enumerate(xs):
    box(ax, x, 46, 22, 9, 'autre', label=rf'$c_{i+1}=1$')
    arrow(ax, (x + 11, 45.5), (x + 11, 36.5), 'varie')
    box(ax, x, 26, 22, 10, 'sujet', label=r'$\mathbb{Z}/2$')
    text(ax, x + 11, 21, '2 éléments', 'sujet', 's')
for x in (29.5, 58.5):
    text(ax, x, 31, r'$\oplus$', 'encre', 'l')
brace(ax, 4, 84, 17, 'resultat', label=r'$2\times2\times2=8=2^3$')
save(fig, '60-226')
