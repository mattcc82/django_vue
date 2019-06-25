<template>
  <div>

    <v-card class="mx-auto" color="grey--darken-3" flat dark>

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

      <v-divider dark></v-divider>

      <v-card-title primary-title>
        <div>
          <span class="headline pre" v-html="$sanitize(question.content)"></span>
        </div>
      </v-card-title>

      <v-divider dark></v-divider>

      <v-card-actions>
        <v-layout align-center justify-end>
          <v-slide-x-transition group>
            <v-chip flat icon v-if="userHasAnswered" key="answered">
              <v-avatar>
                <v-icon>done</v-icon>
              </v-avatar>
              Thanks for your answer!
            </v-chip>
            <span v-if="!userHasAnswered" key="leaveAnswer">
              <v-tooltip left>
                <v-btn fab small icon dark slot="activator" color="success" @click="showAnswerForm = true">
                  <v-icon dark style="height:auto;">add_comment</v-icon>
                </v-btn>
                <span>Answer the Question</span>
              </v-tooltip>
            </span>
          </v-slide-x-transition>
          <v-chip color="green">
            <v-avatar class="green darken-4">{{ answerCount }}</v-avatar>
            Answers
          </v-chip>
        </v-layout>
      </v-card-actions>

    </v-card>

    <v-divider color="blue"></v-divider>

    <v-slide-x-transition mode="out-in">

      <v-layout v-if="showAnswerForm" align-center justify-start>
        <v-flex class="ml-4">
          <v-card color="grey darken-4">
            <v-card-title>
              <span class="subheading text--grey">Answer the question</span>
            </v-card-title>
            <v-card-text>
              <v-form ref="answerForm" v-model="validAnswer" lazy-validation @keyup.enter="submit">
                <v-container>
                  <v-layout row wrap>
                    <v-flex xs12>
                      <v-textarea
                        v-model="newAnswer"
                        auto-grow
                        name="answer-input"
                        label="Answer the question here - "
                        hint="Nice Answer!"
                        :rules="answerRules"
                        :counter=answerMax
                      ></v-textarea>
                    </v-flex>
                  </v-layout>
                </v-container>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-layout align-center justify-end>
                <v-flex>
                  <v-btn :disabled="!validAnswer" @click="submit">Answer</v-btn>
                  <v-btn @click="reset">Clear</v-btn>
                </v-flex>
              </v-layout>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-slide-x-transition>

    <v-slide-x-reverse-transition group>
      <Answer
        class="ml-4"
        v-for="(answer, index) in answers"
        :key="index"
        :answer="answer" />
    </v-slide-x-reverse-transition>

    <v-flex class="ml-4">
      <v-btn v-show="next" block outline color="white" dark @click="getQuestionAnswers">
        <v-progress-circular
          v-if="loading"
          indeterminate
          color="white"
        ></v-progress-circular>
        See More
      </v-btn>
    </v-flex>

    <v-snackbar v-model="error" :timeout="6000">
      {{ errorText }}
      <v-btn dark flat @click="error = false">
        Close
      </v-btn>
    </v-snackbar>
  </div>
</template>
<script>
import { apiService } from '@/common/api.service'
import Answer from '@/components/Answer'
export default {
  name: 'question',
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  components: {
    Answer
  },
  data () {
    return {
      question: {},
      answers: [],
      answerCount: 0,
      next: null,
      loading: false,
      newAnswer: null,
      newAnswerOffset: false,
      userHasAnswered: false,
      showAnswerForm: false,
      answerMax: 240,
      answerRules: [
        v => !!v || 'Answer is Required!',
        v => (v && v.length <= this.answerMax) || 'Answer must be less than 240 characters!'
      ],
      error: null,
      errorText: '',
      validAnswer: true
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
          this.answerCount = this.question.answers_count
          this.setPageTitle(`QandA - ${this.question.slug}`)
          this.userHasAnswered = response.data.user_has_answered
        })
        .catch(error => {
          this.error = true
          this.errorText = error
        })
    },
    getQuestionAnswers () {
      this.loading = true
      let endpoint = `/api/questions/${this.slug}/answers/`
      if (this.next) {
        endpoint = this.next
      }
      apiService.get(endpoint)
        .then(response => {
          let results = response.data.results
          if (this.newAnswerOffset) {
            results.shift()
            this.newAnswerOffset = false
          }
          this.answers.push(...results)
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
    },
    submit () {
      if (this.$refs.answerForm.validate()) {
        let endpoint = `/api/questions/${this.slug}/answer/`
        apiService.post(endpoint, { body: this.$sanitize(this.newAnswer) })
          .then(response => {
            this.answers.unshift(response.data)
            this.answerCount++
            this.newAnswer = null
            this.newAnswerOffset = true
            this.showAnswerForm = false
            this.userHasAnswered = true
            this.error = false
            this.errorText = ''
          })
          .catch(error => {
            this.error = true
            this.errorText = error
          })
      }
    },
    reset () {
      this.$refs.answerForm.reset()
    }
  },
  mounted () {
    this.getQuestionData()
    this.getQuestionAnswers()
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
