def exibeagenda(n):
    if n < 0 or n > 60:
        return 'Informe um valor válido.'
    elif n==0:
        return '00:00'
    else:
        a = '00'
        b = '00'
        horarios = ''
        while int(a) < 24:
            if int(b) < 60:
                horarios+=a+':'+b+'\n'
                b = str(int(b)+n).zfill(2)
                if int(b) >= 60:
                    b = str(int(b)-60).zfill(2)
                    a = str(int(a)+1).zfill(2)
        return horarios