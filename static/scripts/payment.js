// Stripe
Stripe.setPublishableKey('pk_test_6pRNASCoBOKtIshFeQd4XMUh');

StripeI18n = {
  es: {
    errors: {
      incorrect_number: "El número de tarjeta es incorrecto.",
      invalid_number: "El número de tarjeta no es un número de tarjeta válido.",
      invalid_expiry_month: "El mes de caducidad de la tarjeta no es válido.",
      invalid_expiry_year: "El año de caducidad de la tarjeta no es válido.",
      invalid_cvc: "El código de seguridad de la tarjeta no es válido.",
      expired_card: "La tarjeta ha caducado.",
      incorrect_cvc: "El código de seguridad de la tarjeta es incorrecto.",
      incorrect_zip: "Falló la validación del código postal de la tarjeta.",
      card_declined: "La tarjeta fué rechazada.",
      missing: "El cliente al que se está cobrando no tiene tarjeta",
      processing_error: "Ocurrió un error procesando la tarjeta.",
      rate_limit:  "Ocurrió un error debido a consultar la API demasiado rápido. Por favor, avísanos si recibes este error continuamente."
    }
  }
};
//END

// jquery.payment
jQuery(function($) {
  $('#credit_card_number').payment('formatCardNumber');
  $('#credit_card_expiry').payment('formatCardExpiry');
  $('#cvc').payment('formatCardCVC');
  
  $('#credit_card_number').on('input', function(event) {
    var number = $(this).val();
    var type = $.payment.cardType(number);
    $(this).next().removeClass('visa mastercard amex').addClass(type);
  });
});
// END

// Forms behaviour
function sendDataWithHiddenForm(token, plan) {
  var $hidden_form = $('.lp-pom-form form');

  $hidden_form.append($('<input type="hidden" name="stripeToken" />').val(token));

  $hidden_form.append($('<input type="hidden" name="plan" />').val(plan));
  
  // $hidden_form.next('.lp-pom-button').get(0).click();
  
  $hidden_form.get(0).submit();
};

function stripeResponseHandler(status, response) {
  var $visible_form = $('#payment');

  $visible_form.find('button').prop('disabled', false);

  if (response.error) {
    var message = StripeI18n.es.errors[response.error.code] || response.error.message
    return alert(message);
  }

  var token = response.id;
  var plan = $visible_form.find('input[name=plan]:checked').val();
  sendDataWithHiddenForm(token, plan);  
};

jQuery(function($) {
  $('#payment').submit(function(event) {
    event.preventDefault();
    var $form = $(this);

    // Disable the submit button to prevent repeated clicks
    $form.find('button').prop('disabled', true);

    // Fill expiry fields
    expiry_data = $('#credit_card_expiry').payment('cardExpiryVal')
    $('#credit_card_expiry_month').val(expiry_data.month)
    $('#credit_card_expiry_year').val(expiry_data.year)

    Stripe.card.createToken($form, stripeResponseHandler);
  });
});
// END

// URL with email behaviour
jQuery(function($) {
  var email = location.hash.replace('#', '');
  if(email == '') {
    return;
  }
  
  var $hidden_form = $('.lp-pom-form form'); 

  $hidden_form.append($('<input type="hidden" name="email" />').val(email));
});
// END