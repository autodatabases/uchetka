// анимация панели донора после загрузки страницы
window.onload = donorPanelAnimation();

// Функция при прокрутке списка деталей
document.querySelector('.addDetalsPanel').onscroll = function() {
  	var blockTabs = document.querySelector('.tabsDetalsName');
  	var all_tab = blockTabs.querySelectorAll('.titleDetal');
  	var activeTabDetail = blockTabs.querySelector('.activeTab');
  	var positionActiveTabDetail = activeTabDetail.getBoundingClientRect();
  	var activeTabCount = parseInt(activeTabDetail.getAttribute('data-content'));

  	if (positionActiveTabDetail.top <=93) {
  		activeTabDetail.classList.add('topfixed');
  		all_tab[activeTabCount].classList.add('nextTab');
  	}

  	if (all_tab[activeTabCount-2].getBoundingClientRect().top > 50) {
  		activeTabDetail.classList.remove('topfixed');
  		blockTabs.classList.remove('fixedTab');
  		all_tab[activeTabCount].classList.remove('nextTab');
  	}

}

function change_group_detal(tab) {
	document.querySelector('.activeTab').classList.remove('activeTab');
	tab.classList.add('activeTab');
}

function change_detal(tab) {

	function change_tab() {
		activeTab.classList.remove('activeTab');
		activeTab.classList.remove('topfixed');

		tab.classList.add('activeTab');

		if (tab.getAttribute('data-content') == 1) {
			tab.parentElement.classList.add('firstTabActive');
			tab.classList.add('topfixed');
		} else {
			tab.parentElement.classList.remove('firstTabActive');
			all_tab[pk_active_tab].classList.remove('nextTab');
		}

			// содержимое вкладок
			var oldParams = document.querySelector('.contentBlock').querySelector('.active');
			var newParams = document.querySelector('.contentBlock').querySelector('div[data-content="'+pk_new_content+'"]');
			contentBlock.classList.add('hide'); // Свернуть блок содержимго

			setTimeout(function() {
				oldParams.classList.remove('active');
				newParams.classList.add('active');
				contentBlock.classList.remove('hide');	
			}, 350);// Заддержка выполения
	}

	var tabClass = tab.getAttribute('class');
	if (tabClass.indexOf('active') == -1) { // если нажали на неактивную вкладку
		var contentBlock = document.querySelector('.contentBlock');
		var activeContent = contentBlock.querySelector('.active');
		var block_detals_name = document.querySelector('.tabsDetalsName');
		var all_tab = block_detals_name.querySelectorAll('.titleDetal');
		var activeTab = block_detals_name.querySelector('.activeTab');
		var pk_active_tab = activeTab.getAttribute('data-content');
		var pk_new_content = tab.getAttribute('data-content');

		if (activeContent.querySelector('#nal').checked) { // Если есть отметка о наличи детали у текущей выбраной
			console.log('on');
			// Проверяем заполненно ли поле цены
			if (activeContent.querySelector('#price').getElementsByTagName('input')[0].value == 0) {
				activeContent.querySelector('#price').getElementsByTagName('input')[0].classList.add('danger');
				console.log('bad');
			} else {
				console.log('good');
				change_tab();
			}
		} else {
			console.log('off');
			change_tab();
		}
	}
}

function checkboxDetal(checkbox) {
	var activeBlockParams = document.querySelector('.contentBlock').querySelector('.active');
	var activeDetal = activeBlockParams.querySelector('#nal').getAttribute('name').split('_')[0];
	var bottomInfo = document.querySelector('.bottomInfo');
	var countSelect = bottomInfo.querySelectorAll('.value')[0].innerHTML;
	var totalPrice = bottomInfo.querySelectorAll('.value')[1].innerHTML;
	console.log(activeDetal);
	if (checkbox.checked == true) {
		bottomInfo.querySelectorAll('.value')[0].innerHTML = parseInt(countSelect) + 1;
		activeBlockParams.querySelector('#price').getElementsByTagName('input')[0].removeAttribute('disabled');
		activeBlockParams.querySelector('#price').getElementsByTagName('input')[0].setAttribute('name', activeDetal+'_price');
		activeBlockParams.querySelector('.textDetals').getElementsByTagName('textarea')[0].removeAttribute('disabled');
		activeBlockParams.querySelector('.textDetals').getElementsByTagName('textarea')[0].setAttribute('name', activeDetal+'_info');
		document.querySelector('.contentDetailGroup').querySelector('.activeTab').getElementsByTagName('img')[0].setAttribute('src', '/static/img/yes.png');
	} else {
		bottomInfo.querySelectorAll('.value')[0].innerHTML = parseInt(countSelect) - 1;
		activeBlockParams.querySelector('#price').getElementsByTagName('input')[0].classList.remove('danger');
		activeBlockParams.querySelector('#price').getElementsByTagName('input')[0].setAttribute('disabled', '');
		activeBlockParams.querySelector('#price').getElementsByTagName('input')[0].removeAttribute('name');
		activeBlockParams.querySelector('#price').getElementsByTagName('input')[0].value = '';
		activeBlockParams.querySelector('.textDetals').getElementsByTagName('textarea')[0].setAttribute('disabled', '');
		activeBlockParams.querySelector('.textDetals').getElementsByTagName('textarea')[0].removeAttribute('name');
		document.querySelector('.contentDetailGroup').querySelector('.activeTab').getElementsByTagName('img')[0].setAttribute('src', '/static/img/no.png');
	}
}

function change_totalPrice(input) {
	console.log(input.value);
}

function donorPanelAnimation() {
	
	setTimeout(function() { 
		document.querySelector('.donorPanel').classList.add('animationPage1');
		setTimeout(function() { 
			document.querySelector('.donorPanel').classList.add('animationPage2');
		}, 500);
	}, 500);
		
}

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

function saveDonor(block) {
	// Проверяем заполненно ли поле цены
	if (block.querySelector('#donorVin').value == 0) {
		block.querySelector('#donorVin').classList.add('danger');
		console.log('bad');
	} else {
		console.log('good');

		document.querySelector('.backBlack').style.display = 'none';

		var csrftoken = getCookie('csrftoken');
		var all_select = block.getElementsByTagName('select');
		var probeg = block.querySelector('#donorProbeg');
		var vin = block.querySelector('#donorVin');
		var idDonor = document.querySelector('#idDonor').value;

		$.ajaxSetup({
			beforeSend: function(xhr, settings) {
				if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
				}
			}
		});

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
				console.log(data)
			}
		});

		for (var i_param = 0; i_param < all_select.length; i_param++) {
			all_select[i_param].setAttribute('disabled', '');
			console.log(all_select[i_param].options[all_select[i_param].selectedIndex].value);
		};
		probeg.setAttribute('disabled', '');
		vin.setAttribute('disabled', '');
		block.querySelector('#save').setAttribute('disabled', '');
		block.querySelector('#edit').removeAttribute('disabled');
	}
}

// Очистка класса danger 
document.querySelector('.vin').querySelector('#donorVin').onfocus = function() {
	document.querySelector('.vin').querySelector('#donorVin').classList.remove('danger');
}

document.querySelector('.contentBlock').querySelector('.active').querySelector('#price').querySelector('.form-control').onfocus = function() {
	var input_price = document.querySelector('.contentBlock').querySelector('.active').querySelector('#price').querySelector('.form-control');
	input_price.classList.remove('danger');
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
