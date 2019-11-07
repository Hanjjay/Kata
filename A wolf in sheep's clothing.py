def warn_the_sheep(queue):
    a = len(queue)
    b = queue.index("wolf")+ 1
    d = a-b
    
    if b<a:
        return "Oi! Sheep number %d! You are about to be eaten by a wolf!"%(d)
    else:
        return 'Pls go away and stop eating my sheep'
c =['sheep', 'sheep', 'wolf']
e =["sheep", "sheep", "sheep", "wolf", "sheep"]
warn_the_sheep(c)
warn_the_sheep