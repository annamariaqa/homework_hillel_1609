adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adventures_of_t_s_2 = adwentures_of_tom_sawer.replace("\n", " ")
#print(adwentures_of_tom_sawer)
print(adventures_of_t_s_2)

# task 02 ==
""" Замініть .... на пробіл
"""
adventures_of_t_s_3 = adventures_of_t_s_2.replace("....", " ")
print(adventures_of_t_s_3)
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adventures_of_t_s_4 = ' '.join(adventures_of_t_s_3.split())
print(adventures_of_t_s_4)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count = adventures_of_t_s_4.count('h')
print(count)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

adventures_of_t_s_split = adventures_of_t_s_4.split(' ')      
print(adventures_of_t_s_split)

index = 0
for word in adventures_of_t_s_split:
    if word.istitle():  
        print(f'Слово {index} починається з великої літери {word}')
    index += 1  


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
search_word = 'Tom'
search_word_index = adventures_of_t_s_4.find(search_word)  
len_of_search_word = len(search_word)  
final_index = search_word_index + len_of_search_word  
result_sent = adventures_of_t_s_4[final_index:] 
print(result_sent.find('Tom'))


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer_sentences = adventures_of_t_s_4.split('.')
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
adventures_task_8 = adwentures_of_tom_sawer_sentences[3]
adventures_task_8_lower = adventures_task_8.lower()
print(adventures_task_8_lower)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
found = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        found = True
        break 
if found:
    print("Речення починається з 'By the time'")
else:
    print("Немає речення, що починається з 'By the time'")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print(adventures_of_t_s_split[-1])
print(adventures_of_t_s_split[-2])
print(adventures_of_t_s_split[-3])
