
const btn = document.getElementById('predire')

btn.addEventListener('click', () => {
  // Récupération des données du formulaire
 
  var myForm = document.getElementById('houseForm')

  var formData = new FormData(myForm)
  console.log(formData.entries());
  
   var request = new XMLHttpRequest();
   request.open("POST", "https://house-price-pred-simplon.herokuapp.com/house_price/");
//   request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
   console.log(request.readyState);

   request.onreadystatechange = function () {
//     console.log('histoire de voir');
     console.log(request.readyState);
// // attente de réponse de l'api puis choix de l'action en fonction de la réponse
     if (request.readyState === request.DONE && request.status === 200) {
     var resultHouse = JSON.parse(request.responseText)
     console.log('toto');
     console.log(resultHouse);
     var pReponse = document.getElementById('reponse')
     pReponse.innerHTML = resultHouse;
   }

}


 request.send(formData);
console.log('fini');

});


