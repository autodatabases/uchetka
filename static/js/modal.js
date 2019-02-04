// Вспывающее окно выбора авто
$('.button').click(function(){
  var buttonId = $(this).attr('id');
  $('#modal-container').removeAttr('class').addClass(buttonId);
  $('body').addClass('modal-active');
})

$('#close').click(function(){
  $('#modal-container').addClass('out');
  $('body').removeClass('modal-active');
});

