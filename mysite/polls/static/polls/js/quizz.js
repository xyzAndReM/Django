


function responder(str) {

var answer = $("input#answer").val()

if(answer === str){
$("#respond").removeClass("btn btn-danger");
$("#respond").addClass("btn btn-success");
}
else{
$("#respond").removeClass("btn btn-success");	
$("#respond").addClass("btn btn-danger");
}



}