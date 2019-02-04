
// Боковая панель
function move_panel(elem_td) {
    var right_panel = document.querySelector('.right-panel');
    var showed = right_panel.getAttribute('class');
    var pk_content = elem_td.getElementsByTagName('a')[0].getAttribute('id');
    var pk_content_active = right_panel.getAttribute('data-content');

    var detalLine = elem_td.parentElement;
    var detalLine_old = document.querySelector('.selectedDetal');
    
    if (showed == 'right-panel border show') {
        if (detalLine == detalLine_old)  {
            detalLine.classList.remove("selectedDetal");
            right_panel.classList.remove("show");
        } else { 
            detalLine_old.classList.remove("selectedDetal");
            right_panel.classList.remove("show");
            right_panel.setAttribute('data-content', pk_content);
            setTimeout(function(){change_content(pk_content)}, 700);
            
            setTimeout(function(){right_panel.classList.add("show")}, 700);
            detalLine.classList.add("selectedDetal");
        } 
    } else {
        right_panel.classList.add("show");
        right_panel.setAttribute('data-content', pk_content);
        setTimeout(function(){change_content(pk_content)}, 100);
        detalLine.classList.add("selectedDetal");
    }

    function change_content(new_pk_donor){
        document.querySelector('#idDonor').value = new_pk_donor;

        $.ajax({
            url: '/lk/detals_list/load_donor/',
            type: 'post',
            data: {
                'new_pk_donor': new_pk_donor,
                'csrfmiddlewaretoken': csrftoken
            },
            success: function (data) {
                var right_panel = document.getElementById('RightPanel');
                console.log(data);

                right_panel.querySelector('#donorMarkOption').innerHTML = data.mark;
                right_panel.querySelector('#donorModelOption').innerHTML = data.model;
                right_panel.querySelector('#donorGenOption').innerHTML = data.generation;
                right_panel.querySelector('#donorKuzovOption').innerHTML = data.kuzov;
                right_panel.querySelector('#donorYearOption').innerHTML = data.year;
                right_panel.querySelector('#donorProbeg').value = data.probeg;
                right_panel.querySelector('#donorVin').value = data.vin_number;
                right_panel.querySelector('#donorEngineType').innerHTML = data.engine_type;
                right_panel.querySelector('#donorEngineSize').innerHTML = data.engine_size;
                right_panel.querySelector('#donorTransmision').innerHTML = data.transmission;
                right_panel.querySelector('#donorColor').innerHTML = data.color;
                right_panel.querySelector('#donorHelm').innerHTML = data.helm;
                right_panel.querySelector('#donorPrivod').innerHTML = data.privod;
            }
        });

    }
}
// Закрыть боковую панель
function close_panel() {
    var right_panel = document.querySelector('.right-panel');
    right_panel.classList.remove("show");
    document.getElementsByTagName('tbody')[0].querySelector('.selectedDetal').classList.remove("selectedDetal");
}
// Выделение одной детали
function selected(checkbox) {
    var all_checkbox = document.getElementsByTagName('tbody');
    var controlPanel = document.querySelector('.controlPanel')
    var selectedCount = controlPanel.getElementsByTagName('span')[0].innerHTML;
    var selectedPrice = controlPanel.getElementsByTagName('span')[1].innerHTML;
    var detalPrice = checkbox.parentElement.parentElement.getElementsByTagName('span')[0].innerHTML;
    if (checkbox.checked) {
        controlPanel.getElementsByTagName('span')[0].innerHTML = parseInt(selectedCount)+1;
        controlPanel.getElementsByTagName('span')[1].innerHTML = parseInt(selectedPrice)+parseInt(detalPrice);
    } else {
        controlPanel.getElementsByTagName('span')[0].innerHTML = parseInt(selectedCount)-1;
        controlPanel.getElementsByTagName('span')[1].innerHTML = parseInt(selectedPrice)-parseInt(detalPrice);
    }
    if (controlPanel.getElementsByTagName('span')[0].innerHTML < 1) {
        controlPanel.classList.remove('showPanel');
    } else {
        controlPanel.classList.add('showPanel');
    }
}
// Выделение всех деталей
function select_all(){
    var all_checkbox = document.querySelectorAll("#checkbox");
    var controlPanel = document.querySelector('.controlPanel')
    var selectedPrice = controlPanel.getElementsByTagName('span')[1].innerHTML;
    var i = 0;
    if (document.getElementById("select_all").checked){
        while(i < all_checkbox.length){
            all_checkbox[i].checked = true;
            selected(all_checkbox[i]);
            i++;
        }
        controlPanel.getElementsByTagName('span')[0].innerHTML = parseInt(i);
    }
    else{
        while(i < all_checkbox.length){
            all_checkbox[i].checked = false;
            selected(all_checkbox[i]);
            i++;
        }
        controlPanel.getElementsByTagName('span')[1].innerHTML = 0;
    }
}
// Кнопка изменить на боковой панели
function editDonor(block) {
    var all_select = block.getElementsByTagName('select');
    for (var i_param = 0; i_param < all_select.length; i_param++) {
        all_select[i_param].removeAttribute('disabled');
    };
    block.querySelector('#donorProbeg').removeAttribute('disabled');
    block.querySelector('#donorVin').removeAttribute('disabled');
    block.querySelector('#save').removeAttribute('disabled');
    block.querySelector('#edit').setAttribute('disabled', '');
}
// Кнопка сохранить на боковой панели
function saveDonor(block) {
    var all_select = block.getElementsByTagName('select');
    var probeg = block.querySelector('#donorProbeg');
    var vin = block.querySelector('#donorVin');
    var idDonor = block.parentElement.querySelector('#idDonor').value;

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
// Изменение цены двойным кликом
function edit_price(td) {
    var old_value = td.getElementsByTagName('span')[0].innerHTML;
    td.innerHTML = '<input type="text" id="Edit" class="edit" onchange="save_price(this)" onblur="save_price(this)" value="'+old_value+'">';
    td.getElementsByTagName('input')[0].select();
}
// Сохранение изменений цены
function save_price(input) {
    var tr_vin = input.parentElement;
    console.log(tr_vin);
    tr_vin.innerHTML = '<span>'+input.value+'</span> ₽';
}
// Показать фото детали
function view_detal_photo(img_mini) {
    var full_img = img_mini.parentElement.parentElement.querySelector('.fulImg');
    full_img.classList.add('show');
}
// Скрыть фото
function closePhoto(fulImg) { fulImg.classList.remove('show');}

// Быстрые фильтры
// function small_filter(select) {

//     $.ajax({
//         url: '/lk/detals_list/small_filter/',
//         type: 'post',
//         data: {
//             'csrfmiddlewaretoken': csrftoken,
//             'filterType': select.getAttribute('name'),
//             'filterValue': select.options[select.selectedIndex].value, 
//         },
//         success: function (data) {
//             var new_tbody = document.createElement('tbody');
            
//             document.querySelector('.tableDetals').getElementsByTagName('tbody')[0].remove();
//             document.getElementsByTagName('table')[0].appendChild(new_tbody);
//             for (var i = 0; i < data.result_detal.length; i++) {
//                 var new_tr = document.createElement('tr');
//                 var new_td = [document.createElement('td'), document.createElement('td'), document.createElement('td'), document.createElement('td'), document.createElement('td'), document.createElement('td'), document.createElement('td'), document.createElement('td'), document.createElement('td')];
//                 // Новая строка
//                 document.getElementsByTagName('tbody')[0].appendChild(new_tr).setAttribute('data-content', data.result_detal[i].donor_info.id_donor);
//                 // Чекбокс
//                 document.getElementsByTagName('tr')[i+1].appendChild(new_td[0]).classList.add('detalCheckBox');
//                 new_td[0].innerHTML = '<input id="checkbox" type="checkbox" onchange="selected(this)">';
//                 // Порядковый номер
//                 document.getElementsByTagName('tr')[i+1].appendChild(new_td[1]).classList.add('detalNumber');
//                 new_td[1].innerHTML = i+1;
//                 // Название детали
//                 document.getElementsByTagName('tr')[i+1].appendChild(new_td[2]).classList.add('detalTitle');
//                 new_td[2].innerHTML = data.result_detal[i].detal.title;
//                 // Донор 
//                 document.getElementsByTagName('tr')[i+1].appendChild(new_td[3]).setAttribute('onclick', 'move_panel(this)');
//                 new_td[3].classList.add('detalDonor');
//                 new_td[3].innerHTML = '<a href="#" id="'+data.result_detal[i].donor_info.id_donor+'">'+data.result_detal[i].donor_info.mark+' '+data.result_detal[i].donor_info.model+' '+data.result_detal[i].donor_info.generation+'</a>'
//                 // Цена
//                 document.getElementsByTagName('tr')[i+1].appendChild(new_td[4]).classList.add('detalPrice');
//                 new_td[4].setAttribute('ondblclick', 'edit_price(this)')
//                 new_td[4].innerHTML = '<span>'+data.result_detal[i].price+'</span> ₽'
//                 // VIN    
//                 document.getElementsByTagName('tr')[i+1].appendChild(new_td[5]).classList.add('detalVIN');
//                 new_td[5].innerHTML = '06V288B2'
//                 // Склад    
//                 document.getElementsByTagName('tr')[i+1].appendChild(new_td[6]).classList.add('detalSklad');
//                 new_td[6].innerHTML = data.result_detal[i].stockroom.title;
//                 // Фото
//                 document.getElementsByTagName('tr')[i+1].appendChild(new_td[7]).classList.add('detalPhotoImg');
//                 new_td[7].innerHTML = '<a href="#img1"><img src="/static/img/image_mini.png" alt="" onclick="view_detal_photo(this)"></a><a href="#close" class="fulImg" id="img1" onclick="closePhoto(this)"><img src="'+data.result_detal[i].photo+'" alt="товар"></a>';
//                 // Описание
//                 document.getElementsByTagName('tr')[i+1].appendChild(new_td[8]).classList.add('detalOther');
//                 new_td[8].innerHTML = data.result_detal[0].description;
//             }   
//         }
//     });
// }
// Развернуть фильтры
function show_filter(block) {
    var status = document.querySelector('.showfilter');
    var buttonFilter = document.querySelector('.showFilterButton');
    var filter_panel = document.querySelector('.filterBack');

    if (status == null) {
        buttonFilter.classList.add('showfilter');
        filter_panel.classList.add('showfilter');
        block.getElementsByTagName('label')[0].innerHTML = 'Свернуть';
        block.getElementsByTagName('i')[0].setAttribute('class', 'fas fa-angle-double-up fa-lg');
    } else {
        buttonFilter.classList.remove('showfilter');
        filter_panel.classList.remove('showfilter');
        block.getElementsByTagName('label')[0].innerHTML = 'Фильтры';
        block.getElementsByTagName('i')[0].setAttribute('class', 'fas fa-angle-double-down fa-lg');
    }
}
// Добавление имени при выделении
function add_name(input){
    if (input.checked){
        input.setAttribute('name', input.getAttribute('id').split('_')[1])
    } else {
        input.removeAttribute('name')
    }
}
// Отправка формы при изменении малого фильтра
function submit_small_filter(select) {
    var all_select = select.parentElement.parentElement.getElementsByTagName('select')
    for (var i = 0; i < all_select.length; i++) {
        if (all_select[i].options[all_select[i].selectedIndex].value != 'all') {
            all_select[i].setAttribute('name', all_select[i].getAttribute('id'))
        }
    }
    select.parentElement.parentElement.submit();
}