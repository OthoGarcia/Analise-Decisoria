$(document).ready(function() {
	var campos_criterio_max = 10;
	var campos_alternativa_max = 10;    //max de 10 campos
	var x = 3; // campos iniciais
	var y = 3;
	$('#add_field_criterio').click (function(e) {
		e.preventDefault();     //prevenir novos clicks
		if (x <= campos_criterio_max) {
			$('#grupo_criterio').append('<div>\
			<label for="criterio" class="control-label">Criterio:</label>\
			<input type="text" required  name="criterio" placeholder="Informe o nome do criterio">\
			<a href="#" class="remover_campo_criterio btn btn-danger">Remover</a>\
			</div>');
			x++;
		}
	});

	// Remover o div anterior
	$('#grupo_criterio').on("click",".remover_campo_criterio",function(e) {
		e.preventDefault();
		$(this).parent('div').remove();
		x--;
	});
	$('#add_field_alternativa').click (function(e) {
		e.preventDefault();     //prevenir novos clicks
		if (y <= campos_alternativa_max) {
			$('#grupo_alternativa').append('<div>\
			<label for="alternativa" class="control-label">Alternativa:</label>\
			<input type="text" required  name="alternativa" placeholder="Informe o nome da alternativa">\
			<a href="#" class="remover_campo_alternativa btn btn-danger">Remover</a>\
			</div>');
			y++;
		}
	});

	// Remover o div anterior
	$('#grupo_alternativa').on("click",".remover_campo_alternativa",function(e) {
		e.preventDefault();
		$(this).parent('div').remove();
		y--;
	});
});
