import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, r'$f=3x^2+5x+7$', 'encre', 'l')
xs = [6, 34, 62]
tops = [r'$3x^2$', r'$5x$', r'$7$']
bots = [r'$6x$', r'$5$', 'disparaît']
notes = [r'$3\times2=6$', r'$5\times1=5$', None]
for i, x in enumerate(xs):
    box(ax, x, 40, 24, 11, 'fixe', label=tops[i], size='l')
    last = i == 2
    box(ax, x, 18, 24, 11, 'fixe' if last else 'sujet', label=bots[i], size='m' if last else 'l', dash=last)
    arrow(ax, (x + 12, 39.5), (x + 12, 29.5), 'varie')
    if notes[i]:
        text(ax, x + 14, 34.5, notes[i], 'varie', 's', ha='left')
text(ax, 44, 8, r"$f'=6x+5$", 'sujet', 'l')
save(fig, '70-064')
