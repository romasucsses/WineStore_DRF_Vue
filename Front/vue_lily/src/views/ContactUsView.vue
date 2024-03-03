<script setup>
    import NavMneu from '../components/NavMenu.vue'
    import FooterMenu from '../components/FooterMenu.vue'

    const phone_numbers = [
        { depo: "Contact Us", contact:"1(718) 809-9182" },
        { depo: "Complaints", contact:"1(929)355-4426" },
        { depo: "Founder", contact:"lvc.incorp@gmail.com" },
        { depo: "Marketing", contact:"1(212)537-6979" }
    ]
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
          <!-- <div class="card">
            <h3>Complaints</h3>
            <h4>1(929)355-4426</h4>
          </div>
          <div class="card">
            <h3>Founder</h3>
            <h4>lvc.incorp@gmail.com</h4>
          </div>
          <div class="card">
            <h3>Marketing</h3>
            <h4>1(212)537-6979</h4>
          </div> -->
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
          <form method="post">
              {% csrf_token %}
              <input name="name" placeholder="NAME">
              <input name="subject" placeholder="SUBJECT">
              <input name="email"  placeholder="EMAIL">
              <input name="message" id='msg-input' placeholder="MESSAGE">
              <button  type="submit" name="action" value="send-msg">SEND MESSAGE</button>
          </form>
        </div>
      </div>
      
    </div>
</template>

<style scoped>
/*editing  main block */

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
    gap: 20px; /* Adds space between the cards */
    flex-wrap: wrap; /* Allows for multiple rows of cards */
  }

  .phone-numbers .card {
    width: 250px;
    border: 1px solid #000000;
    border-radius: 9px;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Adds a subtle shadow effect */
    text-align: center;
  }

  .phone-numbers .card h3 {
    font-size: 24px;
    color: #007bff; /* Blue color for the headings */
    margin-bottom: 10px;
  }

  .phone-numbers .card h4 {
    font-size: 18px;
    color: #333; /* Dark gray color for the content */
  }

  /* Hover effect for the cards */
  .phone-numbers .card:hover {
    transform: scale(1.05); /* Enlarge the card on hover */
    transition: transform 0.3s ease;
  }


  /* Style for the contact container */
  .contact {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 50px;
    background-color: #f2f3fa;
  }

  /* Style for the left block */
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

  /* Style for the right block */
  .right-block {
    flex: 1;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  }

  .right-block form {
    display: flex;
    flex-direction: column;
    align-items: center;
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
</style>