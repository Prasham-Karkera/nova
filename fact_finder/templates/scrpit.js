const urlbtn = document.querySelector("#urlbtn");       // login
const textbtn = document.querySelector("#textbtn");      //signup
const sbar = document.querySelector("#sbar");      //form
const switchbtn = document.querySelectorAll("#switchbtn");       //switch

let current = 1;

function tab2() {
    sbar.style.marginLeft = "-100%";
    switchbtn[current - 1].classList.add("active");
}

function tab1() {
    sbar.style.marginLeft = "0%";
    switchbtn[current - 1].classList.remove("active");
}
