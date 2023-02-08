
//  JS for increase and decrease Quantity 

$('.plus-cart').click(function () {
    var id = $(this).attr('pid').toString();
    var eml = this.parentNode.children['2']
    var amount=document.getElementById('am')
    var total_amount=document.getElementById('tm')
    var item_t_price=document.getElementById('itemPrice')
    console.log(id)
    $.ajax({
        type: 'GET',
        url: '/plus/',
        data: {
            prod_id: id,
        },
        success: function (data) {
            console.log(data)
            eml.innerText = data.quantity
            amount.innerText=data.amount
            total_amount.innerText=data.total_amount
            item_t_price.innerText=data.item_total_price
            if (data.status == 200) {
                
                console.log('your Status Is Okay ')
            }
        }
    })
})

// Minus Cart
$('.minus-cart').click(function () {
    var id = $(this).attr('pid').toString();
    var eml = this.parentNode.children['2']
    var amount=document.getElementById('am')
    var total_amount=document.getElementById('tm')
    var item_t_price=document.getElementById('itemPrice')
    console.log(id)
    $.ajax({
        type: 'GET',
        url: '/minus/',
        data: {
            prod_id: id,
        },
        success: function (data) {
            console.log(data)
            eml.innerText = data.quantity;
            amount.innerText=data.amount;
            total_amount.innerText=data.total_amount;
            item_t_price.innerText=data.item_total_price;
        }
    })
})

// Remove Item 

$('.remove').click(function () {
    var id = $(this).attr('pid').toString();

    console.log(id)
    $.ajax({
        type:'GET',
        url:'/remove/',
        data:{
            'prod_id':id,
        },
        success:function(data){
            console.log(data)
        }
    })
})