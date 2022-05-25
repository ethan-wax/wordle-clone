<script setup>
import { onMounted, onUnmounted, ref } from 'vue'
import Cell from './Cell.vue'

const goalWord = ''

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


let row_index = 0
let col_index = 0


function evalEntry() {
    for (var i = 0; i < 5; i++) {
        var letter = rows.value[row_index][i].letter
        var pos = goalWord.indexOf(letter)
        if (pos !== -1) {
            if (pos === i) {
                rows.value[row_index][i].color = 'green'
            } else {
                rows.value[row_index][i].color = 'yellow'
            }
        }
    }
}


function keyPress(event) {
    let key = event.key
    if (key.length === 1 && key.match(/[a-z]/i)) {
        if (col_index < 5) {
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
}

onMounted(() => {
    window.addEventListener('keyup', keyPress)
})

onUnmounted(() => {
    window.removeEventListener('keyup', keyPress)
})

</script>

<template>
<div class="container-column">
    <template v-for="row, index in rows" :key="'row' + index">
        <div class="container-row">
            <template v-for="letter, pos in row" :key="'col' + pos">
                <Cell :letter="letter.letter" :color="letter.color" />
            </template>
        </div>
    </template>
</div>
</template>