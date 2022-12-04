$("#register").on("submit", (event) => {
  event.preventDefault();
  $.ajax({
    data: {
      name: $("#name").val(),
      email: $("#email").val(),
      country: $("#country").val(),
      address: $("#address").val(),
      phone: $("#phone").val(),
      password: $("#password").val(),
    },
    type: "POST",
    url: "/register",
  }).done((data) => {
    if (data.error) {
      alert(data.error);
    }
  });
});
