<template>

<v-card
  class="mx-auto mt-2"
  color="grey darken-2"
  flat
  dark>

  <v-layout align-center justify-start>
    <v-flex grow class="text-xs-left pl-3 mt-2 mb-2">
      <v-avatar :size="20" class="pr-2">
        <v-icon dark>person</v-icon>
      </v-avatar>
      <span>
        <span>{{ answer.author }}</span>
      </span>
      <div>
        <span class="grey--text">answered on: </span>
        <span>
          {{ answer.created_at }}
        </span>
      </div>
    </v-flex>
  </v-layout>

  <v-divider light></v-divider>

  <v-card-title primary-title>
    <div>
      <span class="subheading pre" v-html="$sanitize(answer.body)"></span>
    </div>
  </v-card-title>

  <v-divider light></v-divider>

  <v-card-actions>
    <v-layout align-center justify-end>

    </v-layout>
  </v-card-actions>

  <v-divider light></v-divider>

  </v-card>

</template>
<script>
export default {
  name: 'Answer',
  props: {
    answer: {
      type: Object,
      required: true
    }
  }
}
</script>
<style scoped>
.pre {
    white-space: pre-wrap;       /* Since CSS 2.1 */
    white-space: -moz-pre-wrap;  /* Mozilla, since 1999 */
    white-space: -pre-wrap;      /* Opera 4-6 */
    white-space: -o-pre-wrap;    /* Opera 7 */
    word-wrap: break-word;       /* Internet Explorer 5.5+ */
}
</style>
