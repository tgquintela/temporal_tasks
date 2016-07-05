
# Poder, parlamentos y democracia (I)
#### Un primer análisis sobre los parlamentos de Catalunya y España en 2015
## Introducción
Año 2015. España sufre una invasión mediática. Sus televisiones, periódicos y cualquier massive media, redes sociales, pequeños periódicos digitales, televisiones y foros se ven '*okupados*' por una serie de especimenes que nos dicen siempre lo que queremos oir y nos venden soluciones fáciles a problemas complejos. Son los políticos. El año 2015 se consagra como el año electoral por excelencia de la historia democrática de España.
Nunca antes habían coincidido elecciones municipales, catalanas (convertidas en centrales en el sistema político español) y estatales, con un pequeño aperitivo de las europeas de 2014 donde se nos dejó intuir que las cosas habían cambiado.
Un cambio de paradigma, una transición de fase. Pasábamos de un bipartidismo estable a un quatripartidismo estable y España comenzaba a conocer en toda su completa magnitud lo que es un sistema de elección de gobierno parlamentario.

Todo comenzó con ayuntamientos donde nuestro [glorioso presidente del gobierno nos  quiso dejar claro quien debía gobernar](https://www.youtube.com/watch?v=-JdFWHV2J9c), o al menos lo intentó. Después el siempre fraccionado Parlament de Catalunya, donde además de las problemáticas sociales y económicas, hay las propias del nacionalismo, dando pie a más posibilidades electorales estables y al final tuvimos parlamento español. Y en todos el mismo debate. ¿Quién debia gobernar? ¿Cuáles eran los pesos del poder? ¿Cómo formar gobierno?

Vale, pongamonos en situación. España vive en un sistema democrático (o aparentemente democrático para algunos), un sistema *democrático representativo*. La gente delega sus decisiones en una serie de cargos políticos elegidos en elecciones. Por la propia naturaleza de las leyes electorales españolas, el sistema se apoya fuertemente en partidos, que se presentan a las elecciones en listas cerradas. Los independientes acaban yendo en listas de partido. Los principales cargos que se pueden elegir son los parlamentos (que representan al poder legislativo) y los representates de gobiernos, alcaldes, gobiernos regiones y estatal (que representan al ejecutivo). Los parlamentos se eligen normalmente por unas elecciones que pueden ser más proporcionales o menos, más territorializadas o menos, con listas más abiertas o menos.

Los gobiernos también se pueden elegir de forma más directa o menos. Hay diferentes formas de elegirlos. Los miembros del gobierno de forma directa (más proporcionales o menos, más territorializadas o menos), el jefe de gobierno de forma directa (más proporcionales o menos, más territorializadas o menos) y el ya eligirá al resto del gobierno según le convenga, al gobierno de forma indirecta (a través del parlamento) o al jefe de gobierno de forma indirecta (a través del parlamento) y el ya eligirá según convenga. En España tenemos este último sistema.
Cada sistema tiene unas u otras propiedades, ventajas y desventajas. Algunas más y otras menos deseadas dentro de los valores democráticos. No hay una que se pueda decir que representa todos los valores democráticos según todos los representantes políticos nos intentan decir (cada uno siempre la que más le conviene), sino para los alumnos aventajados vean la [paradoja de Arrow](https://es.wikipedia.org/wiki/Paradoja_de_Arrow) y [Teoria de la deicion social](https://en.wikipedia.org/wiki/Social_choice_theory) para entender como todos se asignan la voluntad popular con convicción y el debate entorno a como elegir mediante elecciones problemas con multiples posibles soluciones.

La investidura en sistemas como el español ha puesto en el debate político la justicia o injusticia de esa decisión y como se reparte el poder y las responsabilidades en un sistema de elección (y votación) parlamentaria.
Ya que el parlamento no vota solo la investidura si no otras leyes, los presupuestos tendremos que buscar herramientas matemáticas que nos ayuden a *entender lo que pasa realmente*, a entender las dinámicas reales, más allá de ideologias e intereses.

## Teoria de juegos y las negociaciones
En plena crisis griega surgió la figura de un roquero, rapado y motero, interminablemente alto y con un atractivo especial y diferente. Intelectualmente imponente decidió seguir una estrategia de negociación con los ministros de finanzas de la eurozona no esperada por la mayoría. Y volvió a resucitar en la prensa, por enésima vez, la teoria de juegos para el uso de políticos. Teoria de juegos que para la gran mayoría de los políticos y los mortales significa la película archiconocida ('[_A beautiful mind_](http://www.imdb.com/title/tt0268978/)') de la vida de uno de sus creadores John Nash, y alguna frases hechas como "es un juego de suma cero", o "hay que buscar el equilibrio de Nash", normalmente mal empleadas. En circulos un poco más intelectuales estaría el mantra de "[La tragedia de los comunes](https://en.wikipedia.org/wiki/Tragedy_of_the_commons)" para justificar uno ideología y la contraria. Al final todos han intentado apropiarse de la teoria de juegos. En ciencia las cosas han sido mucho más serias y ha sido una de las teorias más influyentes en ciencia, aportando en diferentes campos de la ciencia muy diversos.

Tampoco tenemos suficiente espacio y tiempo para tratar de enseñar las bases de esta teoria en unas pocas líneas, pero voy a intentar resumir su enfoque básico y su importancia de la forma más breve posible.
La teoría de juegos busca dar un marco matemático a situaciones en las que intervienen más de un agente, que pueden tomar decisiones y ser recompensados positiva o negativamente según las decisiones del conjunto de los agentes.
De esta forma una decisión propia no siempre será buena o mala por ella misma, dependerá de las decisiones tomadas por los demás. Es aquí donde radica su complejidad así como su generalidad. Como podéis observar esto es aplicable a la mayoría de situaciones en nuestra vida. Las negociaciones no son una excepción, de hecho, interacción consciente más directa entre agentes es dificil encontrar.

A todo esto, la aplicación básica y más conocida de la teoría de juegos es cuales son las acciones por las cuales todos los agentes estarían resignados a ello. Y esa es la palabra, resignados y no satisfechos, conformados, contentos o enfadados. Y digo resignados, porque ninguno de los agentes cambiaría su acción o decisión unilateralmente. A esto es a lo que le llaman **equilibrio de Nash**. No es el mejor de los resultados entre todas las posibilidades, ni para el colectivo ni para los agentes individualmente, pero sí que es un resultado que por malo que sea nadie cambiaría sus acciones de forma unilateral.

## Teoria de juegos y el poder de los grupos parlamentarios
Entre la teoría de juegos, no solo se estudia cuales son los equilibros estables o situaciones más probables (en las aplicaciones sobre el mundo real). Este es uno de los casos que nos pertoca, el estudio de poder en los sistemas de votaciones con más de un voto por agente.
Estos sistemas son modelizados en la teoría de juegos como juegos cooperativos.
El caso específico de estos sistemas es que las acciones que pueden tomar los agentes es con quienes cooperar y el reparto de beneficios viene dado por el resultado final de las coaliciones.
Esto es una modelización aceptable para los sistemas de votación parlamentario donde los grupos parlamentarios no dan libertad de voto a sus miembros y votan en bloque (tal como pasa en la mayoría de ocasiones en España y en sus ayuntamientos y CA).

Dentro de esta teoría adaptada a nuestro caso tenemos los jugadores (o los bloques de votación conjunta, normalmente grupos parlamentarios, pero puede haber subgrupos y demás ahora con las convergencias que quizás sea mejor considerarlos por separado), las coaliciones (asociadas a las votaciones posibles que hagan, es decir, normalmente 'sí', 'no' y 'abstención') y el valor de una coalición (si la coalición gana la votación según el ratio necesario para ganar, es decir, la coalición 'sí' para algunas necesita 1/2+1 y para otras mayoría cualificada 2/3+1).

A partir de ello podemos construirnos definiciones de poder de cada jugador (grupo parlamentario). Hay varias medidas en la teoría de juegos de juegos cooperativos. Las dos más conocidas (ambas son valores basados en modelos aleatorios de formación de coaliciones) son:
* [Valor de shapely](https://en.wikipedia.org/wiki/Shapley%E2%80%93Shubik_power_index)(o índice de Shapley-shubik en nuestro caso de votación): en el cual las coaliciones se forman mediante ordenación aleatoria. El valor calculado es el valor esperado (media) del premio que se repartiran los ganadores en todas las ordenaciones posibles, considerando que ganan todos los primeros necesarios para superar la votación. En esta medida solo computamos las posibles combinaciones con victorias mínimas del 'si' (y considerando un mínimo fijo, no mayorias simples). Podemos atribuir a las victorias 1 y a las derrotas 0. Nuestro valores de shapely quedarán entre 0 y 1 y entre todos sumarán valor 1.
* [Índice de poder de Bhanzaf](https://en.wikipedia.org/wiki/Banzhaf_power_index): en el cual se mide cuantas veces respecto al total un jugador es pivote. Un jugador es pivote si convierte una coalición perdedora en una ganadora. Esto nos da un índice de poder en el cual todos estan entre 0 y 1 y suman 1. Además el jugador dictador (el que tiene mayoria absoluta para el límite dado de la votación) tiene 1, y los jugadores falsos (los que no tienen voz a la hora de convertir perdedores en ganadores) tienen valor 0.

Aplicar estas medidas a las votaciones parlamentarias no es nuevo. Así las aprendí yo en clase de *Teoría de Juegos* y así leí no hace mucho un [artículo de Elpais aplicandolas al actual parlamento](http://politica.elpais.com/politica/2016/02/26/actualidad/1456513163_817921.html). Lo cierto es que me sorprendió descubrirlo, más que nada porque pensaba escribir de forma crítica una entrada en mi futuro blog entonces (actual ahora) sobre ello (como puede demostrar mis códigos en [github](https://github.com/tgquintela/CooperativeGames) :D), aunque discrepo en el uso que hace de ellas y sus conclusiones que deja en lineas y entre lineas.

## Aplicación sobre el Parlament de Catalunya
Para simplificar la complejidad de 350 dipudatos y diputadas y unas cuantas fuerzas políticas en el parlamento nos iremos a Catalunya. 'Solo' 6 grupos parlamentarios y 135 diputados. El Parlament nos ayudará a usar primeramente estas medidas y a comenzar a ser *críticos* sobre ellas.
Cabe decir que en estas medidas medimos SOLO el poder que se tiene en votaciones puntuales o generales, pero no el poder general. Para eso se debería tener en cuenta las complejidades organizativas del propio Parlament y sus organos de gobierno propio (Presidencia, vicepresidencia y secretarios) que controlan y regulan el dia a dia del parlament.
Además obviaremos la posibilidad de abstención y de mayorias simples (que no tienen un mínimo de victoria fijo).

Recordemos los resultados de las elecciones que fueron los siguientes:

| JxSi | Cs | PSC | CSQEP | PP | CUP |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 62 | 25 | 16 | 11 | 11 | 10 |

Si aplicamos el índice de Shapley-Shubik, sobre un mínimo de victoria de la mitad de los diputados (comparados con la proporción de diputados que tienen), nos encontraremos estos resultados:

| *medida* | JxSi | Cs | PSC | CSQEP | PP | CUP |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Proporc. | 0.46 | 0.18 | 0.12 | 0.08 | 0.08 | 0.07 |
| Shapley | 2/3 | 1/15 | 1/15 | 1/15 | 1/15 | 1/15 |

Para los no crédulos les dejo aquí un *script* (pequeño programa) usando mi código de github para calcularlo.

```python
# Resultados
seats = [62, 25, 16, 11, 11, 10]
names = ['JxSi', 'Cs', 'PSC', 'CSQEP', 'PP', 'CUP']

# Importar paquetes necesarios
from cooperativegames import shapley_index, show_power_indices

# Cálculo
win_thr = 0.5  # Proporcion de seats para ganar
sh_sh_ind = shapley_index(seats, win_thr)
show_power_indices(sh_sh_ind, names)
```

Como podemos ver la suma de dichos índices es 1. JxSi acapara gran parte del poder y el resto se lo reparten de forma uniforme. Esto es porque son jugadores simétricos ante la victoria. Las coaliciones ganadoras posibles mínimas son JxSi más algún otro partido o el resto todos juntos.
Esto lo único que nos explica de lo que actualmente pasa en el parlament no es más que el alto poder que tiene JxSi, pero obvia a la CUP y su poder de decisión.

Si nos vamos al índice de Bhanzaf obtendremos:

| *medida* | JxSi | Cs | PSC | CSQEP | PP | CUP |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Proporc. | 0.46 | 0.18 | 0.12 | 0.08 | 0.08 | 0.07 |
| Banzhaf | 0.75 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 |

Aquí el *script*:
```python
# Resultados
seats = [62, 25, 16, 11, 11, 10]
names = ['JxSi', 'Cs', 'PSC', 'CSQEP', 'PP', 'CUP']

# Importar paquetes necesarios
from cooperativegames import banzhaf_index, show_power_indices

# Cálculo
win_thr = 0.5  # Proporcion de seats para ganar
bzf_ind = banzhaf_index(seats, win_thr)
show_power_indices(bzf_ind, names)
```

El resultado es igual de revelador. Los números cambian un poco pero no lo que nos dicen. Parecen insuficientes para explicarnos que pasa realmente.

Quizás sea porque lo que sucede va más allá de los datos que estamos mirando. Según los diputados repartidos tenemos a JxSi con muchos diputados y cerca de la mayoría absoluta, mientras que el resto se quedan lejos y necesitan muchos apoyos y grandes coaliciones para llegar a la mayoría.
Estas medidas de poder miden cuanta dependencia específica tienes de otros jugadores para conseguir tus objetivos, cuanto más dependas del resto menos poder. Es por eso que JxSi tiene tanto. 

En cambio si queremos entrar en porqué la CUP tiene tanto poder en esta legislatura tendremos que adentrarnos en el mundo real y ver el contexto y la situación específica que sucede. Y lo que nos encontramos es que hay ciertas coaliciones que son más probables que otras. Hay 'topología' entre los jugadores. No son meros votantes categoricos sin nada en relación. Unos están más cerca de otros que de otros.
Esta 'topología' (las relaciones, similitudes y distancias, entre los jugadores) es dificilmente estudiable sin más y por tanto muy dificil medir cuál está más cerca de unos que de otros y como son de probables cada una de las coaliciones.
Definir una matriz de probabilidades de coalición uno a uno o de similitud entre partidos es dificil y **siempre arbitraria**, cojamos el criterio que cojamos. Tan arbitraria como medir el poder utilizando una u otra medidas.

Hay gente que busca de estudiar utilizando sus programas o para situarlos en un espacio político-ideologico o también llamado espectro político-ideológico (como el izquierda-derecha, el [diagrama de Nolan](https://en.wikipedia.org/wiki/Nolan_Chart), o otros modelos uni-eje o multi-eje) en los cuales podemos medir distancias.
Aquí, para atacar dicho problema intentaremos redefinir las medidas de forma razonable y crear una matriz de similutes de forma razonable, basados en datos medibles directamente o indirectamente.

De estas datos medibles que podriamos pensar es en la percepción de los ciudadanos sobre los partidos en dichos espacio político-ideologicos.
O para *simplificar*, en alguno de sus ejes como la percepción que tienen del eje derecha-izquierda de esos partidos. Existen encuestas de opinión que nos aclararian esta circunstancia. Aunque tampoco parece que sea lo más descriptivo de la situación que sucede en el Parlament, quizás en clave modelo de estado (autonomismo-independentismo) podría ser más descriptivo.
En el [Centre d'Estudis Catalans](http://ceo.gencat.cat) nos ofrece en parte alguna de estas repuestas. Nos da una valoración del eje derecha-izquierda y en españolismo-catalanismo (que no independentismo o permanencia). También podemos encontrar algunos posicionamientos sobre la indpendencia por voto a partidos.

Aquí mostraré el posicionamiento de otros y a ellos mismos, sacado del [primer CEO de 2016](http://ceo.gencat.cat/ceop/AppJava/loadFile?fileId=24313&fileType=1):

| *ejes* | JxSi | Cs | PSC | CSQEP | PP | CUP |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| auto izq-drcha | 3.82 | 5.15 | 4.08 | 3.27 | 6.24 | 2.33 |
| izq-drcha | 4.86 | 7.58 | 5.08 | 3.77 | 8.74 | 1.76 |
| auto esp-cat | 8.06 | 3.89 | 4.20 | 5.47 | 3.18 | 7.95 |
| esp-cat | 7.73 | 2.27 | 4.01 | 6.23 | 1.33 | 8.44 |
| independencia | 81.9 | 1.6 | 7.3 | 9.8 | 2.6 | 78.2 |

Con estos números podemos medir distancias y calcular ciertas matrices de proximidad normalizadas. Estas matrices las podemos interpretar como cuán probable es dicha coalición uno a uno, o cuán probable es que ambos esten en la misma coalición.

Para medir cuán poderoso es un jugador utilizando las matrices de afinidad política y la misma idea que las anteriores medidas. En este caso, en vez de sumar cuantas veces forma parte de una coalición ganadora, pesaremos dichas coaliciones sobre cuán probables son, y en vez de mirar cuantas veces puede ser jugador pivote sobre el total de coaliciones ganadores, pesaremos dichas coaliciones con cuán probable son según la matrix de similitud calculada.

Para hacer lo explicado en este párrafo hay diferentes formas de realizarlo. En los siguientes cálculos utilizaremos una de ellas para conseguir los resultados siguientes:

| *medida* | JxSi | Cs | PSC | CSQEP | PP | CUP |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Proporc. | .459 | .185 | .118 | .081 | .081 | .074 |
| Shapley | .667 | .067 | .067 | .067 | .067 | .067 |
| Banzhaf | .750 | .050 | .050 | .050 | .050 | .050 |
| win_i_d_auto | .322 | .138 | .153 | .147 | .113 | .127 |
| wor_i_d_auto | .368 | .128 | .155 | .144 | .093 | .111 |
| win_i_d | .363 | .122 | .165 | .150 | .095 | .103 |
| wor_i_d | .412 | .109 | .170 | .146 | .077 | .085 |
| win_esp_cat_auto | .351 | .124 | .130 | .145 | .106 | .144 |
| wor_esp_cat_auto | .362 | .117 | .126 | .150 | .092 | .153 |
| win_esp_cat | .383 | .095 | .135 | .165 | .070 | .150 |
| wor_esp_cat | .408 | .082 | .129 | .173 | .057 | .151 |
| win_independ | .438 | .073 | .094 | .102 | .077 | .214 |
| wor_independ | .431 | .067 | .091 | .101 | .071 | .240 |


Para los no crédulos podéis mirar la forma decidida para calcularlos dentro del código subido a github o utilizarlo para obtener los resultados corriendo este *script*:

```python
from tools import from_positions2weights
from cooperativegames import weighted_winning_coalitions,\
    weighted_worsable_coalitions

eje_i_d = [.486, .758, .508, .377, .874, .176]
eje_i_d_auto = [.382, .515, .408, .327, .624, .233]
eje_esp_cat = [.773, .227, .401, .623, .133, .844]
eje_esp_cat_auto = [.806, .389, .420, .547, .318, .795]
eje_independencia = [.819, .016, .073, .098, .026, .782]
matrix_i_d = from_positions2weights(eje_i_d)
matrix_i_d_auto = from_positions2weights(eje_i_d_auto)
matrix_esp_cat = from_positions2weights(eje_esp_cat)
matrix_esp_cat_auto = from_positions2weights(eje_esp_cat_auto)
matrix_independencia = from_positions2weights(eje_independencia)

seats = [62, 25, 16, 11, 11, 10]
names = ['JxSi', 'Cs', 'PSC', 'CSQEP', 'PP', 'CUP']
win_thr = 0.5  # Proporcion de seats para ganar

win_i_d = weighted_winning_coalitions(seats, matrix_i_d, win_thr)
win_i_d_auto = weighted_winning_coalitions(seats, matrix_i_d_auto, win_thr)
win_esp_cat = weighted_winning_coalitions(seats, matrix_esp_cat, win_thr)
win_esp_cat_auto = weighted_winning_coalitions(seats, matrix_esp_cat_auto, win_thr)
win_ind = weighted_winning_coalitions(seats, matrix_independencia, win_thr)

wor_i_d = weighted_worsable_coalitions(seats, matrix_i_d, win_thr)
wor_i_d_auto = weighted_worsable_coalitions(seats, matrix_i_d_auto, win_thr)
wor_esp_cat = weighted_worsable_coalitions(seats, matrix_esp_cat, win_thr)
wor_esp_cat_auto = weighted_worsable_coalitions(seats, matrix_esp_cat_auto, win_thr)
wor_ind = weighted_worsable_coalitions(seats, matrix_independencia, win_thr)

```

En estos resultados podemos ver que la CUP pasa a tener más poder que otros como Cs, PSC, CSQEP y PP, a pesar de tener menos representantes. Esto es debido a que es el aliado más natural al partido con más cercanía a la mayoría absoluta y solo basta con su alianza para conseguirla.

En el caso extremo de solo considerar la variable binaria independencia (independencia SI o independencia NO) veriamos que dividiriamos el parlamento en dos grupos: los que están a favor (JxSi y CUP) y los que estan en contra (Cs, PSC, CSQEP y PP), con todos los matices que podamos poner. En este caso extremo de total polaridad y discrepancia, bastante similar lo que llevamos vivido hasta hoy en Junio de 2016, quedaría:

| *medida* | JxSi | Cs | PSC | CSQEP | PP | CUP |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| extremo | 0.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.5 |

En este hipotético caso, los del grupo que no llegan a la mayoría quedan fuera de las decisiones y sus votaciones no valen para nada, mientras que los dos que pueden 
decidir esto, acaban repartiendose el poder restante, ya que uno sin el otro no pueden hacer nada (son jugadores simétricos en estas circunstancias), sin tener en cuenta el número de diputados de cada uno (para las votaciones, no para el resto de medidas parlamentarias y gestiones que aquí no tratamos).
Esto tiene sus dilemas democráticos, y muy interesantes, que si eso ya trataremos otro día trataremos y en otro post.


## Aplicación sobre el Congreso de los Diputados
Aplicaremos las mismas medidas que hemos aprendido para el Congreso de los Diputados de la XI legislatura. En este caso han corrido también rios de tinta por la complicación y la final falta de acuerdo para la investidura.
Veremos a ver si podemos ver algo diferente aplicando las medidas oportunas.

Consideraremos solo el eje izquierda-derecha para computar cuán probable es una coalición (aunque la realidad nos hace sospechar que no será suficiente para entender la complejidad real).
Tenemos diferentes combinaciones para utilizar debido a la cantidad de confluencias que se dan y pequeños matices (PP con PAR, Foro y UPN, Podemos con Marea, ECP y Compromis; PSOE con PSC, ...). Como tampoco ha habido mucho más a votar que la investidura intentaré ser un poco simplista para no engordar demasiado la lista de jugadores (debido también a la complejidad computacional de los calculos combinatorios de alianzas que pueden poner en complicaciones a según que ordenadores). Los resultados serán entonces:

| PP | PSOE | Podemos | Cs | ERC | DiL | PNV | IU | Bildu | CC |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 123 | 90 | 69 | 40 | 9 | 8 | 6 | 2 | 2 | 1 |


Para construir la matriz de similitud, podemos utilizar el posicionamiento en el eje izquierda-derecha que según el [CIS de Enero 2016](http://www.cis.es/cis/export/sites/default/-Archivos/Marginales/3120_3139/3124/Es3124mar.pdf) es:

| *ejes* | PP | PSOE | Podemos | Cs | ERC | DiL | PNV | IU | Bildu | CC |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| izq-drcha | 8.28 | 4.49 | 2.26 | 6.65 | 3.01 | 6.34 | 5.97 | 2.27 | 2.92 | 5.96 |

Aplicando las mismas medidas utilizadas previamente nos encontramos con:

| *ejes* | PP | PSOE | Podemos | Cs | ERC | DiL | PNV | IU | Bildu | CC |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Proporc. | .351 | .257 | .197 | .114 | .026 | .023 | .017 | .006 | .006 | .003 |
| Shapley | .402 | .220 | .220 | .070 | .030 | .025 | .020 | .006 | .006 | .002 |
| Banzhaf | .378 | .210 | .210 | .084 | .040 | .033 | .026 | .008 | .008 | .003 |
| win_i_d | .192 | .172 | .117 | .106 | .067 | .089 | .088 | .043 | .053 | .074 |
| wor_i_d | .156 | .203 | .101 | .110 | .062 | .097 | .098 | .036 | .050 | .086 |

que podéis calcular utilizando el siguiente *script*:

```python
from cooperativegames import shapley_index, banzhaf_index,\
    weighted_winning_coalitions, weighted_worsable_coalitions
from tools import from_positions2weights

# Datos para el calculo
seats = [123, 90, 69, 40, 9, 8, 6, 2, 2, 1]
names = ['PP', 'PSOE', 'Podemos', 'Cs', 'ERC', 'DiL', 'PNV', 'IU', 'Bildu', 'CC']
win_thr = 0.5  # Proporcion de seats para ganar
eje_i_d = [.828, .449, .226, .665, .301, .634, .597, .227, .292, .596]
matrix_i_d = from_positions2weights(eje_i_d)

# Medidas
sh_sh_ind = shapley_index(seats, win_thr)
bzf_ind = banzhaf_index(seats, win_thr)
win_i_d = weighted_winning_coalitions(seats, matrix_i_d, win_thr)
wor_i_d = weighted_worsable_coalitions(seats, matrix_i_d, win_thr)

```

No hemos incluido los pequeños matices, ni otros ejes que pueden ser relevantes en las discrepancias para pactos, pero podemos sacar pequeñas conclusiones de estas medidas y lo que nos dicen. PSOE tiene más poder que la proporción representativa de diputados que tienen. PP y Podemos mucho menos de la proporción de escaños que tiene. El parlamento se lo da o parece ser que así nos lo indican estas medidas. Pero quedan lejos de acercarse a una proporción dominante.

Mientras en el caso del Parlament nos encontramos dos *clusters* (grupos) practicamente cerrados en los que parece que cada *cluster* va por su lado y hay una desconexión clara entre ambos (una polarización clara). En el que uno de los dos tiene claramente más tamaño que el otro y por tanto guía el camino y controla el poder.
En el caso del Congreso de Diputados de la XI legislatura, tenemos muchos más '*puentes*'. No parece haber unos grupos claros, con varios partidos que pueden pivotar con cierta libertad según les convengan para conseguir más poder e influencia sobre decisiones. Estas medidas lo que acaban pareciendo premiar es una cierta centralidad relativa, la centralidad que es asignada por el parlamento votado por la gente. En este congreso la media ponderada de ideología política que representa al congreso parece ser *5.64* y por tanto los más beneficiados por estas medidas de poder son CC (*5.96*), PNV (*5.97*), DiL (*6.34*) o PSOE (*4.49*).

Que la centralidad da poder parece un hecho que consciente o inconscientemente conocen y por tanto utilizan todos los partidos. Unos asignandose la centralidad absoluta en el eje derecha-izquierda u otros ejes como el PP, otros proponiendose puntos intermedios y haciendo balances entre sus vecinos en un posible espacio político como son Cs y PSOE, o proponiendose mediador en otros ejes como en el dilema territorial, como Podemos.

Estos son los números que parecen describir la realidad. Después quedan las interpretaciones donde unos asignarán a estos números el reflejo de la decisión de la ciudadanía mientras que otros los colocarán como un reparto de responsabilidades ante los fracasos de las negociaciones que se realicen. Eso ya es política.


## Conclusión
Como podemos ver aquí conceptualmente, sí que podemos construir medidas que se adapten y expliquen lo que realmente pasa en los parlamentos, desde medidas derivadas de la teoría de juegos. Esta posibilidad es extendible a muchos problemas de decisiones cooperativas en entornos competitivos como alianzas y busqueda de sinérgias entre empresas en mercado.

Para hacer medidas más predictivas, a parte de necesitar más datos, tendríamos que tener en cuenta dinámicas y procesos dependientes en estrategias de posicionamiento y diferenciación que también podemos ver en el marketing entre empresas en el mercado. Esos partidos centrales que podrían gestionar situaciones para llevar las negociaciones a su propio programa. Esto puede ser barrera para llegar a pactos entre dos partidos sin ser ellos el que se mantiene en la centralidad. Quizás en otra entrada estudie más sobre este tema y podamos aclarar alguna de estas nuevas dudas.

Espero con esto haber ayudado a gente a entender mejor como funciona un sistema parlamentario, y como es de diferente a uno de votación directa. También a entender la importancia de unos pocos diputados más y los fenómenos y dinámicas que suceden cada día en nuestro parlamento. Y como no, sobretodo saber que toda explicación se puede dar en terminos matemáticos, como cualquier justificación (así que cuidado).


## Bibliografía
Para más información:

* Shapley, L. S.; Shubik, M. (1954). [*A Method for Evaluating the Distribution of Power in a Committee System*](http://journals.cambridge.org/abstract_S0003055400000095). American Political Science Review 48 (3): 787-792. 
* Banzhaf, John F. (1965), [*Weighted voting doesn't work: A mathematical analysis*](http://heinonline.org/hol-cgi-bin/get_pdf.cgi?handle=hein.journals/rutlr19&section=19), Rutgers Law Review 19 (2): 317-343
* Downs, Anthony (1957). [*An economic theory of democracy*](https://www.goodreads.com/book/show/335514.An_Economic_Theory_of_Democracy). New York.
* [Mi scripts en github](https://github.com/tgquintela/CooperativeGames)





