<script setup>
import { ref } from 'vue'

const props = defineProps(['word'])
</script>


<template>
    <p>
        {{props.word}}
    </p>
</template>