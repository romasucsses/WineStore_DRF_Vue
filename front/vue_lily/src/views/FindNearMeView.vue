<script setup>
import { ref } from 'vue';

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

const searchQuery = ref('');
const searchResults = ref([]);
const allStores = ref([]);
const allStoresVisible = ref(true);


allStores.value = AddressSet.map((address, index) => ({
  address,
  link: LinksSet[index]
}));



function SearchAddress() {
  const Input = searchQuery.value;
  const matchingAddresses = AddressSet.filter(address => address.toLowerCase().includes(Input.toLowerCase()));
  if (matchingAddresses.length > 0) {
    searchResults.value = matchingAddresses.map((address, index) => ({
      address,
      link: LinksSet[AddressSet.indexOf(address)]
    }));
    
  }
}

function CheckKey(event) {
  if (event.key === 'Enter') {
    SearchAddress();
  }
}
</script>

<template>
  <div>
    <div class="main-block">
      <div class="content">
        <h2>Where you can buy our Wine</h2>
        <div style="text-align: center">
          <input type="text" placeholder="Write your address:" v-model="searchQuery" @keydown="CheckKey">
          <button class='btn-search' type='button' name='action' @click="SearchAddress">Check for results</button>
        </div>
        <p class="p-resutls-js">Search Results:</p>
        <div class="search-results" v-if="searchResults.length">
          <a v-for="result in searchResults" :key="result.address" :href="result.link" target="_blank">{{ result.address
            }}</a>
        </div>
        <p class="p-all-js" v-if="allStoresVisible">Our All Address</p>
        <div class="all-address" v-if="allStoresVisible">
          <a v-for="result in allStores" :key="result.address" :href="result.link" target="_blank">{{ result.address
            }}</a>
        </div>
      </div>
      <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d387194.06241208257!2d-74.30933616806763!3d40.69701926227439!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2z0J3RjNGOLdCZ0L7RgNC6LCDQodCo0JA!5e0!3m2!1sru!2s!4v1694957299661!5m2!1sru!2s"
        width="750" height="150" style="border:0;" allowfullscreen="" loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
  </div>
</template>

<style scoped>
  .main-block {
    background-color: #FFFFFF;
    text-align: center;
  }

  .content {
    margin: 40px;
    padding-top: 40px;
    padding-bottom: 40px;
  }

  h2 {
    font-size: 24px;
    color: #333;
    margin-bottom: 20px;
    text-align: center;
  }

  form {
    text-align: center;
    padding-bottom: 30px;
  }

  label {
    display: block;
    font-size: 16px;
    margin-bottom: 8px;
    color: #666;
  }

  input[type="text"] {
    max-width: 600px;
    width: 100%;
    padding: 10px;
    border: 2px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    margin-bottom: 20px;
  }

  button.btn-search {
    background-color: #000000;
    color: #FFFFFF;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    margin-right: 10px;
    transition: background-color 0.3s;
    border: 2px solid #000000;
    /* Added border to match the other button */
  }

  button.btn-search:hover {
    background-color: #FFFFFF;
    color: #000000;
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
  }

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

  .all-address a:hover {
    background-color: #729AEF;
  }

  iframe {
    margin: 40px;
    border-radius: 30px;
  }

    @media (max-width: 768px){
      iframe {
        width: 300px;
        border-radius: 30px;
      }
    }
</style>
