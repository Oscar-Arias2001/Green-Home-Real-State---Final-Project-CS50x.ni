$("#contact").on("submit", (event) => {
  event.preventDefault();
  $.ajax({
    data: {
      fullname: $("#fullname").val(),
      email: $("#email").val(),
      phone: $("#phone").val(),
      asunto: $("#asunto").val(),
    },
    type: "POST",
    url: "/contact",
  }).done((data) => {
    if (data.error) {
      swal({
        title: "Error en formulario de contacto",
        text: data.error,
        icon: "error",
      });
    } else if (data.correct) {
      window.location.href = "/";
    }
  });
});
