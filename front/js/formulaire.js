// Gestion de la requête API
const btn = document.getElementById('predire')

btn.addEventListener('click', () => {
  // Récupération des données du formulaire

  var myForm = document.getElementById('houseForm')

  var formData = new FormData(myForm)

  var request = new XMLHttpRequest();
  request.open("POST", "http://127.0.0.1:8000/house_price/");
  request.onreadystatechange = function () {

    // // attente de réponse de l'api puis choix de l'action en fonction de la réponse
    if (request.readyState === request.DONE && request.status === 200) {
      var resultHouse = JSON.parse(request.responseText)
      var pReponse = document.getElementById('reponse')
      pReponse.innerHTML = "Votre bien est estimé à: " + Math.round(resultHouse * 100) / 100 + " $";
    }

  }
  request.send(formData);
});


// Gestion de l'animation
const slides = [...document.querySelectorAll(".slide")]

const sliderData = {
  direction: 0,
  slideOutIndex: 0,
  slideInIndex: 0
}

const directionButton = [...document.querySelectorAll(".direction-btn")];

directionButton.forEach(btn => btn.addEventListener("click", handleClick))

function handleClick(e) {
  getDirection(e.target)

  slideOut();
}

function getDirection(btn) {
  sliderData.direction = btn.className.includes("next") ? 1 : 0

  sliderData.slideOutIndex = slides.findIndex(slide => slide.classList.contains("active"))

  if (sliderData.slideOutIndex + sliderData.direction > slides.length - 1) {
    sliderData.slideInIndex = 0;

  } else if (sliderData.slideOutIndex + sliderData.direction < 0) {
    sliderData.slideInIndex = slides.length - 1

  } else {
    sliderData.slideInIndex = sliderData.slideOutIndex + sliderData.direction
  }
}

function slideOut(){
  slideAnimation({
    el: slides[sliderData.slideInIndex],
    props: {
      display: "flex",
      transform: `translateY(${sliderData.direction < 0 ? "100%" : "-100%"})`,
      opacity: 0
    }
  })

  slideAnimation({
    el: slides[sliderData.slideOutIndex],
    props: {
      transition: "transform 0.4s cubic-bezier(0.74, -0.34,1,1.19), opacity 0.4s ease-out",
      transform:`translateY(${sliderData.direction < 0 ?"-100%":"100%" })`,
      opacity: 0
    }
  })

  slides[sliderData.slideOutIndex].addEventListener("transitionend", slideIn)
}

function slideAnimation(animationObject){
  for(const prop in animationObject.props){
    animationObject.el.style[prop] = animationObject.props[prop]
  }
}

function slideIn(e){
  slideAnimation({
    el : slides[sliderData.slideInIndex],
    props: {
      transition: "transform 0.4s ease-out, opacity 0.6s ease-out",
      transform: "translateY(0%)",
      opacity:1
    }
  })

  slides[sliderData.slideInIndex].classList.add("active");

  slides[sliderData.slideOutIndex].classList.remove("active");
  e.target.removeEventListener("transitionend", slideIn)
  slides[sliderData.slideOutIndex].style.display = "none";
}
