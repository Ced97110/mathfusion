import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
for k in range(1,6): text(ax,21.5+11*(k-1),55,str(k),'fixe','s')
for n,y in [(3,42),(4,31),(5,20)]:
    for k in range(1,n+1):
        box(ax,17+11*(k-1),y,9,7,'fixe' if k==1 else ('varie' if k==n else 'sujet'))
    text(ax,8,y+3.5,f'{n} !','sujet','m')
    text(ax,86,y+3.5,f'= {[1,2,6,24,120][n-1]}','resultat','m',ha='right')
brace(ax,17,70,18,'fixe',label='5 facteurs : de 1 à 5')
text(ax,21.5,4,'toujours 1 en premier','fixe','s'); line(ax,[(21.5,6),(21.5,9)],'fixe')
text(ax,64,4,'n en dernier','varie','s'); line(ax,[(65.5,6),(65.5,9)],'varie')
save(fig,'01-054')
