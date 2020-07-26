<template>
  <v-card class = "mx-6" outlined rounded v-if = "!deleted">
        <v-row justify = "center" align = "center">
            <v-col cols = 4 align = "center" justify = "center" class = "mt-4">
              <v-btn text small depressed @click = "deleted = true">
            <v-icon color = "#FBC02D" size = "3rem"> delete </v-icon> </v-btn>
            <div class = "text--secondary mt-2" style = "font-size: 0.65em">Delete </div>
            </v-col>
            <v-col cols = 8 align = "center" justify = "center">
              <div class = "text-right ma-n2 my-n4">
              <v-btn small text right @click = "expand = !expand">
              <v-icon color = "#FBC02D"> expand_more</v-icon></v-btn></div>
               <h5 class = "mt-4 mr-4 text-left"> {{title}} </h5>
                <div class = "text--secondary text-right mr-6"
                style = "font-size: 0.65em">{{company}} </div>
            </v-col>
          </v-row>
          <v-card-text v-if = "expand" class = " mt-1"
          style = "font-size: 0.7em"> {{text}} </v-card-text>
            </v-card>
</template>

<script>
export default {
  data: () => ({
    expand: false,
    deleted: false,
  }),

  props: ['title', 'text', 'deleted', 'company'],
};
</script>
