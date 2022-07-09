var i =0;
var a = 0;
sudoTab = $("input");
selectE = document.getElementById("category");
selectE.value ="1";
for(var i =0;i<sudoTab.length;i++){
	sudoTab[i].value="";
}
if(a==0){
a++;
$.ajax({
	type:"GET",
	url:"/game",
	dataType:"json",
	success:function(data){
		for(i = 0;i<data.length;i++){
			if(data[i].value!=0){
				$(sudoTab[i]).attr('disabled', true);
				$(sudoTab[i]).val(data[i].value);
			}
		}
	}
}
)
}


function checkSudoku(){
	var all = $("input");
	var startingSudoku = [];
	var solution = [];
	for(var i = 0; i<all.length;i++){
		if(all[i].disabled){
		startingSudoku.push([i, all[i].value]);
	}

		else if(all[i].value!=""){
		solution.push([i, all[i].value]);

	}
}	var earlierSolve = solution;
	var data = [startingSudoku, solution];
	var jsonData = JSON.stringify(data);
	 $.ajax
    ({
        type: "POST",
        url: "/check",
        dataType: 'json',
        async: false,
        contentType : 'application/json',
        data: jsonData,
		success: function(response) {
        wrong = response;
        var difference = $(earlierSolve).not(wrong).get();
        for(var i=0; i<difference.length;i++){
        	sudoTab[difference[i][0]].style.backgroundColor = "green";
        }
       	for(var i=0;i<wrong.length;i++){
       		sudoTab[wrong[i]].style.backgroundColor = "red";
       	}
    }    });
}
function get_new_sudoku(){
	for(var i =0;i<sudoTab.length;i++){
	$(sudoTab[i]).css("background-color", "");
	$(sudoTab[i]).attr('disabled', false);
	sudoTab[i].value="";
}
	var sel = document.getElementById("category");
	var value = sel.options[sel.selectedIndex].value;
$.ajax({
	type: "POST",
	url:"/game",
	dataType:"json",
	contentType : 'application/json',

	data: value,
	success:function(response){
		newSudoku = response;
		for(i = 0;i<newSudoku.length;i++){
			if(newSudoku[i].value!=0){
				$(sudoTab[i]).attr('disabled', true);
				$(sudoTab[i]).val(newSudoku[i].value);

			}
		}
	}
}
)
}