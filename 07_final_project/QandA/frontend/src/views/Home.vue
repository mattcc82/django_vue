<template>
  <div class="home">
    <v-layout align-center justify-start class="text-xs-center">
      <v-tooltip right>
        <v-btn fab dark large color="grey darken-3" slot="activator" exact :to="{ name: 'ask' }">
          <v-icon dark style="height:auto;">add_comment</v-icon>
        </v-btn>
        <span>Ask a Question</span>
      </v-tooltip>
    </v-layout>

    <h2>Questions</h2>
    <v-list two-line>
      <v-slide-y-reverse-transition group>
        <template v-for="(question, index) in questions">
          <v-list-tile :key="question.id" avatar :to="{ name: 'question', params: { slug: question.slug } }">
            <v-list-tile-avatar>
              <v-icon>person</v-icon>
            </v-list-tile-avatar>

            <v-list-tile-content>
              <v-list-tile-title>
                <v-icon>open_in_new</v-icon>
                {{ question.content }}
              </v-list-tile-title>
              <v-list-tile-sub-title>
                <v-chip color="green">
                  <v-avatar class="green darken-4">{{ question.answers_count }}</v-avatar>
                  Answers
                </v-chip>
                asked by: <v-chip>{{ question.author }}</v-chip>
                on: <v-chip>{{ question.created_at }}</v-chip>
              </v-list-tile-sub-title>
            </v-list-tile-content>

          </v-list-tile>
          <v-divider :key="`${question.id}_${index}`"></v-divider>
        </template>
      </v-slide-y-reverse-transition>
    </v-list>

    <v-btn v-show="next" block outline color="white" dark @click="getQuestions">
      <v-progress-circular
        v-if="loading"
        indeterminate
        color="white"
      ></v-progress-circular>
      See More
    </v-btn>

    <v-snackbar
      v-model="error"
      :timeout="6000"
    >
      {{ errorText }}
      <v-btn
        dark
        flat
        @click="error = false"
      >
        Close
      </v-btn>
    </v-snackbar>

  </div>
</template>

<script>
import { apiService } from '../common/api.service'
export default {
  name: 'home',
  data () {
    return {
      questions: [],
      next: null,
      loading: false,
      error: null,
      errorText: ''
    }
  },
  methods: {
    getQuestions () {
      this.loading = true
      let endpoint = 'api/questions/'
      if (this.next) {
        endpoint = this.next
      }
      apiService.get(endpoint)
        .then(response => {
          this.questions.push(...response.data.results)
          if (response.data.next) {
            this.next = response.data.next
          } else {
            this.next = null
          }
          this.loading = false
        })
        .catch(error => {
          this.error = true
          this.errorText = error
        })
    }
  },
  mounted () {
    this.getQuestions()
    document.title = 'QandA'
  }
}

</script>

<style>
.primary--text .v-list__tile__title {
    color: #fff !important;
    caret-color: #fff !important;
}
</style>
