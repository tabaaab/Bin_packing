/*********************************************
 * OPL 12.10.0.0 Model
 * Author: abtabaa
 * Creation Date: 28 févr. 2021 at 16:18:11
 *********************************************/


int n=...;
range objet = 1..n;
range boite = 1..n;
int v =...;
int ai[objet]=...; 

dvar boolean x[boite][objet];
dvar boolean y[boite];




minimize sum ( i in boite) y[i];

subject to {
  forall (i in boite)
    premiere_contrainte:
    sum(j in objet) ai[j]*x[i][j] <= v*y[i];
  forall (j in objet )
    deuxieme_contrainte :
    sum(i in objet) x[i][j] ==1;
}

execute {
  writeln("le nombre minimum des boites et la solution optimale est : ",cplex.getObjValue());
}