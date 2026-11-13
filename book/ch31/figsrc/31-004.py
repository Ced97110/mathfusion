import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cols=[(4,5),(34,26),(66,20)]
text(ax,13,56,'côté connu','sujet','s'); text(ax,48,56,'diviseur : le rapport','varie','s'); text(ax,77,56,'côté cherché','resultat','s')
rows=[('4','÷ 0,8660 (cos)','4,62'),('3','÷ 0,8391 (tan)','3,58'),('10','÷ 0,4226 (sin)','23,66')]
for i,(a,b,c) in enumerate(rows):
    y=38-i*14
    box(ax,4,y,18,10,'sujet',label=a,size='l')
    box(ax,30,y,36,10,'varie',label=b,size='m')
    box(ax,72,y,14,10,'resultat',label=c,size='m')
    arrow(ax,(22,y+5),(30,y+5),'encre'); arrow(ax,(66,y+5),(72,y+5),'encre')
text(ax,44,4,'même action, seul le diviseur change','encre','s')
save(fig,'31-004')
