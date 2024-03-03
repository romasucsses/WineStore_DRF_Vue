<script setup>

</script>

<template>
    <div>
        <h3>Order Nr. # order.pk  Information</h3>
        <table class="data-table">

            <thead>
                <tr>
                    <th>Product</th>
                    <th>Total</th>
                </tr>
            </thead>

            <tbody>
            
                <tr>
                    <td><a href="#"> each.product </a></td>
                    <td><span>$ each.product.price  x  each.quantity </span></td>
                </tr>
            

            </tbody>

            <tfoot>

                <tr>
                    <th scope="row">Payment method:</th>
                    <td> order.payment_method </td>
                </tr>

                <tr>
                    <th scope="row">Date:</th>
                    <td><span> order.date </span></td>
                </tr>

                <tr>
                    <th scope="row">Total:</th>
                    <td><span>$ item_total </span></td>
                </tr>

            </tfoot>

        </table>

    </div>
</template>

<style scoped>
    .right-info{
        width: 600px;
        margin: 20px;
        
        
    }



    table {
        margin-left: 10px;
        font-family: Arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
        background-color: #FFFFFF;
    }

    th, td {
        border: 1px solid #483e3e;
        text-align: left;
        padding: 10px;

    }

    th {
        background-color: #007bff;
        color: white;
    }
</style>