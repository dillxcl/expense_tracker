$(document).ready(function(){
	//$('[data-toggle="tooltip"]').tooltip();
    var actions = $("table td:last-child").html();
	// Append table with add row form on add new button click
    $(".add-new").click(function(){
		$(this).attr("disabled", "disabled");
		var index = $("table tbody tr:last-child").index();
        var row = '<tr>' +
            '<td><input type="text" class="form-control" name="category"></td>' +
            '<td><input type="text" class="form-control" name="daily_spent"></td>' +
            '<td><input type="text" class="form-control" name="date_input"></td>' +
			'<td>' + actions + '</td>' +
        '</tr>';
    	$("table").append(row);		
		$("table tbody tr").eq(index + 1).find(".add, .edit").toggle();
        //$('[data-toggle="tooltip"]').tooltip();
    });
	// Add row on add button click
	$(document).on("click", ".add", function(e){
		
		var empty = false;
		var input = $(this).parents("tr").find('input[type="text"]');
        input.each(function(){
			if(!$(this).val()){
				$(this).addClass("error");
				empty = true;
			} else{
                $(this).removeClass("error");
            }
		});
		$(this).parents("tr").find(".error").first().focus();
		if(!empty){	
			var input = $(this).parents("tr").find('input[type="text"]');
			console.log($("input[name='csrfmiddlewaretoken']").val());
			$.ajax({
				type:'POST',
				url:"/expense_home/daily_expense_create/",
				data:{
					csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
					month_id: $(this).attr("data-id"),
					category: $(this).parents("tr").find('input[name="category"]').val(),
					daily_spent: $(this).parents("tr").find('input[name="daily_spent"]').val(), 
					date_input: $(this).parents("tr").find('input[name="date_input"]').val()				
				},
				dataType: "json",
				success:function(){
					alert("created")
				}
			})
			input.each(function(){
				$(this).parent("td").html($(this).val());
			});	
			$(this).parents("tr").find(".add, .edit").toggle();
			$(".add-new").removeAttr("disabled");
			location.reload();
		}		
    });
	// Edit row on edit button click
	$(document).on("click", ".edit", function(){		
        $(this).parents("tr").find("td:not(:last-child)").each(function(){
			$(this).html('<input type="text" class="form-control" value="' + $(this).text() + '">');
		});		
		$(this).parents("tr").find(".add, .edit").toggle();
		$(".add-new").attr("disabled", "disabled");
    });
	// Delete row on delete button click
	$(document).on("click", ".delete", function(){
        $(this).parents("tr").remove();
		$(".add-new").removeAttr("disabled");
		location.reload();
    });
    
});