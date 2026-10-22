const soap = require('soap');
const url = 'http://www.dneonline.com/calculator.asmx?WSDL';
const args = { intA: process.argv[2], intB: process.argv[3]};
const operacao = process.argv[4];

soap.createClient(url, (err, client) => {
    if (err) {
      console.error('Erro ao criar o cliente', err);
      return;   
    }

    switch(operacao){
        case 'adicionar':
            client.Add(args, (err, result) => {
                if (err) {
                    console.error('Erro na operacao:', err);
                    return;
                }
                console.log('Resultado:', result.AddResult);
            });
            break;
        case 'subtrair':
            client.Subtract(args, (err, result) => {
                if (err) {
                    console.error('Erro na operacao:', err);
                    return;
                }
                console.log('Resultado:', result.SubtractResult);
            });
            break;
        case 'multiplicar':
            client.Multiply(args, (err, result) => {
                if (err) {
                    console.error('Erro ao realzar a operacao', err);
                    return;
                }
                console.log('Resultado:', result.MultiplyResult);
            });
            break;
        case 'dividir':
            client.Divide(args, (err, result) => {
                if (err) {
                    console.error('Erro na operacao:', err);
                    return;
                }
                console.log('Resultado:', result.DivideResult);
            });
            break;
        default:
            console.error('Operacao invalida!! somente: "adicionar", "subtrair", "multiplicar", "dividir"');
    }
});