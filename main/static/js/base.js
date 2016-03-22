$(document).ready(function(){
	var lakeInfoList = []
	$('.lake').click(function(){
	lakeInfoList.push($('#box').html())
	for(var x = 0; x < lakeInfoList.length; x++){
		$('#lake-list').append(lakeInfoList[x]);

	}
	console.log($('#box').html())
	});
});