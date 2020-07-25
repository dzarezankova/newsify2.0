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
        <v-btn fab small depressed>
          <v-icon color = "grey"> add </v-icon>
        </v-btn>
        </div>
      </v-row>
      <h4 class = "text-center mt-2"> News Articles </h4>
      <v-row>
      <v-col cols = 6>
      <v-card class = "mx-6" outlined rounded>
        <v-row justify = "center" align = "center">
            <v-col cols = 4 align = "center">
            <v-icon color = "#FBC02D" size = "3rem"> alarm </v-icon>
            </v-col>
            <v-col cols = 8>
              <div class = "text-right ma-n2 my-n4">
              <v-btn small text right @click = "show">
              <v-icon color = "#FBC02D"> expand_more</v-icon></v-btn></div>
               <h5 class = "mt-2 mr-2"> Coronavirus: the first three months as it happened</h5>
                <div class = "text--secondary mt-1" style = "font-size: 0.65em">NBC News </div>
            </v-col>
          </v-row>
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
  }),
};
</script>

<style scoped>
  .banner{
    border-bottom: 5px solid #FBC02D;
    margin-left: 25px;
    margin-right: 25px;
  }
</style>
