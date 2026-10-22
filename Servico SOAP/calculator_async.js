const soap = require('soap');

const url = 'http://www.dneonline.com/calculator.asmx?WSDL';

const args = {
  intA: process.argv[2],
  intB: process.argv[3]
};

const operation = process.argv[4];

(async () => {
  try {
    const client = await soap.createClientAsync(url);

    switch (operation) {
      case 'adicionar':
        const addResult = await client.AddAsync(args);
        console.log('Resultado:', addResult[0].AddResult);
        break;
      case 'subtrair':
        const subtractResult = await client.SubtractAsync(args);
        console.log('Resultado:', subtractResult[0].SubtractResult);
        break;
      case 'multiplicar':
        const multiplyResult = await client.MultiplyAsync(args);
        console.log('Resultado:', multiplyResult[0].MultiplyResult);
        break;
      case 'dividir':
        const divideResult = await client.DivideAsync(args);
        console.log('Resultado:', divideResult[0].DivideResult);
        break;
      default:
        console.error('Operacao invalida!! somente: "adicionar", "subtrair", "multiplicar", "dividir"');
    }
  } catch (err) {
    console.error('Erro na operação:', err);
  }
})();