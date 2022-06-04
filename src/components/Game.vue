<script setup>
import { onMounted, onUnmounted, ref } from 'vue'
import Cell from './Cell.vue'
import words from '../assets/words'
import Keyboard from './Keyboard.vue';

const NUM_ROWS = 6
const NUM_COLS = 5

const rows = ref([
    [
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' }
    ],
    [
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' }
    ],
    [
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' }
    ],
    [
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' }
    ],
    [
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' }
    ],
    [
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' },
        { letter: '', color: '' }
    ]
])

function dateIndex() {
    var date = new Date()
    var i =  (date.getDate() * 100) + (date.getMonth() * 90) + date.getFullYear()
    return i % words.length
}


const goalWord = words[dateIndex()].toUpperCase()


let row_index = 0
let col_index = 0

const over = ref(false)
const win = ref(false)

const keyColors = ref({})

function evalEntry() {
    var word = new Array(5)
    var goal = new Array(5)
    for (var i = 0; i < NUM_COLS; i++) {
        word[i] = rows.value[row_index][i].letter
        goal[i] = goalWord[i]
    }
    // First pass: check for greens and replace with an empty to get rid of doubles
    var numGreens = 0
    for (var i = 0; i < NUM_COLS; i++) {
        if (word[i] === goalWord[i]) {
            rows.value[row_index][i].color = 'green'
            keyColors.value[word[i]] = 'green'
            goal[i] = ''
            numGreens++
        }
    }
    if (numGreens === 5) {
        over.value = true
        win.value = true
    }
    // Second pass: check for yellows
    for (var i = 0; i < NUM_COLS; i++) {
        if (rows.value[row_index][i].color !== 'green') {
            var letter = word[i]
            for (var j = 0; j < NUM_COLS; j++) {
                if (letter === goal[j]) {
                    rows.value[row_index][i].color = 'yellow'
                    if (keyColors.value[word[i]] !== 'green') {
                        keyColors.value[word[i]] = 'yellow'
                    }
                    goal[j] = ''
                    break
                }
            }
        }
    }
    // Third pass: set keyboard color to black for misses
    for (var i = 0; i < NUM_COLS; i++) {
        if (rows.value[row_index][i].color !== 'green' && rows.value[row_index][i].color !== 'yellow') {
            keyColors.value[word[i]] = 'black'
        }
    }
}


function keyPress(event) {
    let key = event.key
    if (key.length === 1 && key.match(/[a-z]/i)) {
        if (col_index < 5 && row_index < 6 && !over.value) {
            rows.value[row_index][col_index].letter = key.toUpperCase()
            col_index++
        }
    } else if (key === 'Enter') {
        if (col_index === 5) {
            evalEntry()
            col_index = 0
            row_index++
        } 
    } else if (key === 'Backspace') {
        if (col_index > 0) {
            col_index--
            rows.value[row_index][col_index].letter = ''
        }
    }
    if (row_index === 6) {
        over.value = true
    }
}

onMounted(() => {
    window.addEventListener('keyup', keyPress)
})

onUnmounted(() => {
    window.removeEventListener('keyup', keyPress)
})

function keyClick(n) {
    keyPress({key: n})
}
</script>

<template>
<h1 v-show="over">Today's word was: {{ goalWord }}</h1>
<div class="container-column">
    <template v-for="row, index in rows" :key="'row' + index">
        <div class="container-row">
            <template v-for="letter, pos in row" :key="'col' + pos">
                <Cell :letter="letter.letter" :color="letter.color" />
            </template>
        </div>
    </template>
</div>
<Keyboard :key-colors="keyColors" @key-click="keyClick"/>
</template>