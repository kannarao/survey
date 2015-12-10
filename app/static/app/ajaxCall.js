<script type='text/javascript'>
    $(document).ready(function(){
    $('#myForm').on('submit',function(event){
	event.preventDefault();
        //$('#img').show();
        $("#block").show()
        //$('input[type="submit"]').prop('disabled', true);
	$.ajax({
            type: "post",
            url: "/thankss/",
            data: $(this).serialize(),
            success: function(responseData) {
                //$("#img").hide();
                $("#block").hide();
                //$('input[type="submit"]').prop('disabled', false);
                if(responseData.result == "success") {
		        	window.location.href = "/contact";
			}
                else if(responseData == "fail"){
				alert("Please fill every field");
				
			}
            },
        })
})
});
</script>

