# Separacao_silabica
API de separação silábica.

Um pequeno projeto de uma API que tem +300K de palavras da língua portuguesa brasileira. 
Você pode requisitar qualquer palavra do português brasileiro e sua separação silábica no formato JSON.
Se a palavra que você estiver procurando não estiver lá, você pode envia-la, eu analisarei e atualizarei o banco de dados futuramente.


A little project about an API that have +300K words from brazilian portuguese. 
You can request any word about the brazilian portuguese and with its syllable separation in JSON format.
If the word that you're looking for isn't there, you can post it, I will analyze and update the data base soon.

# Como usar? How to use?

De antemão, por ser meu primeiro projeto creio que não ficará ativa por muito tempo e/ou será essa mesma URL, porém, deixarei o status de atividade aqui: OFFLINE.

URL = https://5d9634fb-fd87-4d1b-a713-a235ed7d47b6-00-31tr3f3xz013o.worf.replit.dev/

Para puxar a separação silábica de alguma palavra, basta você acrescentar "segmentacao" na URL e usar o metodo GET. Exemplo em python, supondo que a URL esteja salva numa variavel "URL":

palavra = {'palavra': 'abacate'}

segmentacao = requests.get(url + 'segmentacao', json=palavra)

print(segmentacao.json())

# E se não houver a palavra?

Não se preocupe, irei atualizar o banco de dados periodicamente. Basta acrescentar "add_palavra" na URL e usar o metodo POST.
