// lógica simples para realizar operações entre dois números

function getNumber(id) {
  return parseFloat(document.getElementById(id).value) || 0;
}

function calculate(op) {
  const a = getNumber('num1');
  const b = getNumber('num2');
  let result;
  switch (op) {
    case '+': result = a + b; break;
    case '-': result = a - b; break;
    case '*': result = a * b; break;
    case '/':
      result = b !== 0 ? a / b : 'Erro (div/0)';
      break;
    default: result = 'Operador inválido';
  }
  document.getElementById('result').textContent = result;
}

document.getElementById('add').addEventListener('click', () => calculate('+'));
document.getElementById('sub').addEventListener('click', () => calculate('-'));
document.getElementById('mul').addEventListener('click', () => calculate('*'));
document.getElementById('div').addEventListener('click', () => calculate('/'));
