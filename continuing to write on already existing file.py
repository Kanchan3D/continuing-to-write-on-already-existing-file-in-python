'''opeaning file 'txt1.txt' in append mode
    This mode will continue to write on file 'txt1.txt' if already exist and
    If file 'txt1.txt' was not created before then it will be created.'''
f=open('txt1','a')


f.write('\nWe are continuing to write on already exisiting file.')
