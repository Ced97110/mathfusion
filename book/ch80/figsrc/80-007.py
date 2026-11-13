import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
lab=[('de 2','−1','varie'),('de 3','−1','varie'),('de 5','−1','varie'),('de 6','+1','autre'),('de 10','+1','autre'),('de 15','+1','autre'),('de 30','−1','sujet')]
w_,g=10.5,1.5; x0=(88-(7*w_+6*g))/2
for i,(a,b,r) in enumerate(lab): box(ax,x0+i*(w_+g),14,w_,14,r,label=a+'\n'+b,size='s')
c=lambda i:x0+i*(w_+g)
brace(ax,c(0),c(2)+w_,32,'varie','retire',down=False)
brace(ax,c(3),c(5)+w_,32,'autre','remet',down=False)
brace(ax,c(6),c(6)+w_,32,'sujet','retire\nencore',down=False)
text(ax,44,5,'bilan de 30 : un seul retrait','resultat','m')
save(fig,'80-007')
