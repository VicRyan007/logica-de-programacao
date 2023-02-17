const prompt = require ("prompt-sync")({sigint: true})
var n1 = prompt("Digite a nota 1: ")
var n2 = prompt("Digite a nota 2: ")
var media = (n1+n2)/2
if(media >= 7 && media<=9.9 ){
    console.log("APROVADO")
} else if (media == 10) {
    console.log("APROVADO COM DISTINÇÃO")
} else {
    console.log("REPROVADO")
}
