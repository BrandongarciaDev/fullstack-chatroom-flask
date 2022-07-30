setActiveLink = () =>{
    let activeLink = window.location.href;
    let links = document.querySelectorAll('.list__item');

    links.forEach( (element)=>{

        if(element.childNodes[1].href === activeLink){
            element.classList.add('active');
        }

    })

}

setActiveLink();


