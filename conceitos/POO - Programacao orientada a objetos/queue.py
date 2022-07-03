class Queue:
  def __init__(self, q = None):
    'instancia uma lista vazia que conterá os itens da fila'
    if q == None:
      self.q =[]
    else:
      self.q = q
  def __eq__(self,outro):
    'retrona true se as filas self e outro tiverem os mesmos itens na mesma ordem'
    return self.q == outro.q
    
  def __repr__(self):
    'retorna a representacao da string canonica'
    return 'Queue {}'.format(self.q)
  
  def __getitem__(self,chave):
    return self.q[chave]
  
  '''def __setitem__(self, chave, item): #removi por não ser um método interessante para uma fila FIFO
    self.q[chave] = item''' #lembrar que esse método pode mudar qualquer item da fila
    
  def isEmpty(self):
      'retorna True se a fila estiver vazia, False caso contrário'
      return (len(self.q) == 0)
    
  def enqueue(self, item):
      'insere item no fim da fila'
      return self.q.append(item)
    
  '''def dequeue(self):
      'remove e retorna item na frente da fila'
      if len(self) == 0:
        raise KeyboardInterrupt('remoção de uma fila vazia')
      else:
        return self.q.pop(0)'''
    
  def dequeue(self):
    if len(self) == 0:
      raise EmptyQueueError('remoção de uma fila vazia')
    else:
        return self.q.pop(0)
