const foodType= document.querySelectorAll(".foodType");
function HandleClick(){
    console.group("test");
        foodType.style.backgroundColor = "#FFB800";
}

foodType.addEventListener("click",HandleClick);