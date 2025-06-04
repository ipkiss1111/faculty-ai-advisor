<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const questions = ref([])
const currentStep = ref(0)
const answers = ref([])

// Загружаем вопросы с бэкенда
onMounted(async () => {
  const response = await axios.get('http://localhost:5000/api/questions')
  questions.value = response.data
})

const nextQuestion = (answer) => {
  answers.value.push(answer)
  if (currentStep.value < questions.value.length - 1) {
    currentStep.value++
  } else {
    submitAnswers()
  }
}

const submitAnswers = async () => {
  const response = await axios.post('http://localhost:5000/api/analyze', {
    answers: answers.value
  })
  emit('submit', response.data.result)
}

defineEmits(['submit'])
</script>

<template>
  <div class="question-form">
    <h2>{{ questions[currentStep]?.text }}</h2>
    <div class="options">
      <button
        v-for="(option, idx) in questions[currentStep]?.options"
        :key="idx"
        @click="nextQuestion(option)"
      >
        {{ option }}
      </button>
    </div>
    <div class="progress">
      Вопрос {{ currentStep + 1 }} из {{ questions.length }}
    </div>
  </div>
</template>