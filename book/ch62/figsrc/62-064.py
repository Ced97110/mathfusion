import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 76, r'$F\subseteq K\subseteq E$', 'encre', 'l')
xs = [24, 45, 66]
top = [r'$j$', r'$jr$', r'$jr^2$']
bot = [r'$1$', r'$r$', r'$r^2$']
for x, a, b in zip(xs, top, bot):
    box(ax, x, 42, 20, 13, 'varie', label=a)
    box(ax, x, 27, 20, 13, 'sujet', label=b)
brace(ax, 24, 86, 57, 'sujet', label=r'$[K:F]=3$', down=False)
line(ax, [(21, 27), (19, 27), (19, 55), (21, 55)], 'varie', lw=0.8)
text(ax, 12, 41, r'$[E:K]=2$', 'varie', 's', rot=90)
text(ax, 44, 15, r'$[E:F]=[E:K]\,[K:F]=2\times3=6$', 'resultat', 'm')
save(fig, '62-064')
