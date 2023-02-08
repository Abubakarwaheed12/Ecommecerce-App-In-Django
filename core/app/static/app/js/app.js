
//  JS for increase and decrease Quantity 

$('.plus-cart').click(function () {
    var id = $(this).attr('pid').toString();
    var eml = this.parentNode.children['2']
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
    console.log(id)
    $.ajax({
        type: 'GET',
        url: '/minus/',
        data: {
            prod_id: id,
        },
        success: function (data) {
            console.log(data)
            eml.innerText = data.quantity
        }
    })
})

// Remove Item 

$('.remove').click(function () {
    var id = $(this).attr('pid').toString();
    console.log(id)
})