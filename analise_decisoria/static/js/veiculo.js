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
$(document).ready(function() {
  habilitar();
  $("#submit-id-editar").click(function(e){
    if ($("#id_carga").val() == "P") {
      $("#id_descricao_carga").val("");
    }else if ($("#id_carga").val() == "C") {
      $("#id_quantidade_pessoas").val(0);
    }
  });
});
