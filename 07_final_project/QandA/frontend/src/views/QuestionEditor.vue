<template>
  <div>

    <v-tooltip right>
      <v-btn flat icon exact :to="{ name: 'home' }" slot="activator">
        <v-icon>navigate_before</v-icon>
      </v-btn>
      <span>Back</span>
    </v-tooltip>

    <h2>Ask your question</h2>
    <v-form ref="questionForm" v-model="valid" lazy-validation @keyup.enter="submit">
      <v-container>
        <v-layout row wrap>
          <v-flex xs12>
            <v-textarea
              v-model="question"
              auto-grow
              no-resize
              name="input-7-1"
              label="Ask your question here - "
              hint="Ask Away!"
              :rules="questionRules"
              :counter=questionMax
            ></v-textarea>
          </v-flex>
          <v-flex xs12>
            <v-btn :disabled="!valid" @click="submit">Ask</v-btn>
            <v-btn @click="reset">Clear</v-btn>
          </v-flex>
        </v-layout>
      </v-container>
    </v-form>
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
  name: 'QuestionEditor',
  data () {
    return {
      question: null,
      questionMax: 240,
      questionRules: [
        v => !!v || 'Question is Required!',
        v => (v && v.length >= 10 && v.length <= this.questionMax) || 'Question must be between 10 and 240 characters!'
      ],
      error: false,
      errorText: null,
      valid: true
    }
  },
  methods: {
    submit () {
      if (this.$refs.questionForm.validate()) {
        let endpoint = '/api/questions/'
        apiService.post(endpoint, { content: this.question })
          .then(response => {
            this.$router.push({
              name: 'question',
              params: { slug: response.data.slug }
            })
          })
          .catch(error => {
            this.error = true
            this.errorText = error
          })
      }
    },
    reset () {
      this.$refs.questionForm.reset()
    }
  },
  mounted () {
    document.title = 'QandA - Editor'
  }
}
</script>
