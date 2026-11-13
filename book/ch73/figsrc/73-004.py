import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
w,h,sh=30,24,6; x0,x1,y0=8,46,16
poly(ax,[(x0,y0),(x0+w,y0),(x0+w,y0+h),(x0,y0+h)],'sujet')
poly(ax,[(x1,y0),(x1+w,y0),(x1+w+sh,y0+h),(x1+sh,y0+h)],'sujet')
for x in (x0,x1):
    text(ax,x+w/2+(0 if x==x0 else sh/2),y0+h/2,'800 000 pixels','sujet','s')
    brace(ax,x,x+w,y0,'sujet','1 000 px')
text(ax,x0-3.5,y0+h/2,'800 lignes','sujet','s',rot=90)
text(ax,x1+w+sh+2.5,y0+h/2,'800 lignes','sujet','s',rot=90)
arrow(ax,(x0+w+2,y0+h/2),(x1-1,y0+h/2),'varie')
text(ax,x0+w+3,y0+h/2+3.5,'glisser','varie','s',ha='left')
text(ax,x0+w/2,y0+h+4,'avant','fixe','s'); text(ax,x1+w/2+sh/2,y0+h+4,'après','fixe','s')
text(ax,44,5,'toujours 800 000 pixels','resultat','m')
save(fig,'73-004')
