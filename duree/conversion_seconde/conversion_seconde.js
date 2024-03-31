//-----------------------------------------------
// conversion 
/*-----------------------------------------------
/ Convertit des secondes en années, jours, heures
/ minutes et secondes restantes.
/----------------------------------------------*/


//-----------------------------------------------
// Version courte
//-----------------------------------------------
// Cette version permet de comprendre le contextee
// de la fonction et sa logique.

function conversion(seconde) {
  if (seconde == 0) { return "0 seconde"; }
  
  let durees = [31536000, 86400, 3600, 60];
  let noms = ["annee", "jour", "heure",
                "minute", "seconde"];

  let res = Array(4).fill(0);

  for (let i = 0; i < durees.length; i++) {
    res[i] = Math.floor(seconde / durees[i]);
    seconde = seconde % durees[i];
  }

  res.push(seconde)
  
  let nombre = res.filter(a => a != 0).length;
  
  let increment = res.filter(a => a != 0).length;
  let texte = "";
  
  for (let i = 0; i < res.length; i++) {
    if (res[i] > 0) {
      increment -= 1;
      texte += res[i].toString() + ' ';
      texte += noms[i];

      if (res[i] > 1) { texte += "s"; }
      if (nombre >= 2) {
        if (increment == 1) {
          texte += " et ";
        }
        else if (increment > 1){
          texte+= ", ";
        }
      } 
    }
  }
  
  return texte;
}



//-----------------------------------------------
// Application
//-----------------------------------------------

let secondes = [0, 90000, 45000000];
for (let seconde of secondes) {
  let res = C(seconde);
  console.log(res);
}



//-----------------------------------------------
// Version golf
//-----------------------------------------------
// Version condensee et optimisee du code, utili-
// sant des noms de variables courts et combinant
// certaines operations pour reduire la taille du
// code. Pour la beaute du geste !


const C=s=>{ if (s==0) return"0 seconde"; let d=[
31536e2,86400,3600,60],n=["annee","jour","heure",
"minute","seconde"],r=Array(4).fill(0);for(let i=
0;i<d.length;i++){r[i]=Math.floor(s/d[i]);s=s%d[i
]}r.push(s);let c=r.filter(a=>a!=0).length,i=c,u=
"";for(let j=0;j<r.length;j++)r[j]>0&&(i-=1,u+=r[
j]+" "+n[j]+(r[j]>1?"s":"")+(c>=2?i==1?" et ":i>1
?", ":"":""));return u}



//-----------------------------------------------
// Version detaillee
/*-----------------------------------------------
/ Cette version permet de suivre pas a pas l'exe-
/ cution de la fonction. */

function conversion_detaillee(seconde) {

  // Cas particulier.
  if (seconde == 0) {
    return "0 seconde";
  }

  // Initialisations.
  let durees = [31536000, 86400, 3600, 60];
  let nbr_duree = durees.length;
  let noms = ["annee", "jour", "heure",
                "minute", "seconde"];
  let res = Array(4).fill(0);
  let nbr_res = res.length;

  // Calculer les différentes quantités d'unites.
  for (let i = 0; i < nbr_duree; i++) {
    let valeur_sec = durees[i];
    res[i] = Math.floor(seconde / valeur_sec);
    seconde = seconde % valeur_sec;
  }
  res.push(seconde)

  // Calculer le nombre d'unites non nulles.
  let nbr_unites = 0;
  for (let i = 0; i < nbr_res; i++) {
    if (res[i] !== 0) {
      nbr_unites += 1;
    }
  }
  let increment = nbr_unites;

  // Gérer de l'affichage.
  let affichage = "";
  for (let i = 0; i < nbr_res; i++) {
    if (res[i] > 0) {

      increment -= 1;
      affichage += res[i].toString() + ' ';
      affichage += noms[i];

      // Ajouter le s
      if (res[i] > 1) {
        affichage += "s"; 
      }

      // Ajouter le "et" ou ","
      if (nbr_unites > 1) {
        if (increment === 1) {
          affichage += " et ";
        }
        else if (increment > 1){
          affichage+= ", ";
        }
      } 
    }
  }
  
  return affichage;
}



//-----------------------------------------------
// Version commentee
/*-----------------------------------------------
/ Similaire a la version detaillee, mais avec des
/ commentaires concis afin d'expliquer les etapes
/ principales de la fonction. */

function conversion_commentee(seconde) {

  // Si le nombres de secondes est 0,
  if (seconde == 0) {

    // retourner "0 seconde".
    return "0 seconde";

  }
  
  // Initialiser les différents sommes de durées.
  let durees = [31536000, 86400, 3600, 60];

  // Récupérer le nombre de durées.
  let nbr_duree = durees.length;

  // Initialiser les différents noms de durées.
  let noms = ["annee", "jour", "heure",
                "minute", "seconde"];

  // Initialiser un tableau avec des zéros pour
  // accueillir les quotients des divisions.
  let res = Array(4).fill(0);

  // Recuperer la longueur de res.
  let nbr_res = res.length;

  // De 0 a nombre de duree,
  for (let i = 0; i < nbr_duree; i++) {

    // recuperer le total de secondes à l'index i
    let valeur_sec = durees[i];

    // Diviser le nombre de secondes total par le
    // nombre courant de secondes et ajouter le
    // resultat à l'index i dans res.
    res[i] = Math.floor(seconde / valeur_sec);

    // Recuperer le nombre de secondes restantes.
    seconde = seconde % valeur_sec;
  }

  // Ajouter le nombre de secondes restantes au
  // tableau.
  res.push(seconde)
  
  // Initialiser un nombre d'unites à 0.
  let nbr_unites = 0;

  // De O au nombre de valeur dans res,
  for (let i = 0; i < nbr_res; i++) {

    // si la valeur de res à l'ind i n'est pas 0,
    if (res[i] !== 0) {

      // incrementer d'un la variable nombre
      // d'unités. 
      nbr_unites += 1;
    }
  }

  // Conserver cette valeur pour faire une incre-
  // mentation.
  let increment = nbr_unites;

  // Initialiser une variable pour l'affichage.
  let affichage = "";

  // De 0 au nombre de valeur dans res,
  for (let i = 0; i < nbr_res; i++) {

    // si la valeur de res à l'index i est plus 
    // grand que 0.
    if (res[i] > 0) {

      // desincrementer increment;
      increment -= 1;

      // ajouter la valeur de res à l'index i,
      affichage += res[i].toString() + ' ';

      // ajouter le nom de la duree à l'index i.
      affichage += noms[i];

      // Si la valeur de res à l'index i est plus
      // grand que 1,
      if (res[i] > 1) {
        
        // ajouter un s.
        affichage += "s"; 
      
      }

      // Si le nombre d'unites est plus grand
      // que 1,   
      if (nbr_unites > 1) {

        // et si increment est egal à 1,
        if (increment === 1) {

          // ajouter "et" à affichage.
          affichage += " et ";
        }

        // Sinon, si increment est plus grand que
        // la valeur 1.
        else if (increment > 1){

          // ajouter une virgule à affichage.
          affichage+= ", ";

        }
      } 
    }
  }
  
  // Retourner l'affichage.
  return affichage;
}












//