import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
rows=[('1/3 = 0,','3',1,'1 chiffre'),('1/7 = 0,','1 4 2 8 5 7',6,'6 chiffres'),('1/11 = 0,','0 9',2,'2 chiffres')]
c=8
for i,(a,d,n,b) in enumerate(rows):
    y=44-i*19
    text(ax,2,y+4,a,'sujet','m',ha='left')
    box(ax,24,y,n*c,8,'sujet',label=d)
    text(ax,24+n*c+3,y+4,'…','sujet','m',ha='left')
    brace(ax,24,24+n*c,y,'fixe',label=b)
save(fig,'08-097')
