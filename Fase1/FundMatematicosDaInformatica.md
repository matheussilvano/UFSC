# Fundamentos Matemáticos da Informática
## Professor: Arthur Ronald de Vallauris Buchsbaum

### Frase
1. Unidade linguística com sentido completo, que contém pelo menos um verbo principal, sendo delimitada na escrita por letra maiúscula no início, e, no fim por um sinal de pontuação. (ex: Arthur é professor, mas ele não é inteligente, porém ele tem algumas habilidades; Florianópolis é uma cidade pequena)
2. É uma declaração a respeito de objetos (Ex: Rio de Janeiro é maior que Florianópolis)

### Fórmula
- É uma frase em linguagem matemática -> Dois mais três é igual a cinco (2+3=5)

Considere que: 
1. todo homem é mortal
2. Sócrates é homem
Logo, sócrates é mortal

Reescrita moderna deste exemplo: Todo homem é mortal, Sócrates é homem ⊢<sub>LC<sub> Sócrates é mortal } Sequente

⊢ = barra de Frege
LC = Lógica clássica

### Forma geral de um Sequente
Coleção de frases / fórmulas ⊢<sub>LC</sub> conclusão

### Níveis dos sistemas lógicos
1. Nível proposicional -> Relativo a proposição (frase, sentença), é o nível mais elementar, estuda-se as seguintes ideias:
  - Não
  - E
  - Ou
  - Se
  - Então
2. Lógica quantificacional -> Relativo a quantificadores
  - Para todo
  - Existe
3. Lógica equacional ou igualitária -> Relativo à igualdade
  - =
4. Lógica descritiva -> Relativo a descrições
  - tau (artigo definido)
  - []
5. Teoria dos conjuntos -> Relativo a pertinência
  - E (pentence à)

Tipos de lógica: Clássica (mais utilizada), paraconsistente, paracompletas

### Lógica proposicional
#### Negação (¬)
- Um leão não é manso -> Não é verdade que um leão é manso -> ¬M
  - ¬ Não é verdade que
  - M O leão é manso
- ¬P } é uma negação, onde P é a fórmula negada
- Valores veritativos: É o grau de veracidade de uma fórmula, na lógica clássica existem apenas verdadeiro(v) ou falso(f)
- No caso do exemplo do leão, ¬M é v, enquanto M é f
- O Bangladesh não é um país pobre -> ¬P (onde P é verdadeiro e ¬P é falso)
- Tabela veritativa da negação<br>

|  P | ¬P |
| ------------- | ------------- |
| v  | f |
| f  | v  |

#### Adjunção (∧)
- ∧ pode ser lido como "e"
- Ex: O tigre e o leão são carnívoros -> O tigre é carnívoro e o leão é carnívoro -> T ∧ L } Adjunção
  - T = O tigre é carnívoro
  - L = o leão é carnívoro
  - ^ = e
  - T e L são adjuntores da adjunção
  - T é verdadeiro e L é verdadeiro, logo a adjunção é verdadeira (v)
- Ex2: O tigre e o coelho são carnívoros -> O tigre é carnívoro e o coelho é carnívoro -> T ^ C
 - O tigre é carnívoro é verdadeiro, mas o coelho é carnívoro é falso, logo toda a adjunção é falsa
- Tabela veritativa da adjunção<br>

|  P | Q | P^Q |
| ------------- | ------------- | ------------- |
| v | v | v |
| f | v | f |
| v | f | f |
| f | f | f |


  
  
