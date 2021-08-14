let searchForm=document.querySelector("#searchForm")
let pageLinks=document.getElementsByClassName("page-link")

if(searchForm){
  for(let i=0;i<pageLinks.length;i++){
    pageLinks[i].addEventListener("click",function(e){
      e.preventDefault()
      page=this.dataset.page
      console.log(page)
      searchForm.innerHTML+=`<input type="hidden" name="page" value="${page}">`
      searchForm.submit()
    })
  }
}