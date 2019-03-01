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



function add_user(button) {
	var form = button.parentElement.parentElement;
	console.log(form.querySelector('#id_staff_login').value);
	form.parentElement.setAttribute('style', 'display:none');
	loader('on');
	$.ajax({
        url: '/lk/staff/',
        type: 'post',
        data: {
            'csrfmiddlewaretoken': csrftoken,
            'type': 'add_user',
            'staff_login': form.querySelector('#id_staff_login').value,
            'staff_fio': form.querySelector('#id_staff_fio').value,
            'staff_email': form.querySelector('#id_staff_email').value,
            'staff_password': form.querySelector('#id_staff_password').value,
            'staff_group': form.querySelector('#id_staff_group').options[form.querySelector('#id_staff_group').selectedIndex].value,
            'staff_stock': form.querySelector('#id_staff_stock').options[form.querySelector('#id_staff_stock').selectedIndex].value,
        },
        success: function (data) {
        	document.querySelector('.alert-window').classList.add('good');
        	document.querySelector('.alert-message').innerHTML = 'Сотдрудник успешно добавлен!';
        	loader('off');
			setTimeout (
				function() {
        			document.querySelector('.alert-window').classList.add('show');
				}, 400
			);
            auto_close_alert();
        }
    });
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
            		document.querySelector('.alert-window').classList.add('error');
            		document.querySelector('.alert-message').innerHTML = 'Невозможно удалить себя!';
            	} else {
                	select.remove(select.selectedIndex);
                	document.querySelector('.alert-window').classList.add('good');
                	document.querySelector('.alert-message').innerHTML = 'Сотдрудник успешно удален!';
            	}
            	loader('off');
				setTimeout (
					function() {
            			document.querySelector('.alert-window').classList.add('show');
					}, 400
				);
                auto_close_alert();
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
    			loader('off');
            }
        });
	}
}




