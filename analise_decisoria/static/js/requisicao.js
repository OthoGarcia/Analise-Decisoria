//inserir css nos componentes
$(document).ready(function() {
  $('#id_parada_ida').select2();
  $('#id_parada_volta').select2();
  $('#id_parada_ida').removeClass("textinput textInput form-control");
  $('#id_parada_ida').addClass("js-example-basic-multiple js-states form-control");
  $('#id_parada_volta').removeClass("textinput textInput form-control");
  $('#id_parada_volta').addClass("js-example-basic-multiple js-states form-control");


  //habilitando os campos de acordo com o seleçãodo select carga
  habilitar();
  $("#submit-id-editar").click(function(e){
    if ($("#id_carga").val() == "P") {
      $("#id_descricao_carga").val("");
    }else if ($("#id_carga").val() == "C") {
      $("#id_quantidade_pessoas").val(0);
    }
  });


  $('select').addClass("textinput textInput form-control");
  $('input').addClass("textinput textInput form-control");
  $('#id_condutor').removeClass("textinput textInput form-control");


  //verifica se o valor passado da view é 1 sendo que se retornar 1 o formulario
  //foi enviado novamente com as menssagens de error
  var value = $('#endereco').val();
  if (value == 1){
    $('#btn-origem').trigger("click");
  }

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

$("#id_error_quantidade_pessoas").hide();
$("#id_error_descricao_carga").hide();
function verificar_carga(){
  if ($('#id_carga').val() == "P"){
    if ($("#id_quantidade_pessoas").val() == ""){
      $("#id_error_quantidade_pessoas").show();
      return false;
    }else{
      $("#id_error_quantidade_pessoas").hide();
      return true;
    }
  }
  else if ($('#id_carga').val() == "C"){
    if ($("#id_descricao_carga").val() == ""){
      $("#id_error_descricao_carga").show();
      return false;
    }else{
      $("#id_error_descricao_carga").hide();
      return true;
    }
  }
  else if ($('#id_carga').val() == "X"){
    if ($("#id_descricao_carga").val() == "" && $("#id_quantidade_pessoas").val() == ""){
      $("#id_error_descricao_carga").show();
      $("#id_error_quantidade_pessoas").show();
      return false;
    }else {
      if ($("#id_descricao_carga").val() == "" && $("#id_quantidade_pessoas").val() != "" ){
        $("#id_error_descricao_carga").show();
        $("#id_error_quantidade_pessoas").hide();
          return false;
      }else if ($("#id_descricao_carga").val() != "" && $("#id_quantidade_pessoas").val() == "" ){
          $("#id_error_quantidade_pessoas").show();
          $("#id_error_descricao_carga").hide();
          return false;
      }else{
        $("#id_error_descricao_carga").hide();
        $("#id_error_quantidade_pessoas").hide();
        return true;
      }
    }
  }
}

//Escolha das cargas
$("#div_id_descricao_carga").hide();
$("#div_id_quantidade_pessoas").hide();
function habilitar() {
  if ($("#id_carga").val() == "P") {
    $("#div_id_quantidade_pessoas").show();
    $("#div_id_descricao_carga").hide();
    $('#submit-id-cadastrar').prop('disabled', false);
  }else if ($("#id_carga").val() == "C") {
    $("#div_id_quantidade_pessoas").hide();
    $("#id_quantidade_pessoas").val(0);
    $("#div_id_descricao_carga").show();
    $('#submit-id-cadastrar').prop('disabled', false);
  }else if ($("#id_carga").val() == "X") {
    $("#div_id_quantidade_pessoas").show();
    $("#div_id_descricao_carga").show();
    $('#submit-id-cadastrar').prop('disabled', false);
  }else {
    $("#div_id_quantidade_pessoas").hide();
    $("#div_id_descricao_carga").hide();
    $('#submit-id-cadastrar').prop('disabled', true);
  }
}
$("#id_carga").change(function(){
  habilitar();
 });
