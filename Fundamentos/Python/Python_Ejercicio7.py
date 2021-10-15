'''
Crear una función que recibe una lista.
De ella, debe sacar los números que no falten del set, que incluirá de 0 al 9.
Debemos usar una función llamada symmetricDifference.
'''

def ausentes(eva):
  setReferencia = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
  setEvaluar = sorted(set(eva))
  print(*setReferencia.symmetric_difference(setEvaluar))

lista = [2, 5, 4, 1, 8]
ausentes(lista)
