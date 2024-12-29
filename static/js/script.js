let btnBurger = document.getElementById('btn-burger');
let mobileMenu = document.getElementById('mobile-menu');


btnBurger.onclick=()=>{
    if(!mobileMenu.classList.contains('hidden')){
        mobileMenu.classList.add('hidden')
    }
    else{
        mobileMenu.classList.remove('hidden')
    }
}
