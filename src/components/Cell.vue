<script setup>
const props = defineProps(['letter', 'color'])
</script>

<template>
    <h1 class="box" :class="props.color">{{ props.letter }}</h1>
</template>