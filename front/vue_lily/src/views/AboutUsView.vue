<script setup>
    const person_url =  "../../public/pages/images/team-photos/" ;

    const team_people = [
        { name: "Victor Costin", position: "CEO - Founder" },
        { name: "Lily Costin",position: "CFO" },
        { name: "Rachel Zain", position: "Marketing Head" },
        { name: "Roma Costin", position: "Web Devoloper" },
        { name: "Katrina Bennett", position: "Call Operator" },
        { name: "Eugen Pantus", position: "Brand Manger" }
    ]
    
</script>

<template>
    
    <div>
      

      <div class="main-block">
        <h4 class="few-words">A Few Words About</h4>
        <div class="content">
          <div class="left-block">
            <h2>Who We Are</h2>
            <p>
              La Fleur Lily is a wine brand created by Victor and Lily, a young
              family who immigrated to the United States from Europe in search of
              a better life. Upon arriving in New York, Lily began searching for
              her favorite semi-sweet wine that would suit her taste, but Victor,
              who knew a lot about wines thanks to his family of winemakers,
              decided to find a true, quality wine with no additives for her. In
              search of the perfect wine for Lily, Victor traveled the world and
              finally, in 2004, he met a young man who inherited winemaking from
              his parents. This young man was a talented winemaker who created a
              unique wine that matched Lily's character, romantic and
              free-spirited. Victor asked him to taste the wine and realized that
              this was what he was looking for. They named the wine La Fleur Lily
              in honor of Lily and began working together to create more
              high-quality wines. Since then, La Fleur Lily has a portfolio of 12
              wines that sell very well. In 2023, La Fleur Lily received an
              organic certification in France, which confirms their constant
              pursuit of high quality and care for the environment. Thanks to the
              talent and efforts of Victor and the young winemaker, La Fleur Lily
              has become not only Lily's favorite wine but also one of the most
              popular wine brands in the market.
            </p>
          </div>
          <img src="../../public/pages/images/site-img/right-block.jpg" />
        </div>
      </div>
      <div class="our-team-block">
        <h2 class="header-team">Our Team</h2>
        <p class="title-team">
          At La Fleur LIly, we believe in the power of collaboration, innovation,
          and a shared vision. Our diverse and talented team is the driving force
          behind our success, working together to create exceptional solutions and
          deliver outstanding results. Get to know the extraordinary individuals
          who make up our team and discover the passion, expertise, and dedication
          that sets us apart.
        </p>
        <div class="people">
          <div class="card" v-for="person in team_people" :key="person.name">
              <img :src="`${person_url + String(team_people.indexOf(person) + 1)}.png`">
              <h4 class="name">{{ person.name }}</h4>
              <p class="position">{{ person.position }}</p>
          </div>
        </div>
      </div>
      <div class="follow-us-block">
        <div class="center-links">
          <h2>Follow Us</h2>
          <div class="social-media">
            <a href="https://www.facebook.com/profile.php?id=100067500445783">
              <img src="../../public/pages/images/site-img/icons-footer/facebook-footer.svg" >
            </a>
            <a href="https://www.instagram.com/lafleurlilywine/">
              <img src="../../public/pages/images/site-img/icons-footer/instagram-footer.png" >
            </a>
            <a href="https://www.pinterest.com/lafleurlilywine/">
              <img src="../../public/pages/images/site-img/icons-footer/pinterest-footer.svg" >
            </a>
          </div>
        </div>
      </div>

     
    </div>
  
</template>

<style scoped>
.main-block{
    margin-top: 50px;
    margin: 40px;
    text-align: center;


}

.content{
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}
.main-block .left-block{
    font-size: 24px;
    max-width: 520px;
    margin-left: 50px;
}
.main-block .few-words{
    font-size: 40px;
    text-align: center;
    margin-bottom: 40px;
}
.left-block h2{
    font-size: 42px;
}
.left-block p{
    font-size: 16px;
    line-height: 1.9;

}

.main-block img{
    width: 400px;
    height: 450px;
    margin-right: 8%;
    margin-bottom: 5%;
    object-fit: cover;
    object-position: right;

    
    
}


.our-team-block{
    margin-top: 100px;
    margin: 15px;
    text-align: center;

}


.header-team{
    margin-top: 40px;
    font-size: 42px;
    margin: 0 auto;
    margin-bottom: 30px;
}

.title-team{
    font-size: 16px;
    width: 600px;
    line-height: 1.5;

    margin: 0 auto;
}



.people{
    display: flex;
    justify-content: center;
    max-width: 1200px;
    flex-wrap: wrap;
    margin: 50px;
}

.people .card{
    text-align: center;
    width: 260px;
    height: 250px;
    border-radius: 10px;
    background-color: #F5F7F9;
    margin: 20px;
}

.people .card img{
    margin-top: 15px;
    width: 90px;
    height: 90px;
}

.follow-us-block{
    background-image: url(../../public/pages/images/site-img/back_aboutus.jpg);
    text-align: center;
    position: relative;
    height: 400px;
    background-size: cover;
    background-attachment: fixed;
}

.center-links{
    background-color: #FFFFFF;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;

    margin: 0 auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    
    width: 500px;
    height: 400px;
}

.social-media{
    display: flex;
    justify-content: center;
    
}

.social-media img{
    width: 30px;
    height: 30px;
    padding: 30px;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .main-block {
    margin: 20px;
  }

  .content {
    flex-direction: column;
    align-items: center;
  }

  .main-block .left-block {
    margin-left: 0;
    font-size: 18px;
  }

  .main-block img {
    margin-right: 0;
    margin-bottom: 20px;
    width: 100%;
    height: auto;
  }

  .header-team,
  .left-block h2 {
    font-size: 32px;
  }

  .title-team {
    width: 100%;
    font-size: 14px;
  }

  .people .card {
    width: 100%;
    height: auto;
    margin: 10px 0;
  }

  .people .card img {
    width: 70px;
    height: 70px;
  }

  

  .center-links {
    width: 40%;
    height: 40%;
    margin-top: 30%;
    padding: 20px;
  }

  


    .social-media {
      display: flex;
      justify-content: center;
      
    }
  
    .social-media img {
      
      width: 25px;
      height: 25px;
      padding: 20px;
    }

    
}

</style>

