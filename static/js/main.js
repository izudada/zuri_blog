/*===== MENU SHOW Y HIDDEN =====*/
const navMenu = document.getElementById('nav-menu'),
    toggleMenu = document.getElementById('nav-toggle'),
    closeMenu = document.getElementById('nav-close'),
    hamburger = document.getElementById('hamburger')

// SHOW
toggleMenu.addEventListener('click', ()=>{
    navMenu.classList.toggle('show');
    toggleMenu.classList.toggle('hide')
})

// HIDDEN
closeMenu.addEventListener('click', ()=>{
    navMenu.classList.remove('show')
    toggleMenu.classList.remove('hide')
})

/*===== MOUSEMOVE HOME IMG =====*/
document.addEventListener('mousemove', move);
function move(e){
    this.querySelectorAll('.move').forEach(layer =>{
        const speed = layer.getAttribute('data-speed')

        const x = (window.innerWidth - e.pageX*speed)/120
        const y = (window.innerHeight - e.pageY*speed)/120

        layer.style.transform = `translateX(${x}px) translateY(${y}px)`
    })
}

/*===== GSAP ANIMATION =====*/
// NAV
gsap.from('.nav__logo, .nav__toggle', {opacity: 0, duration: 1, delay:2, y: 10})
gsap.from('.nav__item', {opacity: 0, duration: 1, delay: 2.1, y: 30, stagger: 0.2,})

// HOME
gsap.from('.home__container', {opacity: 0, duration: 1, delay:1.6, y: 30})
gsap.from('.intro', {opacity: 0, duration: 1, delay:1.8, y: 30})
gsap.from('.post', {opacity: 0, duration: 1, delay:2.1, y: 30})