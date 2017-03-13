$(document).ready(function () {
  // Create a Stripe client
  var stripe = Stripe('pk_live_GgOomyKy2RnxX7npj2YZV0XR');
  // pk_test_QvqFPIH6h4uZRvIGHSGAQaKB TEST KEY
  // Create an instance of Elements
  var elements = stripe.elements();

  // Custom styling can be passed to options when creating an Element.
  // (Note that this demo uses a wider set of styles than the guide below.)
  var style = {
    base: {
      color: '#32325d',
      lineHeight: '24px',
      fontFamily: 'Helvetica Neue',
      fontSmoothing: 'antialiased',
      fontSize: '16px',
      '::placeholder': {
        color: '#aab7c4'
      }
    },
    invalid: {
      color: '#fa755a',
      iconColor: '#fa755a'
    }
  };

  // Create an instance of the card Element
  var card = elements.create('card', {style: style});

  // Handle real-time validation errors from the card Element.
  $(document).on('click', '#new_card', function () {
    $(this).parent().html(
      '<form action="edit_card" method="post" id="change_card_form">' +
        '<div id="card"></div>' +
        '<div id="card-errors"></div>' +
        '<input type="hidden" name="last_4_digits" id="id_last_4_digits" value="">' +
        '<input type="hidden" name="stripe_token" id="id_stripe_token" value="">' +
        '<input type="submit" name="" value="Change Card">' +
      '</form>'
    )
    // Add an instance of the card Element into the `card-element` <div>
    card.mount('#card');

    card.addEventListener('change', function(event) {
    const displayError = document.getElementById('card_errors');
      if (event.error) {
        displayError.textContent = event.error.message;
      } else {
        displayError.textContent = '';
      }
    });

    // Handle form submission
    var form = document.getElementById('change_card_form');
    form.addEventListener('submit', function(event) {
      event.preventDefault();

      stripe.createToken(card).then(function(result) {
        if (result.error) {
          // Inform the user if there was an error
          var errorElement = document.getElementById('card-errors');
          errorElement.textContent = result.error.message;
        } else {
          // Send the token to your server
          stripeTokenHandler(result.token);
        }
      });
    });
});

$('#reset').on('click',function(){
    console.log("reset");
    $('#cardcontainer').html(
        '<button type="button" id="new_card">Change Card</button>'
    )
    card.unmount('#card');
});


  window.onclick = function(event) {
    if (event.target == $('body')) {
        $('body').style.display = "none";
    }
  }

  function stripeTokenHandler(token) {
    // Insert the token ID into the form so it gets submitted to the server
    var form = document.getElementById('change_card_form');
    var stripe_token = document.getElementById('id_stripe_token');
    var last_4 = document.getElementById('id_last_4_digits');
    stripe_token.setAttribute('value', token.id);
    last_4.setAttribute('value', token.card.last4);


    // Submit the form
    form.submit();
  }
});
