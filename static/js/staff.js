function new_staff_user(button) {
	if (button.getAttribute('id') == 'open') {
		document.querySelector('.add-staff-user').classList.remove('animation-2')
		setTimeout(
			function(){
				document.querySelector('.add-staff-user').classList.remove('animation-1');
				document.querySelector('.backLoad').setAttribute('style', 'display:none');
			}, 500
		);
	} else {
		document.querySelector('.backLoad').removeAttribute('style');
		document.querySelector('.add-staff-user').classList.add('animation-1');
		setTimeout(
			function(){
				document.querySelector('.add-staff-user').classList.add('animation-2')}, 500
		);
	}
}

function delete_user(button) {
	loader('on');
	var select = document.querySelector('#all_staff');
	var user = select.options[select.selectedIndex].value;
	$.ajax({
            url: '/lk/staff/',
            type: 'post',
            data: {
                'csrfmiddlewaretoken': csrftoken,
                'user': user,
                'type': 'delete_user'
            },
            success: function (data) {
            	if (data.user_id == 'Not delete login user') {
            		document.querySelector('.alert-message').innerHTML = 'Нельзя удалить директора!';
            	} else {
                	select.remove(select.selectedIndex);
                	document.querySelector('.alert-message').innerHTML = 'Сотдрудник успешно удален!';
            	}
            	loader('off');
				setTimeout (
					function() {
            			document.querySelector('.alert-window').classList.add('show');
					}, 400
				);
            }
        });
}

function load_user_info(select) {
	var table_user_info = document.querySelector('.user-info').querySelector('table');
	var all_td = table_user_info.querySelector('tbody').querySelectorAll('.param-value');
	var user = select.options[select.selectedIndex].value;
	if (user == 'none') {
		for (var i = 0; i < all_td.length; i++) {
			if (i == 0 ) {
    			all_td[i].innerHTML = 'Сотдрудник не выбран';
			} else {
				all_td[i].innerHTML = '...';
			}
    	}
	} else {
		loader('on');
		$.ajax({
            url: '/lk/staff/',
            type: 'post',
            data: {
                'csrfmiddlewaretoken': csrftoken,
                'user': user,
                'type': 'load_info'
            },
            success: function (data) {
            	for (var i = 0; i < all_td.length; i++) {
            		all_td[i].innerHTML = data[i].param;
            	}
            	setTimeout (
					function() {
            			loader('off');
					}, 300
				);
            	
            }
        });
	}
}




