
//  JS for increase and decrease Quantity 

$('.plus-cart').click(function(){
    var id=$(this).attr('pid').toString();
    console.log(id)
    $.ajax({
        type:'GET',
        url:'/minus/',
        data:{
            prod_id:id,
        },
        success:function(data){
            console.log(data)
        }
    })
})

// Minus Cart
$('.minus-cart').click(function(){
    var id=$(this).attr('pid').toString();
    console.log(id)
    $.ajax({
        type:'GET',
        url:'/minus/',
        data:{
            prod_id:id,
        },
        success:function(data){

        }
    })
})

// Remove Item 

$('.remove').click(function(){
    var id=$(this).attr('pid').toString();
    console.log(id)
})