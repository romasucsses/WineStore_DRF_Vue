<script setup>

</script>


<template>
    <div>
       

        <div class="login-form">
            <h1>Sing Up</h1>
            <form method="post">
    
                <div class="group">
                    <label>Username</label>
                    <input type="text" name="email">
                </div>
                <div class="group">
                    <label>Password</label>
                    <input type="password" name="password">
                </div>
                <div class="remember-me">
                    <p>Remember Me</p>
                    <input type="checkbox" name="remember-me">
                </div>
    
                <button type="submit">Create Account</button>
                <RouterLink :to="{name: 'login'}"><a class="create-account">Login</a></RouterLink>
            </form>
    
        </div>

    </div>
</template>

<style scoped>
.login-form {
    margin: 0 auto;
    margin-top: 60px;
    width: 400px;
    padding: 20px;
    background-color: #f9f9f9fb;
    text-align: center;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.login-form h1 {
    color: #333;
    font-size: 24px;
    margin-bottom: 20px;
}

.login-form form {
    width: 90%;
    margin-top: 20px;
}

.group {
    margin-bottom: 20px;
}

.group label {
    display: block;
    text-align: left;
    color: #555;
    font-weight: bold;
    margin-bottom: 5px;
}

.group input[type="text"],
.group input[type="password"] {
    width: 90%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
}

.remember-me {
    display: flex;
    justify-content: left;
    color: #555;
    font-size: 14px;
}

.remember-me input[type="checkbox"] {
    margin-right: 5px;
}

button[type="submit"] {
    background-color: #007BFF;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
    transition: background-color 0.3s;
}

button[type="submit"]:hover {
    background-color: #0056b3;
}

.create-account {
    margin-top: 10px;
    margin-left: 10px;
}

.create-account a {
    text-decoration: none;
    color: #007BFF;
}

.create-account a:hover {
    text-decoration: underline;
}
</style>