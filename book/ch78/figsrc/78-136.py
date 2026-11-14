import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for cx, tit in ((22, '$\\mathbb{R}$'), (66, '$\\mathbb{C}$')):
    line(ax, [(cx - 17, 35), (cx + 17, 35)], 'fixe'); line(ax, [(cx, 20), (cx, 50)], 'fixe')
    text(ax, cx, 58, tit, 'encre', 'xl')
disc(ax, 31, 35, 2, 'sujet'); text(ax, 31, 30.5, '$x=1$', 'sujet', 's')
text(ax, 22, 15, '$\\bar{x}=x$', 'varie', 'm')
disc(ax, 66, 45, 2, 'sujet'); text(ax, 72, 45, '$i$', 'sujet', 'm')
disc(ax, 66, 25, 2, 'autre'); text(ax, 72.5, 25, '$-i$', 'autre', 'm')
arrow(ax, (63.5, 42), (63.5, 28), 'varie', curve=0.4)
text(ax, 66, 15, '$\\bar{x}=-x$', 'varie', 'm')
box(ax, 8, 2, 28, 9, 'resultat', label='$ji=ij$')
box(ax, 52, 2, 28, 9, 'limite', label='$ji=-ij$')
save(fig, '78-136')
