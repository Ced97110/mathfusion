import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
u=3.2
def case(y,a,b,c,tot):
    text(ax,44,y+22,f'$c=\\sqrt{{{a}^2+{b}^2}}=\\sqrt{{{a*a+b*b}}}={c}$','resultat','m')
    box(ax,8,y+9,a*u,8,'fixe',label=str(a),size='s')
    box(ax,8+a*u,y+9,b*u,8,'fixe',label=str(b),size='s')
    text(ax,8+(a+b)*u+3,y+13,f'${a}+{b}={tot}$','limite','s',ha='left')
    box(ax,8,y,c*u,8,'resultat',label=f'$c={c}$',size='s')
case(44,6,8,10,14)
case(4,5,12,13,17)
save(fig,'22-133')
