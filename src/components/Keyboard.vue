<script setup>
import Key from './Key.vue'
const props = defineProps(['keyColors'])
const emit = defineEmits(['key-click'])

function keyClick(n) {
    if (n === 'Back') {
        n = 'Backspace'
    }
    emit('key-click', n)
}

const row1 = 'QWERTYUIOP'.split('')
const row2 = 'ASDFGHJKL'.split('')
const row3 = 'ZXCVBNM'.split('')


</script>

<template>
<div class="keyboard">
    <div class="key-row">
        <Key v-for="letter in row1" :key="letter" :letter="letter" :color="props.keyColors[letter]" @key-click="keyClick"/>
    </div>
    <div class="key-row">
        <Key v-for="letter in row2" :key="letter" :letter="letter" :color="props.keyColors[letter]" @key-click="keyClick"/>
    </div>
    <div class="key-row">
        <Key :letter="'Enter'" @key-click="keyClick" id="enter"/>
        <Key v-for="letter in row3" :key="letter" :letter="letter" :color="props.keyColors[letter]" @key-click="keyClick"/>
        <Key :letter="'Back'" @key-click="keyClick" id="back"/>
    </div>
</div>
    
</template>