// Scroll-to-Top
const goUp = document.querySelector(".go-up");

goUp.addEventListener("click", () => {
  document.documentElement.scrollTop = 0;
});

window.addEventListener("scroll", () => {
  if (window.scrollY < 250) {
    goUp.style.right = -100 + "px";
  } else {
    goUp.style.right = 5 + "px";
  }
});
