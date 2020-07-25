<template>
  <v-app>
    <v-content>
      <v-row :class = "`banner px-6`" align = "center" justify = "space-around">
        <div class = "text-center">
          <h3 class = "font-weight-medium grey--text text--darken-1"> Newsify </h3>
          <div class = "text--secondary" style = "font-size: 0.65em">
        summarize covid-19 articles</div>
        </div>
        <div class = "ma-2">
            <v-btn fab small depressed @click.stop="dialog = true">
              <v-icon color = "grey"> add </v-icon>
            </v-btn>
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
      <h4 class = "text-center mt-2"> News Articles </h4>
      <v-row v-for = "article in articles" :key = "article">
      <v-col cols = 4>
      <v-card class = "mx-6" outlined rounded>
        <v-row justify = "center" align = "center">
            <v-col cols = 4 align = "center" justify = "center" class = "mt-4">
              <v-btn text small depressed>
            <v-icon color = "#FBC02D" size = "3rem"> delete </v-icon> </v-btn>
            <div class = "text--secondary mt-2" style = "font-size: 0.65em">Delete </div>
            </v-col>
            <v-col cols = 8 align = "center" justify = "center">
              <div class = "text-right ma-n2 my-n4">
              <v-btn small text right @click = "expand = !expand">
              <v-icon color = "#FBC02D"> expand_more</v-icon></v-btn></div>
               <h5 class = "mt-4 mr-4 text-left"> {{article.title}} </h5>
                <div class = "text--secondary text-right mr-6"
                style = "font-size: 0.65em">NBC News </div>
            </v-col>
          </v-row>
          <v-card-text v-if = "expand" class = " mt-1" style = "font-size: 0.7em">
                   </v-card-text>
            </v-card>
            </v-col>
      </v-row>
    </v-content>
  </v-app>
</template>

<script>
// const urlExists = require('url-exists');
const axios = require('axios');

export default {
  name: 'App',
  data: () => ({
    expand: false,
    dialog: false,
    URL: '',
    inputRules: [
      (value) => !!value || 'Required.',
      (value) => !this.isValidURL(value),
    ],
    loading: false,
    article: [
      { title: 'Title 1', text: 'Show this shitShow this shitShow this shitShow this shitShow this shit Show this shitShow this shitShow this shitShow this shitShow this shitShow this shitShow this shitShow this shitShow this shitShow this shit' },
    ],
  }),

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
      console.log('in fetchtext');
      axios.post('http://localhost:8081', {
        URL: this.URL,
      })
        .then((response) => {
          this.loading = false;
          this.text = response; // add text and then title and then add to array
          this.dialog = false;
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
</style>
