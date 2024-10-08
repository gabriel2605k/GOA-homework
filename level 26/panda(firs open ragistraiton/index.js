
let compiuterScore = 0
let userScore = 0
let game = 0
//      rock button
function rock() {
    let rock = Math.random()
    let compiuter =""
    let result =""
    const user = "rock👊"

    // rock, paper, scissors
    if (rock >= 0 && rock <1/3){
        compiuter = "rock👊"
    }
    else if (rock >= 1/3 && rock < 2/3){
        compiuter = "paper✋"
    }
    else if (rock >= 2/3 && rock <1){
        compiuter = "scissors✌️"
    }

    // win, loss, tie
    if (compiuter === 'rock👊'){
        result = "TIE";
        compiuterScore = compiuterScore + 0;
        userScore = userScore + 0
    }
    else if (compiuter === 'paper✋'){
        result = 'You LOST';
        compiuterScore = compiuterScore + 2
        userScore = userScore -1
    }
    else if (compiuter === 'scissors✌️'){
        result = 'You WIN'
        userScore = userScore + 2
        compiuterScore = compiuterScore - 1
    }
    // result
    document.getElementById("compiuter").innerHTML = compiuter;
    document.getElementById('Result').innerHTML = result;
    document.getElementById('user').innerHTML = user;
    // score
    document.getElementById('userScore').innerHTML = userScore
    document.getElementById('compiuterScore').innerHTML = compiuterScore
    document.getElementById("Game").innerHTML = 
    game = game+1
    if (game == 6){
        location.reload()
        if (userScore == compiuterScore){
            alert('თამაში დამთავრდა, ფრეა')
        } else if (userScore > compiuterScore){
            alert('თამაში დამთავრდა, მოიგე')
        } else if (userScore < compiuterScore){
            alert('თამაში დამთავრდა, წააგე')
        }
    }
}

//      paper button
function paper() {
    let paper = Math.random()
    let compiuter =""
    let result =""
    const user = "paper✋"

    // rock, paper, scissors
    if (paper >= 0 && paper <1/3){
        compiuter = "rock👊"
    }
    else if (paper >= 1/3 && paper < 2/3){
        compiuter = "paper✋"
    }
    else if (paper >= 2/3 && paper <1){
        compiuter = "scissors✌️"
    }

    // Loss, win, tie
    if (compiuter === "paper✋"){
        result = 'TIE';
        compiuterScore = compiuterScore + 0;
        userScore = userScore + 0
    }
    else if (compiuter === "scissors✌️"){
        result = 'You LOST';
        compiuterScore = compiuterScore + 2
        userScore = userScore -1
    }
    else if (compiuter === 'rock👊'){
        result = 'You WIN';
        userScore = userScore + 2
        compiuterScore = compiuterScore - 1
    }
    // result
    document.getElementById("Result").innerHTML = result;
    document.getElementById("compiuter").innerHTML = compiuter;
    document.getElementById('user').innerHTML = user 

    // scores
    document.getElementById('userScore').innerHTML = userScore
    document.getElementById('compiuterScore').innerHTML = compiuterScore
    document.getElementById("Game").innerHTML = 
    game = game+1
    if (game == 6){
        location.reload()
        if (userScore == compiuterScore){
            alert('თამაში დამთავრდა, ფრეა')
        } else if (userScore > compiuterScore){
            alert('თამაში დამთავრდა, მოიგე')
        } else if (userScore < compiuterScore){
            alert('თამაში დამთავრდა, წააგე')
        }
    }
}
//      scissors button
function scissors() {
    let scissors = Math.random()
    let compiuter =""
    let result =""
    const user = "scissors✌️"

    // rock, paper, scissors
    if (scissors >= 0 && scissors <1/3){
        compiuter = "rock👊"
    }
    else if (scissors >= 1/3 && scissors < 2/3){
        compiuter = "paper✋"
    }
    else if (scissors >= 2/3 && scissors <1){
        compiuter = "scissors✌️"
    }

    // win, loss, tie
    if (compiuter === "scissors✌️"){
        result = "TIE";
        compiuterScore = compiuterScore + 0;
        userScore = userScore + 0
    }
    else if (compiuter === 'paper✋'){
        result = "You WIN";
        userScore = userScore + 2
        compiuterScore = compiuterScore -1
    }
    else if (compiuter === 'rock👊'){
        result = "You LOST";
        compiuterScore = compiuterScore + 2
        userScore = userScore -1
    }

    // result
    document.getElementById("compiuter").innerHTML = compiuter;
    document.getElementById("Result").innerHTML = result;
    document.getElementById('user').innerHTML = user;

    // scores
    document.getElementById('userScore').innerHTML = userScore;
    document.getElementById('compiuterScore').innerHTML = compiuterScore
    document.getElementById("Game").innerHTML = 
    game = game+1
    if (game == 6){
        location.reload()
        if (userScore == compiuterScore){
            alert('თამაში დამთავრდა, ფრეა')
        } else if (userScore > compiuterScore){
            alert('თამაში დამთავრდა, მოიგე')
        } else if (userScore < compiuterScore){
            alert('თამაში დამთავრდა, წააგე')
        }
    }
}

