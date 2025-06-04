<script setup>
import { ref } from 'vue'
import QuestionForm from './components/QuestionForm.vue'
import ResultView from './components/ResultView.vue'

const currentView = ref('form') // 'form' или 'result'
const aiResult = ref('')

const handleResult = (result) => {
  aiResult.value = result
  currentView.value = 'result'
}
</script>

<template>
  <div class="app">
    <header>
      <h1>AI Faculty Advisor</h1>
    </header>
    <main>
      <QuestionForm 
        v-if="currentView === 'form'" 
        @submit="handleResult" 
      />
      <ResultView 
        v-else 
        :result="aiResult" 
        @restart="currentView = 'form'" 
      />
    </main>
  </div>
</template>

<style scoped>
.app {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}
</style>