from flask import Flask, jsonify, request

app= Flask(__name__)

jogos=[
    {
        'id':1,
        'titulo':'counter-strike 2',
        'estudio': 'Valve'
    },
    {
        'id':2,
        'titulo':'Valorant',
        'estudio': 'Riot Games'
    },
    {
        'id':3,
        'titulo':'World of Warcraft',
        'estudio': 'Blizzard'
    },
]

#consultar --> funçao para consultar toda a lista
@app.route('/jogos',methods=['GET'])
def obter_jogos():
    return jsonify(jogos)

#consultar por (id) --> funçao para consultar por id ,utilizando ciclo repetiçao para verificar toda a lista ate dar match
#adicionado <int:id> a route para especificar o que é esperado passar para a funçao 
@app.route('/jogos/<int:id>',methods=['GET'])
def obter_jogo_por_id(id):
   for jogo in jogos:
       if jogo.get('id')==id:
           return jsonify(jogo) 
       
#editar --> obter informaçao do user pelo request.get_djson e guardar na variavel 
#ciclo for para correr indice/jogo e verificar match com id passado como argumento
#apos match , update para alterar pelo index a nova informaçao
#retorna a informaçao alterada atravez do indice
@app.route('/jogos/<int:id>',methods=['PUT'])
def editar_jogo_por_id(id):
    jogo_alterado=request.get_json()
    for indice,jogo in enumerate(jogos):
        if jogo.get('id')==id:
            jogos[indice].update(jogo_alterado)
            return jsonify(jogos[indice])

#criar utlizaçao do metodo .append para adicionar a lista , retorna todos jogos no fim 
@app.route('/jogos',methods=['POST'])
def incluir_novo_jogo():
    novo_jogo=request.get_json()
    jogos.append(novo_jogo)

    return jsonify(jogos)

#excluir  enumerar todos jogos por indice , quando o for encontra o id igual ao id passado por parametro, o delete é aplicado ao indice 
@app.route('/jogos/<int:id>',methods=['DELETE'])
def excluir_jogo(id):
    for indice,jogo in enumerate(jogos):
        if jogo.get('id')==id:
            del jogos[indice]

    return jsonify(jogos)


app.run(port=5000,host='localhost',debug=True)
