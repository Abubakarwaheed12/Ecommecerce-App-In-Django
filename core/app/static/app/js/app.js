
//  JS for increase and decrease Quantity 

$('.plus-cart').click(function () {
    var id = $(this).attr('pid').toString();
    var eml = this.parentNode.children['2']
    var amount=document.getElementById('am')
    var total_amount=document.getElementById('tm')
    var itemprice=document.getElementById('itemPrice')
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
            itemprice.innerText=data.item_total_price
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
    var itemprice=document.getElementById('itemPrice')
    var cid=document.getElementById('cid')
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
            itemprice.innerText=data.item_total_price;
           if (data.ok==200){
            cid.parentNode.parentNode.parentNode.parentNode.remove()
           }
        }
    })
})

// Remove Item 

$('.remove').click(function () {
    var id = $(this).attr('pid').toString();
    var amount=document.getElementById('am')
    var total_amount=document.getElementById('tm')
    var cid=document.getElementById('cid')
    console.log(id)
    $.ajax({
        type:'GET',
        url:'/remove/',
        data:{
            'prod_id':id,
        },
        success:function(data){
            console.log(data)
            total_amount.innerText=data.total_amount;
            amount.innerText=data.amount;
            cid.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})