$(document).ready(function() {
	        var campos_max = 10;
	        var campos_max2 = 10;    //max de 10 campos
	        var x = 3; // campos iniciais
	        var y = 3;
	        $('#add_field').click (function(e) {
	                e.preventDefault();     //prevenir novos clicks
	                if (x <= campos_max) {
	                        $('#grupo').append('<div>\
	                        	<label for="criterio" class="control-label">Criterio:</label>\
	                                 <input type="text" required  name="criterio[]" placeholder="Informe o nome do criterio">\
	                                <a href="#" class="remover_campo btn btn-danger">Remover</a>\
	                                </div>');
	                        x++;
	                }
	        });

	        // Remover o div anterior
	        $('#grupo').on("click",".remover_campo",function(e) {
	                e.preventDefault();
	                $(this).parent('div').remove();
	                x--;
	        });
	        $('#add_field2').click (function(e) {
	                e.preventDefault();     //prevenir novos clicks
	                if (y < 11) {
	                        $('#grupo2').append('<div>\
	                        	<label for="alternativa" class="control-label">Alternativa:</label>\
	                                 <input type="text" required  name="alternativa[]" placeholder="Informe o nome da alternativa">\
	                                <a href="#" class="remover_campo2 btn btn-danger">Remover</a>\
	                                </div>');
	                        x++;
	                }
	        });

	        // Remover o div anterior
	        $('#grupo2').on("click",".remover_campo2",function(e) {
	                e.preventDefault();
	                $(this).parent('div').remove();
	                x--;
	        });
	});