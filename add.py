def add(self,*args):
    result = args[0]
    rsize = len(result)
    csize = len(result[0])
    for arg in args[1:]:
        if (len(arg) != rsize):
            raise ValueError
        for row in range(0,rsize):
            if (len(arg[row]) != csize):
                raise ValueError
            for col in range(0,csize):
                result[row][col] += arg[row][col]
    return result
