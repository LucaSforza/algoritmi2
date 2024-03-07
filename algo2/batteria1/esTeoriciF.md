# es3
```python
for 

```
- (a) Dimostrare che in un grafo connesso G ci sono sempre almeno due vertici
che hanno lo stesso grado.

    prendiamo i gradi di un grafo non orientato che possono variare da 0 a n-1, 
    il grafo essendo connesso varia da 1 a n-1 perche nessun nodo puo avere grado 0
    quindi quando vado a vedere i gradi di tutti i nodi al caso pessimo arrivo 
    all'penultimo dove opgni nodo ha un grado diverso , e l'ultimo sicuramente avra 
    un grado come uno dei precedenti

—l’affermazione ‘e ancora valida nel caso in cui il grafo non sia connesso?

    il principio funziona anche se il grafo e sconnesso perche i possibili ordini 
    variano da 0 a n-2 perche essendoci almeno un nodo sconnesso nessun nodo ha 
    ordine n-1

(b) Dimostrare che se tutti i vertici di un grafo G hanno grado almeno due
allora nel grafo G c’‘e almeno un ciclo.
Se il grado di ogni vertice ‘e esattamente due, si pu‘o a↵ermare che G e un
ciclo?


es4

Dimostrare che ogni grafo connesso contiene un vertice la cui rimozione
non sconnette il grafo

    se il grafo ha un nodo di ordine 1 posso rimuovere quello e il grafo non si sconnette
    da dimostrare che con l'albero di un DFS togliendo una sua foglia non sconnetto il grafo


teorema da dimostrare per casa 
    sia f una foglia di una dfs di g  = (v,e) il sottografo indotto da V\{f} e connesso 


es del esercitatore 7 marzo

    sia G un grafo non orientato, dimostrare che se uno tra G e Gcomplementare e connesso

    caso 1 se G e connesso dimostrato perche G stesso e connesso 
    caso 2 se G ha un solo nodo sconnesso da tutto il resto del grafo , 
        nel grafo complementare quel nodo sara connesso a tuttio glialtri 
        e g complementare sara connesso
    caso 3 se G ha due sottografi sconnessi nel grafo complementare ogni punto di un 
        sottografo sara connesso a tutti gli altri dell altro sottografo   stessa cosa
         nell'altro senso e tutto sara connesso 