$("#login").on("submit", (event) => {
  event.preventDefault();
  $.ajax({
    data: {
      email_s: $("#email_s").val(),
      password_s: $("#password_s").val(),
    },
    type: "POST",
    url: "/log_in",
  }).done((data) => {
    if (data.error) {
      swal({
        title: "Error en Inicio de Sesión",
        text: data.error,
        icon: "error",
      });
    } else if (data.correct) {
      window.location.href = "/";
    }
  });
});
