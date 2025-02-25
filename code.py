from flask import Flask, jsonify, request
import sqlite3

app = Flask('app')

class Envie_Receba():
    def __init__(self):
        self.excel_file = 'revisao.xlsx'
        
        self.conexao = sqlite3.connect('palavras_bank.db')  
        self.comando = self.conexao.cursor()


    def homepage(self):
        return 'A API está no ar'
        
    def busca_palavra(self, palavra):
        self.comando.execute(f"SELECT * FROM tb_palavras_e_silabas WHERE palavras = '{palavra}' LIMIT 1")
        resultado = self.comando.fetchone()
        if resultado:
            return {'palavra': resultado[1], 'segmentacao': resultado[2]}
        else:
            return {'mensagem': 'Palavra não encontrada, verifique se a palavra está escrita corretamente'}

    def pe_de_palavra(self):
        data = request.get_json()
        palavra = data['palavra']

        if len(palavra) < 2:
            return jsonify({'erro': 'Palavra deve ter pelo menos 2 caracteres'})


        resposta = {'mensagem': 'em analise, obrigado pela contribuição', 'palavra': palavra}
        with open('revisao.txt', 'a') as arquivo:

            arquivo.write(f"{resposta['palavra']}\t{resposta['mensagem']}\n")

    
        return jsonify(resposta)


envie_receba = Envie_Receba()


if 'app' == '__main__':
    app.run()

@app.route('/')
def homepage():
  return envie_receba.homepage()

@app.route('/segmentacao', methods=['GET'])
def manda_me_palavra():
    data = request.get_json()
    palavra = data['palavra']

    envie_receba = Envie_Receba()

    resultado = Envie_Receba().busca_palavra(palavra)

    return jsonify(resultado)

@app.route('/add_palavra', methods=['POST'])
def pe_de_palavra():
  return envie_receba.pe_de_palavra()

app.run(host='0.0.0.0', port=8080)
