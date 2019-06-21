<template>
  <v-card
    class="mx-auto"
    color="grey--darken-3"
    flat
    dark>

    <v-layout align-center justify-start>
      <v-flex shrink>
        <v-tooltip bottom>
          <v-btn flat icon exact :to="{ name: 'home' }" slot="activator">
            <v-icon>navigate_before</v-icon>
          </v-btn>
          <span>Back</span>
        </v-tooltip>
      </v-flex>
      <v-flex grow class="text-xs-right pr-3">
        <v-avatar :size="20" class="pr-2">
          <v-icon dark>person</v-icon>
        </v-avatar>
        <span>
          <span>{{ question.author }}</span>
        </span>
        <div>
          <span class="grey--text">asked on: </span>
          <span>
            {{ question.created_at }}
          </span>
        </div>
      </v-flex>
    </v-layout>
    <v-divider light></v-divider>
    <v-card-title primary-title>
      <div>
        <pre class="headline" v-html="question.content"></pre>
      </div>
    </v-card-title>
    <v-divider light></v-divider>
    <v-card-actions>
      <v-layout
        align-center
        justify-end
      >
        <v-chip color="green">
          <v-avatar class="green darken-4">{{ question.answers_count }}</v-avatar>
          Answers
        </v-chip>
      </v-layout>
    </v-card-actions>

  </v-card>
</template>
<script>
import { apiService } from '../common/api.service'
export default {
  name: 'question',
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      question: {}
    }
  },
  methods: {
    setPageTitle (title) {
      document.title = title
    },
    getQuestionData () {
      let endpoint = `/api/questions/${this.slug}/`
      apiService.get(endpoint)
        .then(response => {
          this.question = response.data
          this.setPageTitle(`QandA - ${this.question.slug}`)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  mounted () {
    this.getQuestionData()
  }
}
</script>
<style scoped>
pre {
    white-space: pre-wrap;       /* Since CSS 2.1 */
    white-space: -moz-pre-wrap;  /* Mozilla, since 1999 */
    white-space: -pre-wrap;      /* Opera 4-6 */
    white-space: -o-pre-wrap;    /* Opera 7 */
    word-wrap: break-word;       /* Internet Explorer 5.5+ */
}
</style>
