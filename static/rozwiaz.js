cleanTab();
function cleanTab(){
   var sudoTab = $("input");
   console.log(sudoTab.length);
   for(var i =0;i<sudoTab.length;i++){
   console.log("jestem");
   sudoTab[i].value="";
}
}
function solveSudoku(){
   var sudoTab = $("input");
   console.log(sudoTab.length)
for(var i = 0; i<sudoTab.length;i++){
	questionSudoku=[]
	if(sudoTab[i].value!=""){questionSudoku.push([i,sudoTab[i].value]);}
}
var jsonData = JSON.stringify(questionSudoku);
 $.ajax
    ({
        type: "POST",
        url: "/solve_json",
        dataType: 'json',
        async: false,
        contentType : 'application/json',
        data: jsonData,
		success: function(response) {
        var solution = response;
        console.log(solution)
        for(var i=0; i<solution.length;i++){
        	if(sudoTab[i].value==''){
        		sudoTab[i].value=solution[i].value;
            sudoTab[i]
            $(sudoTab[i]).css("background-color", "gold");
        	}
        }
}
}
)
}