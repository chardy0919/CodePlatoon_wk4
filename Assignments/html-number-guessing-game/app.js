console.log("HELLO VICTOR PLATOON!")
// Your function(s) should go here that will interact with the webpage or DOM
 let answer = Math.floor(Math.random()*100)
 let count = 0
const guessNumber = () =>{
    let input = Number(document.getElementById("input-number"));
    let output = document.getElementById("output-display");
    
    if (input < 0 || input > 99){
        output.innerHTML = "Invalid Guess"
        count++
    } else if (input < answer){
        output.innerHTML = "Too low!"
        count++
    } else if (input > answer){
        output.innerHTML = "Too high!"
        count++
    } else if (input == answer && count === 1){
        output.innerHTML = "First Try!"
    } else {
        output.innerHTML = 'Correct!'
    }
    console.log(answer,input)
}
message.innerHTML = ""
    if (isNaN(guessInput.value) || guessInput.value == ""){
        const text = document.createElement('p');
        text.innerHTML = "Not a number!"
        message.append(text)
    }
    else {
        const text = document.createElement('p');

        guess = Number(guessInput.value)
        console.log(guess)
        console.log(num)
        if (guess == num){
            text.innerHTML = "Correct!"
        }else if (guess > num){
            text.innerHTML = "Guess is High!"
        }else if (guess < num){
            text.innerHTML = "Guess is Low!"
        }
        message.append(text)
    }