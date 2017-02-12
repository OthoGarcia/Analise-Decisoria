$(document).ready(function() {
  $('#id_parada_ida').select2();
  $('#id_parada_volta').select2();
  $('#id_parada_ida').removeClass("textinput textInput form-control");
  $('#id_parada_ida').addClass("js-example-basic-multiple js-states form-control");
  $('#id_parada_volta').removeClass("textinput textInput form-control");
  $('#id_parada_volta').addClass("js-example-basic-multiple js-states form-control");


  $('select').addClass("textinput textInput form-control");
  $('input').addClass("textinput textInput form-control");
  $('#id_condutor').removeClass("textinput textInput form-control");

});

//inserir calendario ao formulario. Precisa jquery-ui
/*$(function() {
  $( ".calendario" ).datepicker({
    dateFormat: 'dd/mm/yy',
    dayNames: ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado'],
    dayNamesMin: ['D','S','T','Q','Q','S','S','D'],
    dayNamesShort: ['Dom','Seg','Ter','Qua','Qui','Sex','Sáb','Dom'],
    monthNames: ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'],
    monthNamesShort: ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'],
    nextText: 'Próximo',
    prevText: 'Anterior'
  })
});
*/


//Responsavel por gerar o calendario e configurar o mesmo
$('#id_data_saida').removeClass("form-control col-md-3 col-sm-6 calendario textinput textInput")
$('#id_data_saida').addClass("date date-1")
$('#id_data_chegada').removeClass("form-control col-md-3 col-sm-6 calendario textinput textInput")
$('#id_data_chegada').addClass("date date-1")

var dt = new Date();
var mm = dt.getMonth()+1;
dtF = dt.getFullYear() + "/"+ mm + "/" + dt.getDate();

$('.date').datePicker({
  weekDays: ['Dom','Seg', 'Ter', 'Quar', 'Quin', 'Sex', 'Sab'],
  months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
            'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
  timeFormat: 'HH:MM', // can be HH:MM:SS AM, HH:MM AM, HH:MM:SS or HH:MM
   timeFormatAttribute:'data-timeformat', // attribute holding the timeFormat information if different from standard
   doAMPM: false, // switch for standard AM / PM rendering
   minuteSteps: 5, // steps of minutes displayed as options in {{minutes}}
   AMPM: ['AM', 'PM'], // rendered strings in picker options and input fields
   // classes for event listeners (change of selects)
   selectHourClass: 'dp-select-hour', // class name of select for hours
   selectMinuteClass: 'dp-select-minute', // class name of select for minutes
   selectSecondClass: 'dp-select-second', // class name of select for seconds
   selectAMPMClass: 'dp-select-am-pm', // class name of select for AM/PM
   rangeStartAttribute: 'data-from', // attribute holding the name of the other input in a range collective (either rangeEndAttribute or name attribute)
   rangeEndAttribute: 'data-to',
   minDate: dtF,
});



$("#id_origem").change(function(e){
  if ($("#id_origem").val() == 1) {
    $('#id-roteiroForm').show();
  }
});
  // Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("btn_endereco");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
