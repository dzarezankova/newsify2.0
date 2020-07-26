<template>
  <v-app>
    <v-content>
      <v-row :class = "`banner px-6`" align = "center">
        <div class = "ma-2 text-center">
            <v-btn fab small depressed @click.stop="dialog = true" class = "mt-6">
              <v-icon color = "grey"> add </v-icon>
            </v-btn>
            <div class = "text--secondary text-center text-overline"
                style = "font-size: 0.65em"> Add Article</div>
            <v-dialog
              v-model="dialog"
              max-width="290"
            >
            <v-card>
              <v-card-title>Add New Article</v-card-title>
              <v-card-text>
                <v-form class = "px-3" ref = "form">
                   <div v-if= "noerrors">
                    <h1>Please correct the following error(s):</h1>
                    <ul>
                      <li v-for= "error in errors" :key = "error">{{ error }}</li>
                    </ul>
                  </div>
                  <v-text-field label = "Insert URL" v-model = "URL"
                  prepend-icon = "link" :rules = "[
      (value) => !!value || 'Required.',
      (value) => this.isValidURL(value),
    ]">
                  </v-text-field>
                  <v-btn flat small class = "mt-4" color = "#FBC02D"
                  @click = "submit" :loading = loading>Summarize</v-btn>
                </v-form>
              </v-card-text>
            </v-card>
            </v-dialog>
          </div>
      </v-row>
          <h1 class = "font-weight-medium grey--text text--darken-1 text-center
          mt-2 text-overline"> Newsify </h1>
      <v-row>
      <v-col cols = 4 v-for = "article in articles" :key = "article.item" :class = "`fixed`">
        <helloworld :title = "article.title" :text = "article.text"
        :company = 'article.company'></helloworld>
      </v-col>
      </v-row>
    </v-content>
  </v-app>
</template>
<script>
// const urlExists = require('url-exists');
import helloworld from './components/HelloWorld.vue';

const axios = require('axios');

export default {
  name: 'App',
  data: () => ({
    dialog: false,
    URL: '',
    inputRules: [
      (value) => !!value || 'Required.',
      (value) => !this.isValidURL(value),
    ],
    loading: false,
    articles: [
      { title: 'Coronavirus: the first three months as it happened ', company: 'NBC News', text: 'As of April 5, Global News is only reporting lab-confirmed cases for British Columbia, Alberta and Manitoba, where provincial health authorities are including probable and “epidemiologically-linked” cases in their official count.' },
      { title: 'Coronavirus: Wow', company: 'CBC News', text: 'Newly confirmed COVID-19 cases reported by the provinces have brought the national total to over 113,000 cases and more than 8,800 deaths. More than 99,000 people have since recovered — more than 88 per cent of the remaining confirmed cases. More than 4.3 million people have been tested.' },
      { title: 'The risks behind Covid-19 ', company: 'NBC News', text: 'Data provided by the Public Health Agency of Canada shows that most cases are the result of community spread, while a little less than a quarter are the result of travelling or close contact with a traveller.' },
    ],
  }),

  components: {
    helloworld,
  },

  methods: {
    submit() {
      if (this.$refs.form.validate()) {
        this.loading = true;
        console.log('you submitted');
        this.fetchText();
      }
    },

    isValidURL(str) {
      const pattern = new RegExp('^(https?:\\/\\/)?' // protocol
      + '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' // domain name
      + '((\\d{1,3}\\.){3}\\d{1,3}))' // OR ip (v4) address
      + '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' // port and path
      + '(\\?[;&a-z\\d%_.~+=-]*)?' // query string
      + '(\\#[-a-z\\d_]*)?$', 'i'); // fragment locator
      return !!pattern.test(str);
    },

    fetchText() {
      axios.post('http://localhost:8081', {
        URL: this.URL,
      })
        .then((response) => {
          this.loading = false;
          const insert = {};
          insert.text = response.data.URL;
          insert.title = response.data.title;
          this.articles.unshift(insert);
          this.dialog = false;
          console.log(response);
        });
      console.log(this.dialog);
    },
  },
};
</script>

<style scoped>
  .banner{
    border-bottom: 5px solid #FBC02D;
    margin-left: 25px;
    margin-right: 25px;
  }

  .top {
    border-top: 5px solid #FBC02D;
    margin-left: 25px;
    margin-right: 25px;
  }
</style>
