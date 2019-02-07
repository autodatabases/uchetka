document.querySelector('.topPanel').setAttribute('style', 'width: 66.5%');
// анимация панели донора после загрузки страницы
window.onload = function(){
	document.querySelector('.menu').classList.add('hideMenu')
	
} 
// Функиця изменения параметров донора
function editDonor(block) {
	var all_select = block.getElementsByTagName('select');
	for (var i_param = 0; i_param < all_select.length; i_param++) {
		if ((all_select[i_param].getAttribute('id') == 'all_marks') || (all_select[i_param].getAttribute('id') == 'all_models') || (all_select[i_param].getAttribute('id') == 'all_generations')) {
			continue;
		}
		all_select[i_param].removeAttribute('disabled');
	};
	block.querySelector('#donorProbeg').removeAttribute('disabled');
	block.querySelector('#donorVin').removeAttribute('disabled');
	block.querySelector('#save').removeAttribute('disabled');
	block.querySelector('#edit').setAttribute('disabled', '');
}
// Функция сохранения параметров донора
function saveDonor() {
	var block = document.querySelector('.donorContent');
	var all_select = block.getElementsByTagName('select');
	var probeg = block.querySelector('#donorProbeg');
	var vin = block.querySelector('#donorVin');
	var idDonor = document.querySelector('#idDonor').value;
	$.ajax({
		url: '/lk/detals_list/save_donor/',
		type: 'post',
		data: {
			'csrfmiddlewaretoken': csrftoken,
			'mark' : all_select[0].options[all_select[0].selectedIndex].value,
			'model' : all_select[1].options[all_select[1].selectedIndex].value,
			'generation' : all_select[2].options[all_select[2].selectedIndex].value,
			'year' : all_select[3].options[all_select[3].selectedIndex].value,
			'kuzov' : all_select[4].options[all_select[4].selectedIndex].value,
			'engine_type' : all_select[5].options[all_select[5].selectedIndex].value,
			'engine_size' : all_select[6].options[all_select[6].selectedIndex].value,
			'transmission' : all_select[7].options[all_select[7].selectedIndex].value,
			'color' : all_select[8].options[all_select[8].selectedIndex].value,
			'helm' : all_select[9].options[all_select[9].selectedIndex].value,
			'privod' : all_select[10].options[all_select[10].selectedIndex].value,
			'vin' : vin.value,
			'probeg' : probeg.value,
			'idDonor' : idDonor
		},
		success: function (data) {
			var block = document.querySelector('.buttonBlock');
			for (var i_param = 0; i_param < all_select.length; i_param++) {
				all_select[i_param].setAttribute('disabled', '');
			};
			probeg.setAttribute('disabled', '');
			vin.setAttribute('disabled', '');
			block.querySelector('#save').setAttribute('disabled', '');
			block.querySelector('#edit').removeAttribute('disabled');
		}, 
		error: function(){
			alert('error!');
	    }
	});
}
/// Парметры размещения детали
function paramsSklad(radiobutton) {
	var all_inputSklad = document.querySelector('.contentBlock').querySelectorAll('#all_years');
	var selectStockRoom = document.querySelector('.bottomSettingButtons').querySelector('.custom-select');
	if (radiobutton.getAttribute('id') == 'customRadio1'){
		for	(var i = 0; i<all_inputSklad.length; i++) {
			all_inputSklad[i].removeAttribute('disabled');
		}
		selectStockRoom.removeAttribute('name');
		selectStockRoom.setAttribute('disabled', '');
	} else {
		for	(var i = 0; i<all_inputSklad.length; i++) {
			all_inputSklad[i].setAttribute('disabled', '');
		}
		selectStockRoom.setAttribute('name', 'selectStock');
		selectStockRoom.removeAttribute('disabled');
	}
}
// функция загрузки фотографии с последующим отображением
function load_photo(inputFile){
	$.ajax({
			url: '/lk/detals_list/save_donor/',
			type: 'post',
			data: {
				'csrfmiddlewaretoken': csrftoken,
			},
			success: function (data) {
			}
		});
}
// Счетчик
function price_all(){
  var price = document.querySelectorAll("price_available");
  var i = 0;
  while (i < price.length){
    document.getElementById("price_all").innerHTML += price[i].value;
  }
  document.getElementById("price_all").innerHTML = parseInt(document.getElementById("price_all").innerHTML) + parseInt(document.querySelector('.contentBlock').querySelector('.active').querySelector('#price_available').value);

  //if (document.getElementById("nala").disabled == true){
  //  document.getElementById("price_all").innerHTML = 0;
  //}
}
function sub(){
  var price_all = document.querySelectorAll("price_available");
  document.getElementById("price_all").innerHTML -= document.getElementById("price_available").innerHTML;
}

function qsd(){
}