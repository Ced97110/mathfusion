import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
Y=[56,45,34,23,12]
N=[('156',24,'sujet'),('−12',21,'varie'),('36',24,'sujet'),('−36',24,'varie'),('0',24,'resultat')]
for (s,x,r),y in zip(N,Y): text(ax,x,y,s,r,'l',ha='right')
line(ax,[(28,60),(28,51)],'fixe'); line(ax,[(28,51),(40,51)],'fixe')
text(ax,34,56,'12','autre','l'); text(ax,34,45,'13','resultat','l')
line(ax,[(6,39.5),(26,39.5)],'fixe'); line(ax,[(6,17.5),(26,17.5)],'fixe')
L=['12 dans 15 : 1 fois','1 × 12 = 12','15 − 12 = 3, puis le 6 : 36','3 × 12 = 36','reste 0, quotient 13']
R=['varie','varie','sujet','varie','resultat']
for s,r,y in zip(L,R,Y): text(ax,46,y,s,r,'s',ha='left')
for y in Y: line(ax,[(30,y-5.5)] if False else [(28.5,y),(30,y)],'fixe') if False else None
save(fig,'21-108')
