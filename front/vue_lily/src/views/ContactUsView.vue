<script setup>
  import { DOMAIN_NAME } from '@/utils/api_links';
  import axios from 'axios';

    const phone_numbers = [
        { depo: "Contact Us", contact:"1(718) 809-9182" },
        { depo: "Complaints", contact:"1(929)355-4426" },
        { depo: "Founder", contact:"lvc.incorp@gmail.com" },
        { depo: "Marketing", contact:"1(212)537-6979" }
    ]

    let name;
    let subject;
    let email;
    let msg;

    function sendMsg(){
      const FinalEndPoint = DOMAIN_NAME + 'orders/contact-us/';
      axios.post(FinalEndPoint, {
        name: name,
        subject: subject,
        email: email,
        message: msg
      }).then((response) => {
        console.log(response);
        window.location.reload();
      })
    }
</script>

<template>
    <div>
      
      <div class="header-block">
        <h1>Contact Us</h1>
      
      </div>
      <div class="phone-numbers">
          <div class="card" v-for="each in phone_numbers" :key="each">
            <h3>{{ each.depo }}</h3>
            <h4>{{ each.contact }}</h4>
          </div>
      </div>
      <div class="contact">
      
        <div class="left-block">
          <h2>We're here to help</h2>
          <h6>Don't be a stranger!</h6>
          <h2>You tell us. We listen.</h2>
          <p>
            Welcome to our Contact Us page! We value your feedback, inquiries, and
            suggestions, and we’re here to provide you with the support you need.
            Whether you have a question about our products or services, need
            assistance with an order, or simply want to share your thoughts, this
            is the place to connect with us.
          </p>
        </div>
        <div class="right-block">
          <div>
              <input name="name" placeholder="NAME" v-model="name">
              <input name="subject" placeholder="SUBJECT" v-model="subject">
              <input name="email"  placeholder="EMAIL" v-model="email">
              <input name="message" id='msg-input' placeholder="MESSAGE" v-model="msg">
              <button  name="action" @click="sendMsg()" >SEND MESSAGE</button>
          </div>
        </div>
      </div>
      
    </div>
</template>

<style scoped>

  .header-block h1{
    text-align: center;
    font-size: 50px;
    margin-bottom: 90px;
    color: #333;
  }




  .phone-numbers {
    margin-top: 90px;
    margin-bottom: 90px;
    display: flex;
    justify-content: center;
    gap: 20px; 
    flex-wrap: wrap; 
  }

  .phone-numbers .card {
    width: 250px;
    border: 1px solid #000000;
    border-radius: 9px;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); 
    text-align: center;
  }

  .phone-numbers .card h3 {
    font-size: 24px;
    color: #007bff; 
    margin-bottom: 10px;
  }

  .phone-numbers .card h4 {
    font-size: 18px;
    color: #333; 
  }

  
  .phone-numbers .card:hover {
    transform: scale(1.05); 
    transition: transform 0.3s ease;
  }


 
  .contact {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 50px;
    background-color: #f2f3fa;
  }

  .left-block {
    flex: 1;
    padding: 20px;
    color: #333;
  }

  .left-block h6 {
    font-size: 18px;
    color: #0084d6;
  }

  .left-block h2 {
    font-size: 32px;
    margin: 10px 0;
  }

  .left-block p {
    font-size: 16px;
    line-height: 1.5;
  }

  .right-block {
    text-align: center;
    flex: 1;
    padding: 12px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  }

  .right-block  {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 45%;
  }

  .right-block input,
  .right-block button {
    width: 80%;
    padding: 10px;
    margin: 10px 0;
    border: none;
    border-radius: 4px;
  }

  .right-block input {
    background-color: #f2f3fa;
  }

  #msg-input{
    height: 80px;
  }

  .right-block button {
    background-color: #0084d6;
    color: #fff;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .right-block button:hover {
    background-color: #f2f3fa;
    color: #0084d6;
  }
  /* Responsive Styles */
  @media (max-width: 768px) {
    .header-block h1 {
      font-size: 36px;
      margin-bottom: 60px;
    }

    .phone-numbers {
      flex-direction: column;
      align-items: center;
    }

    .contact {
      flex-direction: column;
      padding: 20px;
    }

    .right-block {
      max-width: 100%;
    }

    .left-block,
    .right-block {
      padding: 10px;
    }

    .left-block h2 {
      font-size: 24px;
    }

    .left-block p {
      font-size: 14px;
    }

    .right-block input,
    .right-block button {
      width: 90%;
    }
  }
</style>