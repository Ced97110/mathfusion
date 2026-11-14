import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
x0=14; L=62; h=10
def bar(y,a,lab_a,lab_b,name):
    box(ax,x0,y,a*L,h,'sujet',label=lab_a,size='s',r=0.01)
    box(ax,x0+a*L,y,(1-a)*L,h,'autre',label=lab_b,size='s',r=0.01)
    text(ax,x0,y+h+3,name,'encre','s',ha='left')
bar(36,0.36,r'$0{,}36$',r'$0{,}64$','triangle 3, 4, 5')
bar(14,25/169,r'$\frac{25}{169}$',r'$\frac{144}{169}$','triangle 5, 12, 13')
text(ax,x0+0.18*L,58,r'$\sin^2 A$','sujet','s')
text(ax,x0+0.7*L,58,r'$\cos^2 A$','autre','s')
brace(ax,x0,x0+L,13,'resultat',label='somme = 1')
save(fig,'26-041')
