<script setup>
const props = defineProps(['letter', 'color'])
</script>

<template>
    <h1 class="key" :class="props.color" @click="$emit('key-click', props.letter)">{{ props.letter }}</h1>
</template>