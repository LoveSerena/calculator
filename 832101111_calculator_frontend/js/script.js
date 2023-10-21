let display = document.getElementById('display');
let ansValue = 0;

function appendToDisplay(value) {
  display.value += value;
}

function clearDisplay() {
  display.value = '';
}

function calculateResult() {
  try {
    let expression = display.value;

    // Replace trigonometric functions with JavaScript functions
    expression = expression.replace(/sin\(/g, 'Math.sin(');
    expression = expression.replace(/cos\(/g, 'Math.cos(');
    expression = expression.replace(/tan\(/g, 'Math.tan(');


    let result = eval(expression);


    if (!isFinite(result)) {
      display.value = 'Error';
    } else {
      ansValue = result; 
      display.value = result;
    }
  } catch (error) {
    display.value = 'Error';
  }
}

function calculateSquareRoot() {
  display.value = Math.sqrt(eval(display.value));
}

function calculateLog() {
  display.value = Math.log10(eval(display.value));
}

function calculateScientificNotation() {
  display.value = eval(display.value.toExponential());
}

function calculateFactorial() {
  let num = eval(display.value);
  let result = 1;
  for (let i = 2; i <= num; i++) {
    result *= i;
  }
  ansValue = result; 
  display.value = result;
}

function useAns() {
  display.value += ansValue;
}

function addLeftBracket() {
  display.value += '(';
}

function addRightBracket() {
  display.value += ')';
}


fetch('/history', {
  method: 'GET',
})
  .then(response => response.json())
  .then(data => {
    // 处理获取的历史记录
    console.log(data);
  })
  .catch(error => {
    console.error('Error:', error);
  });
