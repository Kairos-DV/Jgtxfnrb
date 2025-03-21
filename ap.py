
cord=(3,5)
'X: {0[0]};Y:{0[1]}'.format(cord)
'X: 3;Y:5'
'X: {0[0]}; Y:{0[1]}'.format(cord)
'X: 3; Y:5'
"rept() show quotes: {!r}; str() doesn`t: {!s}".format('test1','test2')
"rept() show quotes: 'test1'; str() doesn`t: test2"
'X: {0[0]}; Y:{0[1]}'.format(cord)
'X: 3; Y:5'
'X: {0[0]} | Y:{0[1]}'.format(cord)
'X: 3 | Y:5'
cord=(3, 5)
'X: {0[0]} | Y:{0[1]}'.format(cord)
'X: 3 | Y:5'
cord=(3.4, 5.5)

print('X: {0[0]!r} | Y:{0[1]!s}'.format(cord))
# 'X: 3.4 | Y:5.5'

# 'X: {0[0]!r} | Y:{0[1]!s}'.format(cord)cord=(3.4, 5.5)
# SyntaxError: invalid syntax
cord=(3.40001, 5.50001)
print('X: {0[0]!r} | Y: {0[1]!s}'.format(cord))
'X: 3.40001 | Y:5.50001'
cord=('3.40001', '5.50001')
print('X: {0[0]!r} | Y: {0[1]!s}'.format(cord))
"X: '3.40001' | Y:5.50001"
print('{0!r:>50}'.format('left aligned'))
':<30'
':>0'.format('left aligned')
':>0'
':>30'.format('left aligned')
':>30'
'{:>30}'.format('left aligned')
'                  left aligned'
'{:>50}'.format('left aligned')
'                                      left aligned'
print('{:^50}'.format('left aligned'))

# '                   left aligned

