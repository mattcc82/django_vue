let app = new Vue({
  el: '#app',
  data: {
    tasks: [],
    taskInput: ''
  },
  methods: {
    addTask () {
      this.tasks.push(this.taskInput)
      this.taskInput = ''
    },
    removeTask (index) {
      this.tasks.splice(index, 1)
    }
  }
})
