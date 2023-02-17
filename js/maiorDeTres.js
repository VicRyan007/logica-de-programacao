const prompt = require ("prompt-sync")({sigint: true})


var n1 = prompt("Digite o primeiro número: ")
var n2 = prompt("Digite o segundo número: ")
var n3 = prompt("Digite o terceiro número: ")

    var maior,meio,menor

    if(n1>n2 && n1>n3){
        maior = n1
    } else if(n1<n2 && n1<n3) {
        menor = n1
    } else if (n2>n1 && n2>n3){
        maior = n2
    } else if (n2<n1 && n2<n3){
        menor = n2
    } else if (n3>n1 && n3>n2){
        maior = n3
    } else if (n3<n1 && n3<n2){
        menor = n3
    } else if (n1>n2 && n1<n3){
        meio = n1
    } else if (n1>n2 && n2>n3){
        meio = n2
    } else if (n1>n3 && n3>n2){
        meio = n3
    }

    console.log("Maior: "+maior)
    console.log("Meio: "+meio)
    console.log("Menor: "+menor)