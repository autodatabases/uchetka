window.onscroll = function() {
    // var tr = document.querySelector('.tableDetals ').querySelector('tbody').querySelectorAll('tr');
    // var first_tr_top = tr[0].getBoundingClientRect().top;
    // var last_tr_pos_bottom = tr[tr.length-1].getBoundingClientRect().bottom;
    // var pag_panel = document.querySelector('.pag-panel');
    // var active_page = parseInt(pag_panel.querySelector('.active').querySelector('a').innerHTML);
    // var html = document.querySelector('html')
    // console.log(last_tr_pos_bottom, html_height);
    
    // if (html_height == last_tr_pos_bottom-1) {
    //     console.log(active_page);
    //     $.ajax({
    //         url: '/lk/detals_list/',
    //         type: 'get',
    //         data: {
    //             'page': active_page+1
    //         },
    //         success: function (data) {
    //             console.log()
    //             var active_page_button = pag_panel.querySelector('.active');
    //             active_page_button.classList.remove('active');
    //             active_page_button.nextSibling.nextElementSibling.classList.add('active');
    //         }
    //     });
    // } else {
    //     console.log();
    // }
}


$(document.querySelector('.smallFilter').querySelectorAll('select')).change(function(){
    console.log(this.value);
});


// Боковая панель
function move_panel(elem_td) {
    var donor_panel = document.querySelector('.donor');
    var showed = donor_panel.getAttribute('class');
    var id_donor_new = elem_td.getElementsByTagName('a')[0].getAttribute('id')
    var detalLine = elem_td.parentElement;
    var detalLine_old = document.querySelector('.selectedDetal');
    if (showed == 'donor in-detal-list show') {
        if (id_donor_new == document.getElementById('idDonor').value)  {
            if (detalLine == detalLine_old) {
                donor_panel.classList.remove("show");
                detalLine.classList.remove("selectedDetal");
            } else {
                detalLine_old.classList.remove("selectedDetal");
                detalLine.classList.add("selectedDetal");
            }
        } else { 
            detalLine_old.classList.remove("selectedDetal");
            donor_panel.classList.remove("show");
            setTimeout(function(){change_content(id_donor_new)}, 100);
            setTimeout(function(){donor_panel.classList.add("show")}, 700);
            detalLine.classList.add("selectedDetal");
        } 
    } else {
        donor_panel.classList.add('show');
        setTimeout(function(){change_content(id_donor_new)}, 100);
        detalLine.classList.add("selectedDetal");
    }

    function change_content(id_donor_new){
        document.querySelector('#idDonor').value = id_donor_new;
        $.ajax({
            url: '/lk/detals_list/load_donor/',
            type: 'post',
            data: {
                'new_pk_donor': id_donor_new,
                'csrfmiddlewaretoken': csrftoken
            },
            success: function (data) {
                var donor_panel = document.querySelector('.donor');
                donor_panel.querySelector('#donorVin').value = data.vin_number;
                document.getElementById('all_marks').value = data.mark;
                document.getElementById('all_models').value = data.model;
                document.getElementById('all_generations').value = data.generation;
                document.getElementById('all_years').value = data.year;
                document.getElementById('all_kuzovs').value = data.kuzov;
                donor_panel.querySelector('#donorProbeg').value = data.probeg;
                document.getElementById('all_engine_type').value = data.engine_type;
                document.getElementById('all_engine_size').value = data.engine_size;
                document.getElementById('all_kpp').value = data.transmission;
                document.getElementById('all_color').value = data.color;
                document.getElementById('all_helm').value = data.helm;
                document.getElementById('all_privod').value = data.privod;
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