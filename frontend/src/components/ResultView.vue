<script setup>
defineProps({
  result: String
})

defineEmits(['restart'])
</script>

<template>
  <div class="result-view">
    <h2>Ваши рекомендации:</h2>
    <div class="ai-result" v-html="result.replace(/\n/g, '<br>')"></div>
    <button @click="$emit('restart')">Начать заново</button>
  </div>
</template>

<style scoped>
.ai-result {
  text-align: left;
  margin: 1rem 0;
  padding: 1rem;
  background: #f5f5f5;
  border-radius: 8px;
}
</style>