// No edit, this for POST
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;
}
function csrfSafeMethod(method) { return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method)); }
var csrftoken = getCookie('csrftoken');
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
// end

// Меню
$(function() {
	var Accordion = function(el, multiple) {
		this.el = el || {};
		this.multiple = multiple || false;

		// Variables privadas
		var links = this.el.find('.link');
		// Evento
		links.on('click', {el: this.el, multiple: this.multiple}, this.dropdown)
	}

	Accordion.prototype.dropdown = function(e) {
		var $el = e.data.el;
			$this = $(this),
			$next = $this.next();

		$next.slideToggle();
		$this.parent().toggleClass('open');

		if (!e.data.multiple) {
			$el.find('.submenu').not($next).slideUp().parent().removeClass('open');
		};
	}	

	var accordion = new Accordion($('#accordion'), false);
});
// Скрыть меню
function hideMenu(button){
	document.querySelector('#modal-container').classList.add('out');
	setTimeout(function() {
		button.form.submit();	
	}, 1500);// Заддержка выполения
}

function change_params_donor() {
    $.ajax({
        url: '/lk/detals_list/change_donor_params/',
        type: 'post',
        data: {
            'csrfmiddlewaretoken': csrftoken
        },
        success: function (data) {
            console.log(data)
            var right_panel = document.querySelector('.right-panel');

            for (var i_param = 0; i_param < data.params.length; i_param++) {
                var name = Object.keys(data.params[i_param])[0];
                var select_param = right_panel.querySelector('#'+name);
                select_param.removeAttribute('disabled');
                console.log(data.params[i_param][name]);
                for (var i_option = 0; i_option < data.params[i_param][name].length; i_option++) {
                    select_param.options[i_option] = new Option(data.params[i_param][name][i_option].title, data.params[i_param][name][i_option].value);
                    if (data.params[i_param][name][i_option].value == 'noselect') {
                        select_param.options[i_option].setAttribute('selected', '');
                    };
                }
            }
        }
    });
}

function load_models() {
	var selectMark = document.getElementById("selectMark");
	$.ajax({
		url: '/lk/add_auto/select_auto/',
		type: 'post',
		data: {
			'selectedMark': selectMark.options[selectMark.selectedIndex].value,
			'csrfmiddlewaretoken': csrftoken
		},
		success: function (data) {
			console.log('done');
			var selectModel = document.getElementById("selectModel");
			for (var i = 0; i < data.models.length; i++) {
				selectModel.options[i] = new Option(data.models[i].title, data.models[i].value)
			}
		}
	});
}
function load_generations() {
	var selectModel = document.getElementById("selectModel");
	$.ajax({
		url: '/lk/add_auto/select_auto/',
		type: 'post',
		data: {
			'selectedModel': selectModel.options[selectModel.selectedIndex].value,
			'csrfmiddlewaretoken': csrftoken
		},
		success: function (data) {
			console.log('done');
			var selectGen = document.getElementById("selectGeneration");
			for (var i = 0; i < data.generations.length; i++) {
				selectGen.options[i] = new Option(data.generations[i].title, data.generations[i].value)
			}
		}
	});
}
function donorTabs(newActiveTab) {
	var changeContent = function() {
		 var paramsBlock = document.querySelector('.donorParmas');
		 var photoBlock = document.querySelector('.donorPhoto');
		 if (newActiveTab.getAttribute('data-content') == 'photo') {
		 	photoBlock.classList.add('show');
		 } else	{
		 	photoBlock.classList.remove('show');
		 }
	}
	var oldActiveTab = newActiveTab.parentElement.querySelector('.active');
	oldActiveTab.classList.remove('active');
	newActiveTab.classList.add('active');
	changeContent();
}
function change_modal_content(changeButton) {
	var modalContent = document.querySelector('.modalcontent');
	if (changeButton.getAttribute('id') == 'open_add_stock_panel') {
		modalContent.querySelector('.createStockRoom').classList.add('show');
	} else {
		modalContent.querySelector('.createStockRoom').classList.remove('show');
	}
}
function add_StockRoom(createStockRoom_panel) {
	// Перменные передаваемых параметров
	var titleStockRoom = createStockRoom_panel.querySelector('#titleStockRoom').value;
	var countryStockRoom = createStockRoom_panel.querySelector('#countryStockRoom');
	var regionStockRoom = createStockRoom_panel.querySelector('#regionStockRoom');
	var cityStockRoom = createStockRoom_panel.querySelector('#cityStockRoom');
	var streetStockRoom = createStockRoom_panel.querySelector('#streetStockRoom').value;
	var houseStockRoom = createStockRoom_panel.querySelector('#houseStockRoom').value;
	$.ajax({
		url: '/lk/add_stockroom/',
		type: 'post',
		data: {
			'titleStockRoom': titleStockRoom,
			'streetStockRoom': streetStockRoom,
			'houseStockRoom': houseStockRoom
		},
		success: function (data) {
			console.log('done');
			change_modal_content(createStockRoom_panel.querySelector('#close_add_stock'));
			document.querySelector('.selectAutoDonor').querySelector('#selectMark').removeAttribute('disabled');
			document.querySelector('.selectAutoDonor').querySelector('#selectModel').removeAttribute('disabled');
			document.querySelector('.selectAutoDonor').querySelector('#selectGeneration').removeAttribute('disabled');
			document.querySelector('.selectAutoDonor').querySelector('#nextpageadd').removeAttribute('disabled');
			document.querySelector('.selectAutoDonor').querySelector('.alert').classList.remove('alert-warning');
			document.querySelector('.selectAutoDonor').querySelector('.alert').classList.add('alert-success');
			document.querySelector('.selectAutoDonor').querySelector('.alert').innerHTML = 'Склад успешно создан'
		}
	});
}