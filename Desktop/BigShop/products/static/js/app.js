// Pour le menu dropdown
var btnToggleDropdown = document.querySelector('a.dropdown')
var dropdown = document.querySelector('.dropdown-menu')

btnToggleDropdown.addEventListener('click', function(event){
    if(dropdown.classList.contains('show-dropdown')){
        dropdown.classList.remove('show-dropdown')
        console.log('dropdown')
    }
    else{
        dropdown.classList.add('show-dropdown')
    }
})

// Pour le toggle menu > 992px
var btnToggle = document.querySelector('.btn-toggle__header')
var menu = document.querySelector('.box__header')

btnToggle.addEventListener('click', function(event){
    if(menu.classList.contains('show-menu')){
        menu.classList.remove('show-menu')
    }
    else{
        menu.classList.add('show-menu')
    }
})


// le message info search
var btnSearch = document.querySelector('.btn-search')

btnSearch.addEventListener('click', function(event){
    var info = document.querySelector('.search-info')
    if(info.textContent != ""){
        console.log("suis la")
        window.setTimeout(function(){
            info.style.display = 'flex'
        }, 10000)
    }
})