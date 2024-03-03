<script setup>
import NavMneu from '../components/NavMenu.vue'
import FooterMenu from '../components/FooterMenu.vue'

const AddressSet = [
    "3607 Broadway",
    "3790 Broadway, NY",
    "720 West 181st street",
    "2235 Frederick Douglass Blvd",
    "152 Wyckoff Ave, Brooklyn",
    "66-22 FOREST AVE, RIDGEWOOD"
];

const LinksSet = [
    "https://maps.app.goo.gl/cs2d1ZdU2R8aS1J79",
    "https://maps.app.goo.gl/WEWXwQwj4AH61jq17",
    "https://maps.app.goo.gl/jkcsRmqhRhJj1oLT7",
    "https://maps.app.goo.gl/TefsTKejmnN52CAY7",
    "https://maps.app.goo.gl/g3CmTXm5Fzp2eQWu5",
    "https://maps.app.goo.gl/rQbDK224unuF2E5E8"
];


function AllStores(){
    const ElementInner = document.querySelector(".allstores-js");
    for(let i=0; i < AddressSet.length; i++){
        console.log(`<a href="#" target="_blank">${AddressSet[i]}</a>`)
        ElementInner.innerHTML += `<a href="${LinksSet[i]}" target="_blank">${AddressSet[i]}</a>`;
    }

    document.querySelector(".p-all-js").innerHTML = "Our All Address";
};


function SearchAddress(){
    const Input = document.querySelector(".request-srch").value;
    const matchingAddresses = AddressSet.filter(address => address.toLowerCase().includes(Input.toLowerCase()));
    const DivResults = document.querySelector(".srch-results-js");
    const p_results_text = document.querySelector(".p-resutls-js");

    if (matchingAddresses !== null && matchingAddresses.length > 0){
        for (let i=0; i < matchingAddresses.length; i++){

            console.log(`<a href=
                "${LinksSet[AddressSet.indexOf(matchingAddresses[i])]}"
                target="_blank">${matchingAddresses[i]}
            </a>`);
    
            DivResults.innerHTML += `<a href=
                "${LinksSet[AddressSet.indexOf(matchingAddresses[i])]}"
                target="_blank">${matchingAddresses[i]}
            </a>`;
        }
        p_results_text.innerHTML = "Results: click on the address";
    }

    else{
        p_results_text.innerHTML = "Results:";
        DivResults.innerHTML = `<p>No mathching result please check the all addreses down</p>`;
        AllStores();
        
    };

};

function CheckKey(event){
    if(event.key === 'Enter'){
        console.log(event.key);
        return SearchAddress();
    }
}
</script>

<template>
    <div>
      
      <div class="main-block">
          <div class="content">
              <h2>Where you can buy our Wine</h2>
              <div>
                  <input type="text" placeholder="Write your addres:" class="request-srch" onkeydown="CheckKey(event)">
                  <button class='btn-search' type='button' name='action' value="search_stores" onclick="SearchAddress()">Check for results</button>
                  <button class='btn-showall' type="button" onclick="AllStores()">See All Stores</button>
              </div>
              <p class="p-resutls-js"></p>
              <div class="search-results srch-results-js">
      
              </div>
      
              <p class="p-all-js"></p>
              <div class="all-address allstores-js">
      
              </div>
          </div>
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d387194.06241208257!2d-74.30933616806763!3d40.69701926227439!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2z0J3RjNGOLdCZ0L7RgNC6LCDQodCo0JA!5e0!3m2!1sru!2s!4v1694957299661!5m2!1sru!2s" width="550" height="150" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
      
    </div>
</template>

<style scoped>
/* edinting main block */

  .main-block{
      background-color: #FFFFFF;
  }

  .content{
      margin: 40px;
      padding-top: 40px;
      padding-bottom: 40px;
  }

  /* Style for the heading */
  h2 {
      font-size: 24px;
      color: #333;
      margin-bottom: 20px;
      text-align: center;
    }
    
    /* Style for the form container */
    form {
      text-align: center;
      padding-bottom: 30px;
    }
    
    /* Style for the label */
    label {
      display: block;
      font-size: 16px;
      margin-bottom: 8px;
      color: #666;
    }
    
    /* Style for the input field */
    input[type="text"] {
      max-width: 600px;
      width: 100%;
      padding: 10px;
      border: 2px solid #ccc;
      border-radius: 5px;
      font-size: 16px;
      margin-bottom: 20px;
    }
    
    /* Style for the search button */
    button.btn-search {
      background-color: #000000;
      color: #FFFFFF;
      border-radius: 5px;
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
      margin-right: 10px;
      transition: background-color 0.3s;
    }
    
    button.btn-search:hover {
      background-color: #FFFFFF;
      color: #000000;
    }
    
    /* Style for the show all button */
    button.btn-showall {
      background-color: #FFFFFF;
      color: #000000;
      border-color: #000000;
      border-radius: 5px;
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
      transition: background-color 0.3s;
    }
    
    button.btn-showall:hover {
      background-color: #000000;
      color: #FFFFFF;
    }


  .content p {
      margin-top: 40px;
      font-size: 18px;
      color: #333;
      text-align: center;
      padding: 10px;
      background-color: #f2f2f2;
      border-radius: 5px;
      cursor: pointer;
      transition: background-color 0.3s, color 0.3s;
  }

  .search-results {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px;
  }

  .search-results a {
      text-decoration: none;
      background-color: #5B606A;
      color: #fff;
      padding: 10px 20px;
      border-radius: 5px;
      font-size: 16px;
      margin: 5px;
      transition: background-color 0.3s, color 0.3s;
    }

    .search-results a:hover {
      background-color: #729AEF;
    }

  .all-address {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      /* gap: 10px; */
    }
    
    /* Style for the address links */
    .all-address a {
      text-decoration: none;
      background-color: #5B606A;
      color: #fff;
      padding: 10px 20px;
      border-radius: 5px;
      font-size: 16px;
      margin: 5px;
      transition: background-color 0.3s, color 0.3s;
    }
    
    /* Hover effect */
    .all-address a:hover {
      background-color: #729AEF;
    }
    

  iframe{
      margin: 40px;
      border-radius: 30px;
  }
</style>