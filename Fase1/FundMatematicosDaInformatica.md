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

- Ou seja, uma adjunção é verdadeira se, e somente se ambos os ajuntores forem verdadeiros.
- Val(P^Q) = v sss Val(P)=Val(Q)=v

#### Disjunção (v)
- Pode ser lido como "ou"
- P v Q } Disjunção
- P e q São disjuntores
- Ex: Pelo menos um dos países Rússia ou Paraguai é bem grande -> A Rússia é bem grande ou o Paraguai é bem grande -> R v P
  - R é verdadeiro, enquanto P é falso. Logo, toda a disjunção é verdadeira
- Ex2: Pelo menos um dos países Rússia ou Canadá é bem grande -> A Rússia é bem grande ou o Paraguai é bem grande -> R v C
  - Tanto R quanto C são verdadeiros, logo, a disjunção é verdadeira
- Tabela veritativa da disjunção:

  |  P | Q | P^Q |
  | ------------- | ------------- | ------------- |
  | v | v | v |
  | f | v | v |
  | v | f | v |
  | f | f | f |

- Ou seja, uma disjunção é verdadeira se, e somente se pelo menos um de seus disjuntores é verdadeiro.
- Val(PvQ) = v sss Val(P) ou Val(Q)=v

#### Implicação (→)
- Leituras:
  - Se P, então Q
  - P implica em Q
  - Q, se P
  - P é suficiente para Q
  - Q é necessário para P
- Ex: Se houver um terremoto numa área populosa, então haverá muitas mortes -> T → M (implicação)
  - T = houver um terremoto numa área populosa
  - M = haverá muitas mortes
  - Se = Antecedente
  - Então = Consequente

- Tabela veritativa da disjunção:

  |  P | Q | P→Q |
  | ------------- | ------------- | ------------- |
  | v | v | v |
  | f | v | v |
  | v | f | f |
  | f | f | v |

- Implicação natural vs IMplicação material:
  - Natural: É das línguas realmente faladas.
  - Material: É a implicação matemática da lógica clássica

- Logo, uma implicação é falsa se, e somente se, seu antecedente for verdadeiro e seu consequente for falso
- Val(P→Q)=f sss Val(P)=v e Valor(Q)=f

#### Verum (T)
- Representa frases sempre verdadeiras em um dado contexto
- Ex: 2+3=5 } T
- Ex2: Arthur é professor.
- Tabela veritativa do Verum:

  |  T |
  | ------------- |
  | v | 

#### Falsum (⊥)
- Representa frases sempre falsas em um dado contexto
- Ex: 2+3=7 } ⊥
- Ex2: Arthur é estivador.
- Tabela veritativa do Falsum:

  |  ⊥ |
  | ------------- |
  | f |

#### Definições (Def)
Podem ser:
- Abreviaturas
- Reescritos
- ⇆

#### Equivalência (<->)
- P <-> Q ⇆ (P->Q) ^ (Q->P)
- P <-> Q é a equivalência, onde P e Q são membros
- Leituras:
  - P equivale à Q
  - P é equivalente a Q
  - P se, e somente se, Q
  - P é necessário o suficiente para Q
- Se P não equivale a Q, é necessário usar parenteses: ¬(P->Q), pois se usar ¬P -> Q, eu afirmo que não P equivale a Q

##### Implicação
- Para alguém ser pediatra, ele precisa ser médico, logo, alguém ser pediatra implica que ele é médico
- 'P se Q' = 'Se Q, então P' : Q -> P

##### Análise Semântica de P<->Q
P Q P->Q Q->P (P->Q)^(Q->P)

| P | Q | P->Q | Q->P | (P->Q)^(Q->P) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| v | v | v | v | v |
| f | v | v | f | f |
| v | f | f | v | f |
| f | f | v | v | v |

Forma compacta:<br>
(P->Q)^(Q->P)
| | | | | | | |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| v | v | v | v | v | v | v |
| f | v | v | f | v | f | f |
| v | f | f | f | f | v | v |
| f | v | f | v | f | v | f |

##

#### Tabela veritativa de P <-> Q (Equivalência)
| P | Q | P <-> Q |
| - | - | ------- |
| v | v | v |
| f | v | f |
| v | f | f |
| f | f | v |

Sinopse: Uma equivalência é verdadeira se, e somente se ambos os membros tiverem os mesmos valores veritativos (vv, ff)<br>
Val(P<->Q)=v sss Val(P)=Val(Q) 

### Disjunção Exclusiva (∀)
Ex: Ou Pedro cuida de sua saúde, ou ele ficará doente. -> S ∀ D
  - S = Pedro cuida de sua saúde
  - D = ele ficará doente

P ∀ Q ⇆ (PvQ) ^ ~(P^Q)

Tabela Veritativa:

| P | Q | P ∀ Q |
| - | - | ------- |
| v | v | f |
| f | v | v |
| v | f | v |
| f | f | f |

Uma adjunção exclusiva é verdadeira se, e somente se os se, seus componetes tiverem valores veritativos distintos



## Convencoes de pontuacão

1. Dispensa do par exterior de parênteses
2. Hierarquia de pontuação: {^,v}, ->, <->
3. Sucessões de conectivos diáticos distintos de '->': a parentização considerada é da esquerda para a direita
4. Sucessões do conectivo '->': a parentização é da direita para a esquerda
