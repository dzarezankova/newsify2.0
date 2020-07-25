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
                <v-form class = "px-3">
                  <v-text-field label = "Insert URL" v-model = "URL"
                  prepend-icon = "link" :rules = "inputRules"></v-text-field>
                  <v-btn flat small color = "#FBC02D" @click = "validate">Summarize</v-btn>
                </v-form>
              </v-card-text>
            </v-card>
            </v-dialog>
          </div>
      </v-row>
      <h4 class = "text-center mt-2"> News Articles </h4>
      <v-row>
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
               <h5 class = "mt-4 mr-4 text-left"> Coronavirus:
                 the first three months as it happened </h5>
                <div class = "text--secondary text-right mr-6"
                style = "font-size: 0.65em">NBC News </div>
            </v-col>
          </v-row>
          <v-card-text v-if = "expand" class = " mt-1" style = "font-size: 0.7em">
                  Show this shitShow this shitShow this shitShow this shitShow this shit
                  Show this shitShow this shitShow this shitShow this shitShow this
                  shitShow this shit
                  Show this shitShow this shitShow this shitShow this shit </v-card-text>
            </v-card>
            </v-col>
      </v-row>
    </v-content>
  </v-app>
</template>
<script>

export default {
  name: 'App',
  data: () => ({
    expand: false,
    dialog: false,
    URL: '',
    inputRules: [
      v => !!v || 'Name is required',
    ],
  }),

  methods: {
    validate() {
      this.$refs.form.validate();
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
