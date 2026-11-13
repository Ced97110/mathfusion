import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
cx=[16,44,72]
for x,l,r in zip(cx,['½ tour','¾ tour','¼ tour'],['sujet','varie','sujet']): box(ax,x-12,48,24,11,r,label=l,size='s')
for x,l,r in zip(cx,['½ tour','¼ tour','¾ tour'],['sujet','sujet','varie']): box(ax,x-12,24,24,11,r,label=l,size='s')
text(ax,44,63,r'$a_n$ en position $h$','varie','s')
arrow(ax,(44,47),(44,36),'varie'); text(ax,48,41.5,'échange de voisins','varie','s',ha='left')
brace(ax,4,56,24,'sujet',label=r'$n-1$ éléments restent',down=True)
text(ax,72,16,r'$a_n$ à droite','varie','s')
save(fig,'45-133')
