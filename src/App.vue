<script setup>
import { ref } from 'vue'

const header = ref("Wordle Clone")

const log = (l) => {
  console.log("l")
}


const state = ref({ count: 0 })

function increment() {
  state.value.count++
}

const row1 = ref([
  {id: 1, letter: 'P'},
  {id: 2, letter: 'E'},
  {id: 3, letter: 'N'},
  {id: 4, letter: 'I'},
  {id: 5, letter: 'S'}
])

const emptyRow = ref([
  {id: 1, letter: ''},
  {id: 2, letter: ''},
  {id: 3, letter: ''},
  {id: 4, letter: ''},
  {id: 5, letter: ''}
])

const row2 = emptyRow
const row3 = emptyRow
const row4 = emptyRow
const row5 = emptyRow
const row6 = emptyRow

let rows = [
  row1,
  row2,
  row3,
  row4,
  row5,
  row6
]

let letterIndex = 0
let rowIndex = 0

const addLetter = (l)=>{
  if (letterIndex < 5) {
    rows[rowIndex].value[letterIndex].letter = l
    letterIndex++
  } 
}
</script>

<template>
  <header>
    <h1>{{header}}</h1>
  </header>
  <main>
    <div class="container-column">
      <div class="container-row">
        <div class="box" v-for="({id, letter}, ) in row1" :key="id">
          <p @click="key">{{letter}}</p>
        </div>
      </div>
      <div class="container-row">
        <div class="box" v-for="({id, letter}, ) in row2" :key="id">
          <p>{{letter}}</p>
        </div>
      </div>
      <div class="container-row">
        <div class="box" v-for="({id, letter}, ) in row3" :key="id">
          <p>{{letter}}</p>
        </div>
      </div>
      <div class="container-row">
        <div class="box" v-for="({id, letter}, ) in row4" :key="id">
          <p>{{letter}}</p>
        </div>
      </div>
      <div class="container-row">
        <div class="box" v-for="({id, letter}, ) in row5" :key="id">
          <p>{{letter}}</p>
        </div>
      </div>
      <div class="container-row">
        <div class="box" v-for="({id, letter}, ) in row6" :key="id">
          <p>{{letter}}</p>
        </div>
      </div>
    </div>
  </main>
</template>

<style>
@import './assets/base.css';
</style>
