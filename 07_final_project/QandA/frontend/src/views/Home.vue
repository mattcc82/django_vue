<template>
  <div class="home">
    <h2>Questions</h2>
    <v-list two-line>
      <template v-for="(question, index) in questions">
        <v-list-tile :key="question.id" avatar @click="">
          <v-list-tile-avatar>
            <v-icon>person</v-icon>
          </v-list-tile-avatar>

          <v-list-tile-content>
            <v-list-tile-title>{{ question.content }}</v-list-tile-title>
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
    </v-list>
  </div>
</template>

<script>
import { apiService } from '../common/api.service'
export default {
  name: 'home',
  data () {
    return {
      questions: []
    }
  },
  methods: {
    getQuestions () {
      let endpoint = 'api/questions/'
      apiService.get(endpoint)
        .then(response => {
          this.questions.push(...response.data.results)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  mounted () {
    this.getQuestions()
  }
}

</script>
