let alertWrapper=document.querySelector('.alert')
let alertClose=document.querySelector('.alert__close')

function hide(){
  console.log("Clicked!")
  alertWrapper.style.display='none'
}

if(alertWrapper){
  console.log("Inside")
  alertClose.addEventListener("click",hide)
}