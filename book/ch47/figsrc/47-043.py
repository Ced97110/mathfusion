import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
s=11
def sq(x,y,A,B):
    poly(ax,[(x,y),(x+s,y),(x+s,y+s),(x,y+s)],'fixe')
    C=[(x,y),(x+s,y),(x+s,y+s),(x,y+s)]
    disc(ax,C[A][0]+[1.8,-1.8,-1.8,1.8][A],C[A][1]+[1.8,1.8,-1.8,-1.8][A],1.5,'sujet')
    disc(ax,C[B][0]+[1.8,-1.8,-1.8,1.8][B],C[B][1]+[1.8,1.8,-1.8,-1.8][B],1.5,'varie')
for row,(ops,fin) in enumerate([(('s','r'),(2,1)),(('r','s'),(0,3))]):
    y=52-row*38
    sq(5,y,0,1); 
    mid=((1,0) if ops[0]=='s' else (1,2))
    sq(34,y,*mid); sq(63,y,*fin)
    for i,x in enumerate((17,46)):
        arrow(ax,(x,y+s/2),(x+14,y+s/2),'varie'); text(ax,x+7,y+s/2+3.5,ops[i],'varie','m')
    text(ax,44,y+s+8,'d’abord '+ops[0]+', puis '+ops[1],'encre','s')
text(ax,76,40,'≠','limite','xl')
text(ax,16,4,'rond bleu et rond orange suivent le carré','fixe','s') if False else None
save(fig,'47-043')
