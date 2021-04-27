/*********************************************
 * OPL 12.10.0.0 Model
 * Author: abtabaa
 * Creation Date: 24 févr. 2021 at 22:42:04
 *********************************************/

 //creation des parametres 
 
 
int n = ...;
range objet = 1..n; //liste des objets
range boite = 1..n; //liste des bins
float v= ...; // en cas des capacité réelle 
float ai[objet]=...;//volume des objets

dvar boolean x[boite][objet];
dvar boolean y[boite];

minimize sum(i in boite) y[i];

subject to{
  
   forall(i in boite)
    constraint_1:
    sum(j in objet) ai[j]*x[i][j] <= v*y[i];
  
  forall(j in objet)
    constraint_2:
    sum(i in objet) x[i][j] ==1;
  
 
    
}
execute{
  
  if(cplex.getCplexStatus()==1){
    writeln("objet placé dans boite :",x.solutionValue)
  }
  else{
    writeln("erreur");
  }
  
}