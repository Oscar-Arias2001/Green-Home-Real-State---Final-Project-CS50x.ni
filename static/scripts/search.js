document.addEventListener("keyup", (e) => {
  if (e.target.matches("#buscador")) {
    if (e.key === "Escape") e.target.value = "";

    document.querySelectorAll(".card").forEach((propertie) => {
      propertie.textContent.toLowerCase().includes(e.target.value.toLowerCase())
        ? propertie.classList.remove("filtro")
        : propertie.classList.add("filtro");
    });
  }
});

// document.addEventListener("keyup", (e) => {
//     if (e.target.matches("#buscador1")) {
//       if (e.key === "Escape") e.target.value = "";
  
//       document.querySelectorAll(".card").forEach((propertie) => {
//         propertie.textContent.toLowerCase().includes(e.target.value.toLowerCase())
//           ? propertie.classList.remove("filtro")
//           : propertie.classList.add("filtro");
//       });
//     }
//   });