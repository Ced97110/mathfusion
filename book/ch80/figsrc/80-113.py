import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
rows=[('110',[1,1,0],'sujet'),('101',[1,0,1],'sujet'),('011',[0,1,1],'resultat')]
for r,(lab,dg,role) in enumerate(rows):
    y=54-r*12
    text(ax,10,y,lab,role,'m')
    for j,d in enumerate(dg): box(ax,24+j*10,y-4,8,8,role,label=str(d),size='m')
text(ax,50,44,'+','varie','l',ha='left') if False else None
text(ax,70,42,'chiffre par chiffre','varie','s'); text(ax,70,34,'(1 + 1 = 0)','varie','s')
line(ax,[(10,14),(78,14)],'fixe')
for x,l,role in [(18,'110','sujet'),(44,'101','sujet'),(70,'011','resultat')]:
    disc(ax,x,14,1.6,role); text(ax,x,8,l,role,'s')
text(ax,44,22,'trois points alignés','resultat','s')
save(fig,'80-113')
