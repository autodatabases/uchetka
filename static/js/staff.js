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