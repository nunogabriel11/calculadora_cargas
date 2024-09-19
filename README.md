# Calculadora de Volume e Peso Taxável

Este projeto focou-se no desenvolvimento de uma aplicação executável simples e didática com o propósito de obter o volume como também o peso taxável em casos de mercadorias complexas, por exemplo, 3 paletes europeias, 32 caixas pequenas e 7 rolos. 
O primeiro bloco de execução da aplicação centra-se em inserir, por parte do utilizador, o número de cargas distintas existentes como também o fator de dimensionalidade a considerar para o cálculo do peso taxável.

<p align="center">
  <img src="https://github.com/nunogabriel11/calculadora_cargas/blob/main/imgs/ui.png?raw=true" width="200" />
</p>

*Figura 1: Imagem ilustrativa do bloco principal da aplicação.*

Após serem introduzidas as descrições anteriores, seleciona-se o botão “iniciar cálculo” na qual irá abrir tantas novas de descrição de carga tanto o número inserido em “Número de cargas”. Cada uma dessas janelas questiona o utilizador acerca da descrição da carga sobre esta ser paletizada ou não paletizada. e, posteriormente a sua descrição:
1. Caso a mercadoria seja paletizada, irá abrir uma nova janela correspondente á inserção da descrição da mercadoria (comprimento, largura, altura e número de paletes)
2. Caso a mercadoria seja não paletizada, o utilizador terá de selecionar uma opção entre “caixas” ou “rolos”
   a. No caso de a carga ser constituída por caixas, irá ser pedido ao utilizador para introduzir a descrição da carga (comprimento, largura, altura e número de caixas)
   b. Já no caso de a carga ser constituída por rolos, o utilizador terá, novamente, inserir a descrição da carga para rolos (diâmetro, altura e número de rolos).

Finalizado esse processo, irá ser retornado, na janela principal, o volume total associado a todas as mercadorias distintas (ou não) como também o peso taxável total referente ao volume obtido e ao fator de dimensionamento para peso taxável introduzido (Fator CBM).

O seguinte vídeo representa o funcionamento e obtenção dos resultados por parte da aplicação para 3 cargas diferentes entre si:

- Carga 1: 3 paletes com dimensões de 1,2 x 0,8 x 0,6 (m)
- Carga 2: 27 caixas com dimensões de 0,5 x 0,4 x 0,4 (m)
- Carga 3: 5 tubos com 0,6 (m) de diâmetro e 1,2 (m) de altura

<p align="center">
  <img src="https://github.com/nunogabriel11/calculadora_cargas/blob/main/imgs/demo.GIF?raw=true" width="600" />
</p>
