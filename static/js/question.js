$('.answer').click(function() {
   	$(".answer:has(input:checked)").css("background", "#95d6a2");
	$(".answer:has(input:checked)").siblings().css("background", "#d3d3d35e");
	if ($(".answer:has(input:checked)")) {
		$(".answer:has(input:checked)").children(".tick").css("display", "inline-block");
		$(".answer:has(input:checked)").siblings().children(".tick").css("display", "none");
		$(".answer:has(input:checked)").children("label").css("color", "#0f4e21");
		$(".answer:has(input:checked)").siblings().children("label").css("color", "black");
		$("input:checked").css("display", "none");
		$(".answer:has(input:checked)").siblings().children("input").css("display", "inline-block");
	}
});
