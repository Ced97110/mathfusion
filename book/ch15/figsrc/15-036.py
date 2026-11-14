import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(96)
rows=[(78,'sujet',r'$3x+5$'),(54,'varie',r'$3\times4+5$'),(30,'varie',r'$12+5$'),(6,'resultat',r'$17$')]
for y,r,l in rows: box(ax,6,y,32,12,r,label=l,size='l')
labs=[r'on remplace $x$ par 4',r'on calcule $3\times4$',r'on calcule $12+5$']
for k,(y,_,_) in enumerate(rows[:3]):
    arrow(ax,(22,y),(22,y-12),'varie'); text(ax,28,y-6,labs[k],'varie','s',ha='left')
save(fig,'15-036')
