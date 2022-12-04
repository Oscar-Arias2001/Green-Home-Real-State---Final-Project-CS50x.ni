$("#register").on("submit", (event) => {
  event.preventDefault();
  $.ajax({
    datos: {
      name: $("#name").val(),
      email: $("#email").val(),
      country: $("#country").val(),
      address: $("#address").val(),
      phone: $("#phone").val(),
      password: $("#password").val(),
    },
    type: "POST",
    url: "/register",
  }).done((dato) => {
    if (dato.error) {
      alert(dato.error);
    }
  });
});
