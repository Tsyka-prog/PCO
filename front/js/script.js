

// Animation accueil
const banniere = document.querySelector('.banniere')
const slider = document.querySelector('.background')
const logo = document.querySelector('#logo')
const titre = document.querySelector('.titre')
const partie = document.querySelectorAll('.partie')


gsap.fromTo(banniere,1, {height: "0%"}, {height:"80%",ease: Power2.easeInOut})
gsap.fromTo(banniere,1.2, {width: "100%"}, {width:"80%",ease: Power2.easeInOut})
gsap.fromTo(slider, 1.2, {x: "-100%"}, {x: '0%', ease: Power2.easeInOut}, "-=1.2")
gsap.from(logo, 1, {x:"-100%", ease: Back.easeOut.config(1.7)}, "-=2")
gsap.from(partie, 1, {opacity:0, ease: "power1", stagger:{
  each: 0.14,
  from: "center"
}});


