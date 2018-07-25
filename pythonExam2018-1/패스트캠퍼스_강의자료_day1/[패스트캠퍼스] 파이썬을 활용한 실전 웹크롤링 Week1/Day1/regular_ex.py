import re

# test1 = ['가지','나비','라디오']
#
# ex1 = re.compile('[가나다]')
#
# print('='*10,'예제1','='*10)
# for test in test1:
#     print(ex1.match(test))

# test2 = ['sam','훈민정음뷁', 'sam 오취리']
#
# ex2 = re.compile('[가-힣]')
#
# print('='*10,'예제2','='*10)
# for test in test2:
#     print(ex2.match(test))

# test3 = ['김철수 대리','김리 대리','윤 인성 대리','sam 대리']
#
# ex3 = re.compile('... 대리')
# ex4 = re.compile('.+대리')
# ex5 = re.compile('[가-힣]+ 대리')
# ex6 = re.compile('[가-힣]{2,3} 대리')
# print('='*10,'예제3','='*10)
# for test in test3:
#     print(ex3.match(test))
#     print(ex4.match(test))
#     print(ex5.match(test))
#     print(ex6.match(test))
#     print('='*10)
#
# test4 = ['http://www.naver.com','https://www.xdfkjer.co.kr','www.op.gg','www.slkdjf.com']
#
# ex7 = re.compile('^http://|^https://')
# ex8 = re.compile('com$')
# ex9 = re.compile('.*com$')
#
# print('='*10,'예제4','='*10)
# for test in test4:
#     print(test)
#     print(ex7.match(test))
#     print(ex8.match(test))
#     print(ex8.search(test))
#     print(ex9.match(test))
#     print('='*10)
#
with open('example.txt', 'r', encoding='utf-8') as example:
    test5=example.read().replace('\n', ' ')
print(test5)

ex10 = re.compile('([가-힣]{2,3})([0-9]{1})')
ex11 = re.compile('\([가-힣]{0,5}대\)')
quiz = re.compile('.[A-Z][0-9]{1,2}\.\s[가-힣a-zA-Z0-9\s\-]*\s\([가-힣]{2,3}\/[가-힣A-Z]*\).')
# print(ex10.findall(test5))
# iters = ex10.finditer(test5)
# for iter in iters:
#     print(iter.group(1))
# print(ex11.findall(test5))
print(quiz.findall(test5))
