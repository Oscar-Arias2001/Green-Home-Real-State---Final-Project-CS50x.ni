$("#register").on("submit", (event) => {
  event.preventDefault();
  $.ajax({
    data: {
      name: $("#name").val(),
      email: $("#email").val(),
      city: $("#city").val(),
      address: $("#address").val(),
      phone: $("#phone").val(),
      password: $("#password").val(),
      confirmation_password: $("#confirmation_password").val(),
    },
    type: "POST",
    url: "/register",
  }).done((data) => {
    if (data.error) {
      swal({
        title: "Error en Registro de Usuario",
        text: data.error,
        icon: "error",
      });
    }
  });
});

