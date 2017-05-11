var drop = $(".drop");
var gift_item = $('.gift_item');
var dropped = false

function correct(){
    alert("hello")
}

for(var i = 0; i < gift_item.length; i++){
    gift_item[i].id = i
}


drop.click(function(){
    number = $(this).closest("div").prop("id"); //$(this) is what you clicked!
    if(!dropped){
        $(".gift_details")[number].style.display = "block"
        dropped = true
        $(this).addClass('fa-chevron-circle-up')
        $(this).removeClass('fa-chevron-circle-down')
        
        
    }else{
        $(".gift_details")[number].style.display = "none"
        dropped = false
        $(this).removeClass('fa-chevron-circle-up')
        $(this).addClass('fa-chevron-circle-down')
    }
    
   
});



