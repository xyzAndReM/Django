


function responder(str) {

var answer = $("input#answer").val()

if(answer === str){
$("#respond").removeClass("btn btn-danger");
$("#respond").addClass("btn btn-success");
$("#respond").text("Correto!");
var audio = new Audio('/static/polls/media/sounds/correct.mp3');
audio.play();
}
else{
$("#respond").removeClass("btn btn-success");	
$("#respond").addClass("btn btn-danger");
$("#respond").text("Incorreto :(");
}



}