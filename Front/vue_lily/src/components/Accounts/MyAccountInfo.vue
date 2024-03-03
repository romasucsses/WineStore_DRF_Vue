<script setup>
// const AccsessToken = localStorage.getItem('AccsessToken');

// async function fetchDataWithAccessToken(accessToken) {
//     try {
//         const response = await axios.get('http:/http://127.0.0.1:8000/api/v1/users/my-account-details/', {
//             headers: {
//                 Authorization: `Bearer ${accessToken}`
//             }
//         });
//         // Assuming response.data contains the fetched data
//         console.log( response.data);

//     } catch (error) {
//         // Handle error
//         console.error('Request failed:', error);
//         throw error;
//     }
// }
// fetchDataWithAccessToken(AccsessToken);

</script>

<template>
    
    <div>
        
        <p>Editing Your Account Information</p>
        <form method="post">
            <div class="fields">
                <div class="data">
                    <label>username</label>
                    <input id="username" name="username" value="{{ user.username }}">
                    <label>email</label>
                    <input id="email"  name="email" value="{{ user.email }}">
                </div>
                <div class="data">
                    <label>first name</label>
                    <input id="name" name="name" value="{{ user.name }}">
                    <label>last name</label>
                    <input id="last_name" name="last_name" value="{{ user.last_name }}">
                </div>
            </div>
            <div class="btns">
                <button type="submit" name="action" value="save-changes">Save Changes</button>
                <button>Reset Password</button>
            </div>
        </form>
    </div>
</template>

<style scoped>
    .right-info .fields{
        display: flex;
        justify-content: space-between;

    }

    .right-info .data{
        margin: 15px;
    }

    .right-info form {
        display: flex;
        flex-direction: column;
        max-width: 400px;
        margin: 0 auto;
    }

    .right-info label{
        color: gray;
    }

    .right-info input {
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 16px;
        width: 250px;
    }

    .right-info button {
        padding: 10px 20px;
        margin: 5px;
        border: none;
        border-radius: 5px;
        background-color: #007bff;
        color: #fff;
        font-size: 14px;


    }

    .right-info button:hover {
        background-color: #0056b3;
    }

    .right-info .btns {
        width: 80%;
        display: flex;
        justify-content: space-between;
        margin-left: 140px;
    }

    .right-info .btns button {
        margin-bottom: 10px;
    }
</style>
