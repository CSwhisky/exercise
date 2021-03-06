const notes = [{
    title: 'My next trip',
    body: 'I;d like to go to Spain'
}, {
    title: 'Habbits to work on',
    body: 'Exercise. Eating a bit better.'
}, {
    title: 'Office modification',
    body: 'Get a new seat'
}]

// const findNote = function (notes, noteTitle) {
//     const index = notes.findIndex(function (note, index) {
//         return note.title.toLowerCase() === noteTitle.toLowerCase()
//     })
//     return notes[index]
// }

const sortNotes = function (notes) {
    notes.sort(function (a,b) {
        if (a.title.toLowerCase() < b.title.toLowerCase()) {
            return -1
        } else if (b.title.toLowerCase() < a.title.toLocaleLowerCase()) {
            return 1
        } else {
            return 0
        }
    })
}

const findNote = function (notes, noteTitle) {
    return notes.find(function (note) {
        return note.title.toLowerCase() === noteTitle.toLowerCase()
    })
}

const findNotes = function(notes, query) {
    return notes.filter(function (note){
        const isTitleMatch = note.title.toLowerCase().includes(query.toLocaleLowerCase());
        const isBodyMatch = note.body.toLocaleLowerCase().includes(query.toLocaleLowerCase());
        return isTitleMatch || isBodyMatch
    })
}

console.log(filterNotes)

const note = findNote(notes, 'My next trip')
console.log(note)

// console.log(notes.pop())
// notes.push("my new note!")

// console.log(notes.shift())
// notes.unshift('my first note')

// notes.splice(1,0,"aye!")
// console.log(notes)

// notes.forEach(function (item, index) {
//     console.log(item)
// })

// for (let count = 0; count <= 2; count = count +1) {
//     console.log(count)
// }

// for (let count = notes.length - 1; count >= 0; count--) {
//     console.log(notes[count])
// }

// console.log(notes.indexOf('Note 1'))