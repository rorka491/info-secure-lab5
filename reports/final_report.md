# Лабораторная работа № 5 Криптография

Учебная модель, не для реальной защиты.
Не является юридически значимой УКЭП.
TLS-модель не совместима с реальным протоколом.

## Паспорт

CryptoLab · лабораторная работа № 5. Вымышленные данные. JSON → репозиторий → сервисы → доменные функции → отчёт. Dishka связывает зависимости CLI и GUI.

## Итог по разделам

{
  "classics": true,
  "analysis": true,
  "stego": true,
  "hash": true,
  "signature": true,
  "tls": true,
  "incidents": true,
  "tests": true
}

## Учебные сообщения

[
  {
    "id": "short",
    "alphabet": "en",
    "purpose": "Короткая фраза",
    "text": "Meet at noon.",
    "algorithms": [
      "caesar",
      "atbash",
      "polybius",
      "vigenere",
      "permutation",
      "rotor"
    ]
  },
  {
    "id": "medium",
    "alphabet": "en",
    "purpose": "Средний образец",
    "text": "At noon the study group meets by the garden. The group tests a model carrier and records the results. Later the group compares the original message with the decoded text.",
    "algorithms": [
      "caesar",
      "atbash",
      "polybius",
      "vigenere",
      "permutation",
      "rotor"
    ]
  },
  {
    "id": "punctuation",
    "alphabet": "en",
    "purpose": "Регистр и пунктуация",
    "text": "Quiet, lab team! Ready?",
    "algorithms": [
      "caesar",
      "atbash",
      "polybius",
      "vigenere",
      "permutation",
      "rotor"
    ]
  },
  {
    "id": "repeated",
    "alphabet": "en",
    "purpose": "Повторяющиеся буквы",
    "text": "AAAA BALLOON BALLOON",
    "algorithms": [
      "caesar",
      "atbash",
      "polybius",
      "vigenere",
      "permutation",
      "rotor"
    ]
  },
  {
    "id": "rare",
    "alphabet": "en",
    "purpose": "Редкие буквы",
    "text": "Jazz wax quiz",
    "algorithms": [
      "caesar",
      "atbash",
      "polybius",
      "vigenere",
      "permutation",
      "rotor"
    ]
  },
  {
    "id": "russian",
    "alphabet": "ru",
    "purpose": "Контрольный пример Цезаря",
    "text": "ВСТРЕЧА УЧЕБНОЙ ГРУППЫ В ДЕСЯТЬ ЧАСОВ",
    "algorithms": [
      "caesar",
      "atbash",
      "polybius",
      "vigenere",
      "permutation",
      "rotor"
    ]
  },
  {
    "id": "latin",
    "alphabet": "en",
    "purpose": "Латиница",
    "text": "A fictional signal.",
    "algorithms": [
      "caesar",
      "atbash",
      "polybius",
      "vigenere",
      "permutation",
      "rotor"
    ]
  },
  {
    "id": "digits",
    "alphabet": "ru",
    "purpose": "Сохранение цифр",
    "text": "КОД 42, ЭТАП 7.",
    "algorithms": [
      "caesar",
      "atbash",
      "polybius",
      "vigenere",
      "permutation",
      "rotor"
    ]
  },
  {
    "id": "long",
    "alphabet": "en",
    "purpose": "Длинный образец",
    "text": "At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message.At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message.",
    "algorithms": [
      "caesar",
      "atbash",
      "polybius",
      "vigenere",
      "permutation",
      "rotor"
    ]
  }
]

## Классические шифры

| Набор | Алгоритм | Открытый текст | Параметры | Шифротекст | Восстановление | Проверка |
| --- | --- | --- | --- | --- | --- | --- |
| short | caesar | Meet at noon. | {'shift': 3} | Phhw dw qrrq. | Meet at noon. | ok |
| short | atbash | Meet at noon. | {} | Nvvg zg mllm. | Meet at noon. | ok |
| short | polybius | Meet at noon. | {'aliases': {'J': 'I'}} | [[3, 2, false], [1, 5, true], [1, 5, true], [4, 4, true], " ", [1, 1, true], [4, 4, true], " ", [3, 3, true], [3, 4, true], [3, 4, true], [3, 3, true], "."] | Meet at noon. | ok |
| short | vigenere | Meet at noon. | {'key': 'LAB'} | Xefe au yopy. | Meet at noon. | ok |
| short | permutation | Meet at noon. | {'key': [2, 0, 3, 1]} | eMtet  aonno. | Meet at noon. | ok |
| short | rotor | Meet at noon. | {'offset': 2, 'wiring': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'} | Wnrx xx aisr. | Meet at noon. | ok |
| medium | caesar | At noon the study group meets by the garden. The group tests a model carrier and records the results. Later the group compares the original message with the decoded text. | {'shift': 3} | Dw qrrq wkh vwxgb jurxs phhwv eb wkh jdughq. Wkh jurxs whvwv d prgho fduulhu dqg uhfrugv wkh uhvxowv. Odwhu wkh jurxs frpsduhv wkh ruljlqdo phvvdjh zlwk wkh ghfrghg whaw. | At noon the study group meets by the garden. The group tests a model carrier and records the results. Later the group compares the original message with the decoded text. | ok |
| medium | atbash | At noon the study group meets by the garden. The group tests a model carrier and records the results. Later the group compares the original message with the decoded text. | {} | Zg mllm gsv hgfwb tilfk nvvgh yb gsv tziwvm. Gsv tilfk gvhgh z nlwvo xziirvi zmw ivxliwh gsv ivhfogh. Ozgvi gsv tilfk xlnkzivh gsv lirtrmzo nvhhztv drgs gsv wvxlwvw gvcg. | At noon the study group meets by the garden. The group tests a model carrier and records the results. Later the group compares the original message with the decoded text. | ok |
| medium | polybius | At noon the study group meets by the garden. The group tests a model carrier and records the results. Later the group compares the original message with the decoded text. | {'aliases': {'J': 'I'}} | [[1, 1, false], [4, 4, true], " ", [3, 3, true], [3, 4, true], [3, 4, true], [3, 3, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [4, 3, true], [4, 4, true], [4, 5, true], [1, 4, true], [5, 4, true], " ", [2, 2, true], [4, 2, true], [3, 4, true], [4, 5, true], [3, 5, true], " ", [3, 2, true], [1, 5, true], [1, 5, true], [4, 4, true], [4, 3, true], " ", [1, 2, true], [5, 4, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [2, 2, true], [1, 1, true], [4, 2, true], [1, 4, true], [1, 5, true], [3, 3, true], ".", " ", [4, 4, false], [2, 3, true], [1, 5, true], " ", [2, 2, true], [4, 2, true], [3, 4, true], [4, 5, true], [3, 5, true], " ", [4, 4, true], [1, 5, true], [4, 3, true], [4, 4, true], [4, 3, true], " ", [1, 1, true], " ", [3, 2, true], [3, 4, true], [1, 4, true], [1, 5, true], [3, 1, true], " ", [1, 3, true], [1, 1, true], [4, 2, true], [4, 2, true], [2, 4, true], [1, 5, true], [4, 2, true], " ", [1, 1, true], [3, 3, true], [1, 4, true], " ", [4, 2, true], [1, 5, true], [1, 3, true], [3, 4, true], [4, 2, true], [1, 4, true], [4, 3, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [4, 2, true], [1, 5, true], [4, 3, true], [4, 5, true], [3, 1, true], [4, 4, true], [4, 3, true], ".", " ", [3, 1, false], [1, 1, true], [4, 4, true], [1, 5, true], [4, 2, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [2, 2, true], [4, 2, true], [3, 4, true], [4, 5, true], [3, 5, true], " ", [1, 3, true], [3, 4, true], [3, 2, true], [3, 5, true], [1, 1, true], [4, 2, true], [1, 5, true], [4, 3, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [3, 4, true], [4, 2, true], [2, 4, true], [2, 2, true], [2, 4, true], [3, 3, true], [1, 1, true], [3, 1, true], " ", [3, 2, true], [1, 5, true], [4, 3, true], [4, 3, true], [1, 1, true], [2, 2, true], [1, 5, true], " ", [5, 2, true], [2, 4, true], [4, 4, true], [2, 3, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [1, 4, true], [1, 5, true], [1, 3, true], [3, 4, true], [1, 4, true], [1, 5, true], [1, 4, true], " ", [4, 4, true], [1, 5, true], [5, 3, true], [4, 4, true], "."] | At noon the study group meets by the garden. The group tests a model carrier and records the results. Later the group compares the original message with the decoded text. | ok |
| medium | vigenere | At noon the study group meets by the garden. The group tests a model carrier and records the results. Later the group compares the original message with the decoded text. | {'key': 'LAB'} | Lt ozoo ehf dtvoy hcova mfptt my use hlrepn. Use hcova tfdtt l mpoem nascifc aoo rfnosos use spsvwtt. Waupr use hcova cpxpbcet ehf zrjrioll npstlgf hius tip dfnoepd upxu. | At noon the study group meets by the garden. The group tests a model carrier and records the results. Later the group compares the original message with the decoded text. | ok |
| medium | permutation | At noon the study group meets by the garden. The group tests a model carrier and records the results. Later the group compares the original message with the decoded text. | {'key': [2, 0, 3, 1]} |  Antno oet husdtgyr po uemtebsy h eta rgnd.eh eTr og utptess  maeolda rcerrin dae crdosrh ete srtuslL.a rt eet hogurcpo amrp ets hoegriiln asmseea gtwhih ete cdeodde xtt. | At noon the study group meets by the garden. The group tests a model carrier and records the results. Later the group compares the original message with the decoded text. | ok |
| medium | rotor | At noon the study group meets by the garden. The group tests a model carrier and records the results. Later the group compares the original message with the decoded text. | {'offset': 2, 'wiring': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'} | Ky qkut coo uudgh leldf vinwv ki gkr oxvlnh. Adh movcy viblk e uykbv zblvpna ixk sacphiu djn jgshuyx. Sxxgv vhl csqxm ixjsfbov pub reriaaqy gltpslr grcr loo nlevarq dmyd. | At noon the study group meets by the garden. The group tests a model carrier and records the results. Later the group compares the original message with the decoded text. | ok |
| punctuation | caesar | Quiet, lab team! Ready? | {'shift': 3} | Txlhw, ode whdp! Uhdgb? | Quiet, lab team! Ready? | ok |
| punctuation | atbash | Quiet, lab team! Ready? | {} | Jfrvg, ozy gvzn! Ivzwb? | Quiet, lab team! Ready? | ok |
| punctuation | polybius | Quiet, lab team! Ready? | {'aliases': {'J': 'I'}} | [[4, 1, false], [4, 5, true], [2, 4, true], [1, 5, true], [4, 4, true], ",", " ", [3, 1, true], [1, 1, true], [1, 2, true], " ", [4, 4, true], [1, 5, true], [1, 1, true], [3, 2, true], "!", " ", [4, 2, false], [1, 5, true], [1, 1, true], [1, 4, true], [5, 4, true], "?"] | Quiet, lab team! Ready? | ok |
| punctuation | vigenere | Quiet, lab team! Ready? | {'key': 'LAB'} | Bujpt, mlb upan! Ceboy? | Quiet, lab team! Ready? | ok |
| punctuation | permutation | Quiet, lab team! Ready? | {'key': [2, 0, 3, 1]} | iQeu tl, atbme!ae aR?dy | Quiet, lab team! Ready? | ok |
| punctuation | rotor | Quiet, lab team! Ready? | {'offset': 2, 'wiring': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'} | Qokud, lne vwcw! Sahjf? | Quiet, lab team! Ready? | ok |
| repeated | caesar | AAAA BALLOON BALLOON | {'shift': 3} | DDDD EDOORRQ EDOORRQ | AAAA BALLOON BALLOON | ok |
| repeated | atbash | AAAA BALLOON BALLOON | {} | ZZZZ YZOOLLM YZOOLLM | AAAA BALLOON BALLOON | ok |
| repeated | polybius | AAAA BALLOON BALLOON | {'aliases': {'J': 'I'}} | [[1, 1, false], [1, 1, false], [1, 1, false], [1, 1, false], " ", [1, 2, false], [1, 1, false], [3, 1, false], [3, 1, false], [3, 4, false], [3, 4, false], [3, 3, false], " ", [1, 2, false], [1, 1, false], [3, 1, false], [3, 1, false], [3, 4, false], [3, 4, false], [3, 3, false]] | AAAA BALLOON BALLOON | ok |
| repeated | vigenere | AAAA BALLOON BALLOON | {'key': 'LAB'} | LABL BBWLPZN CLLMZOO | AAAA BALLOON BALLOON | ok |
| repeated | permutation | AAAA BALLOON BALLOON | {'key': [2, 0, 3, 1]} | AAAAA LBOLNOA LBOLNO | AAAA BALLOON BALLOON | ok |
| repeated | rotor | AAAA BALLOON BALLOON | {'offset': 2, 'wiring': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'} | KCHB KJHRSYX LKPUPLK | AAAA BALLOON BALLOON | ok |
| rare | caesar | Jazz wax quiz | {'shift': 3} | Mdcc zda txlc | Jazz wax quiz | ok |
| rare | atbash | Jazz wax quiz | {} | Qzaa dzc jfra | Jazz wax quiz | ok |
| rare | polybius | Jazz wax quiz | {'aliases': {'J': 'I'}} | [[2, 4, false], [1, 1, true], [5, 5, true], [5, 5, true], " ", [5, 2, true], [1, 1, true], [5, 3, true], " ", [4, 1, true], [4, 5, true], [2, 4, true], [5, 5, true]] | Iazz wax quiz | ok |
| rare | vigenere | Jazz wax quiz | {'key': 'LAB'} | Uaak wbi qvtz | Jazz wax quiz | ok |
| rare | permutation | Jazz wax quiz | {'key': [2, 0, 3, 1]} | zJzaa xwu iqz | Jazz wax quiz | ok |
| rare | rotor | Jazz wax quiz | {'offset': 2, 'wiring': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'} | Rcbg gjy abeh | Jazz wax quiz | ok |
| russian | caesar | ВСТРЕЧА УЧЕБНОЙ ГРУППЫ В ДЕСЯТЬ ЧАСОВ | {'shift': 3} | ЕФХУЗЪГ ЦЪЗДРСМ ЁУЦТТЮ Е ЖЗФВХЯ ЪГФСЕ | ВСТРЕЧА УЧЕБНОЙ ГРУППЫ В ДЕСЯТЬ ЧАСОВ | ok |
| russian | atbash | ВСТРЕЧА УЧЕБНОЙ ГРУППЫ В ДЕСЯТЬ ЧАСОВ | {} | ЭНМОЪЗЯ ЛЗЪЮСРХ ЬОЛППД Э ЫЪНАМГ ЗЯНРЭ | ВСТРЕЧА УЧЕБНОЙ ГРУППЫ В ДЕСЯТЬ ЧАСОВ | ok |
| russian | polybius | ВСТРЕЧА УЧЕБНОЙ ГРУППЫ В ДЕСЯТЬ ЧАСОВ | {'aliases': {}} | [[1, 3, false], [4, 1, false], [4, 2, false], [3, 6, false], [1, 6, false], [5, 1, false], [1, 1, false], " ", [4, 3, false], [5, 1, false], [1, 6, false], [1, 2, false], [3, 3, false], [3, 4, false], [2, 5, false], " ", [1, 4, false], [3, 6, false], [4, 3, false], [3, 5, false], [3, 5, false], [5, 5, false], " ", [1, 3, false], " ", [1, 5, false], [1, 6, false], [4, 1, false], [6, 3, false], [4, 2, false], [5, 6, false], " ", [5, 1, false], [1, 1, false], [4, 1, false], [3, 4, false], [1, 3, false]] | ВСТРЕЧА УЧЕБНОЙ ГРУППЫ В ДЕСЯТЬ ЧАСОВ | ok |
| russian | vigenere | ВСТРЕЧА УЧЕБНОЙ ГРУППЫ В ДЕСЯТЬ ЧАСОВ | {'key': 'КЛЮЧ'} | МЭРЗПГЮ КВРЯЕЩХ БЗЮЫНТ М ПГИЙЮЪ ОКЭМЩ | ВСТРЕЧА УЧЕБНОЙ ГРУППЫ В ДЕСЯТЬ ЧАСОВ | ok |
| russian | permutation | ВСТРЕЧА УЧЕБНОЙ ГРУППЫ В ДЕСЯТЬ ЧАСОВ | {'key': [2, 0, 3, 1]} | ТВРСАЕ ЧЕУБЧЙН ОУГПР ПВЫЕ СДЬЯ ТСЧОАВ | ВСТРЕЧА УЧЕБНОЙ ГРУППЫ В ДЕСЯТЬ ЧАСОВ | ok |
| russian | rotor | ВСТРЕЧА УЧЕБНОЙ ГРУППЫ В ДЕСЯТЬ ЧАСОВ | {'offset': 2, 'wiring': 'ИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯЗЖЁЕДГВБА'} | КЪЫЩНЪИ ЪАНЙШХШ ЛЩЬШШД Т ОЛЪНЫМ АЕЪЧК | ВСТРЕЧА УЧЕБНОЙ ГРУППЫ В ДЕСЯТЬ ЧАСОВ | ok |
| latin | caesar | A fictional signal. | {'shift': 3} | D ilfwlrqdo vljqdo. | A fictional signal. | ok |
| latin | atbash | A fictional signal. | {} | Z urxgrlmzo hrtmzo. | A fictional signal. | ok |
| latin | polybius | A fictional signal. | {'aliases': {'J': 'I'}} | [[1, 1, false], " ", [2, 1, true], [2, 4, true], [1, 3, true], [4, 4, true], [2, 4, true], [3, 4, true], [3, 3, true], [1, 1, true], [3, 1, true], " ", [4, 3, true], [2, 4, true], [2, 2, true], [3, 3, true], [1, 1, true], [3, 1, true], "."] | A fictional signal. | ok |
| latin | vigenere | A fictional signal. | {'key': 'LAB'} | L fjntjznbw sjrnbw. | A fictional signal. | ok |
| latin | permutation | A fictional signal. | {'key': [2, 0, 3, 1]} | fAi icotln agsni.al | A fictional signal. | ok |
| latin | rotor | A fictional signal. | {'offset': 2, 'wiring': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'} | K skldatsdq zvmxhv. | A fictional signal. | ok |
| digits | caesar | КОД 42, ЭТАП 7. | {'shift': 3} | НСЖ 42, АХГТ 7. | КОД 42, ЭТАП 7. | ok |
| digits | atbash | КОД 42, ЭТАП 7. | {} | ФРЫ 42, ВМЯП 7. | КОД 42, ЭТАП 7. | ok |
| digits | polybius | КОД 42, ЭТАП 7. | {'aliases': {}} | [[2, 6, false], [3, 4, false], [1, 5, false], " ", "4", "2", ",", " ", [6, 1, false], [4, 2, false], [1, 1, false], [3, 5, false], " ", "7", "."] | КОД 42, ЭТАП 7. | ok |
| digits | vigenere | КОД 42, ЭТАП 7. | {'key': 'КЛЮЧ'} | ХЪВ 42, ФЭЛН 7. | КОД 42, ЭТАП 7. | ok |
| digits | permutation | КОД 42, ЭТАП 7. | {'key': [2, 0, 3, 1]} | ДК О,4 2АЭПТ. 7 | КОД 42, ЭТАП 7. | ok |
| digits | rotor | КОД 42, ЭТАП 7. | {'offset': 2, 'wiring': 'ИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯЗЖЁЕДГВБА'} | УЧМ 42, ЁБИА 7. | КОД 42, ЭТАП 7. | ok |
| long | caesar | At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message.At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message. | {'shift': 3} | Dw qrrq wkh vwxgb jurxs uhfrugv lwv revhuydwlrqv lq d vkduhg qrwherrn. Wkh fodvv fkdqjhv wkh duudqjhphqw ri ohwwhuv dqg fkhfnv zkhwkhu wkh ruljlqdo whaw fdq eh uhfryhuhg. Hdfk vpdoo hashulphqw surylghv hylghqfh derxw d surshuwb ri wkh prgho. Wkh uhvxowv iurp wkh suhylrxv hahuflvh duh frpsduhg zlwk wkh rxwsxw ri wkh qhz hahuflvh. Wkh ilfwlrqdo whdp revhuyhv zklfk ohwwhuv rffxu prvw riwhq lq d orqj sdvvdjh. Wkh lqvwuxfwru wkhq dvnv wkh whdpv wr frpsduh wkh ghfrghg qrwhv zlwk wkh ruljlqdov. Wkh vwxgb jurxs glvfxvvhv zkdw dq revhuyhu frxog ohduq iurp d sdwwhuq lq d phvvdjh.Dw qrrq wkh vwxgb jurxs uhfrugv lwv revhuydwlrqv lq d vkduhg qrwherrn. Wkh fodvv fkdqjhv wkh duudqjhphqw ri ohwwhuv dqg fkhfnv zkhwkhu wkh ruljlqdo whaw fdq eh uhfryhuhg. Hdfk vpdoo hashulphqw surylghv hylghqfh derxw d surshuwb ri wkh prgho. Wkh uhvxowv iurp wkh suhylrxv hahuflvh duh frpsduhg zlwk wkh rxwsxw ri wkh qhz hahuflvh. Wkh ilfwlrqdo whdp revhuyhv zklfk ohwwhuv rffxu prvw riwhq lq d orqj sdvvdjh. Wkh lqvwuxfwru wkhq dvnv wkh whdpv wr frpsduh wkh ghfrghg qrwhv zlwk wkh ruljlqdov. Wkh vwxgb jurxs glvfxvvhv zkdw dq revhuyhu frxog ohduq iurp d sdwwhuq lq d phvvdjh. | At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message.At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message. | ok |
| long | atbash | At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message.At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message. | {} | Zg mllm gsv hgfwb tilfk ivxliwh rgh lyhviezgrlmh rm z hszivw mlgvyllp. Gsv xozhh xszmtvh gsv ziizmtvnvmg lu ovggvih zmw xsvxph dsvgsvi gsv lirtrmzo gvcg xzm yv ivxlevivw. Vzxs hnzoo vckvirnvmg kilerwvh verwvmxv zylfg z kilkvigb lu gsv nlwvo. Gsv ivhfogh uiln gsv kiverlfh vcvixrhv ziv xlnkzivw drgs gsv lfgkfg lu gsv mvd vcvixrhv. Gsv urxgrlmzo gvzn lyhvievh dsrxs ovggvih lxxfi nlhg lugvm rm z olmt kzhhztv. Gsv rmhgifxgli gsvm zhph gsv gvznh gl xlnkziv gsv wvxlwvw mlgvh drgs gsv lirtrmzoh. Gsv hgfwb tilfk wrhxfhhvh dszg zm lyhvievi xlfow ovzim uiln z kzggvim rm z nvhhztv.Zg mllm gsv hgfwb tilfk ivxliwh rgh lyhviezgrlmh rm z hszivw mlgvyllp. Gsv xozhh xszmtvh gsv ziizmtvnvmg lu ovggvih zmw xsvxph dsvgsvi gsv lirtrmzo gvcg xzm yv ivxlevivw. Vzxs hnzoo vckvirnvmg kilerwvh verwvmxv zylfg z kilkvigb lu gsv nlwvo. Gsv ivhfogh uiln gsv kiverlfh vcvixrhv ziv xlnkzivw drgs gsv lfgkfg lu gsv mvd vcvixrhv. Gsv urxgrlmzo gvzn lyhvievh dsrxs ovggvih lxxfi nlhg lugvm rm z olmt kzhhztv. Gsv rmhgifxgli gsvm zhph gsv gvznh gl xlnkziv gsv wvxlwvw mlgvh drgs gsv lirtrmzoh. Gsv hgfwb tilfk wrhxfhhvh dszg zm lyhvievi xlfow ovzim uiln z kzggvim rm z nvhhztv. | At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message.At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message. | ok |
| long | polybius | At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message.At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message. | {'aliases': {'J': 'I'}} | [[1, 1, false], [4, 4, true], " ", [3, 3, true], [3, 4, true], [3, 4, true], [3, 3, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [4, 3, true], [4, 4, true], [4, 5, true], [1, 4, true], [5, 4, true], " ", [2, 2, true], [4, 2, true], [3, 4, true], [4, 5, true], [3, 5, true], " ", [4, 2, true], [1, 5, true], [1, 3, true], [3, 4, true], [4, 2, true], [1, 4, true], [4, 3, true], " ", [2, 4, true], [4, 4, true], [4, 3, true], " ", [3, 4, true], [1, 2, true], [4, 3, true], [1, 5, true], [4, 2, true], [5, 1, true], [1, 1, true], [4, 4, true], [2, 4, true], [3, 4, true], [3, 3, true], [4, 3, true], " ", [2, 4, true], [3, 3, true], " ", [1, 1, true], " ", [4, 3, true], [2, 3, true], [1, 1, true], [4, 2, true], [1, 5, true], [1, 4, true], " ", [3, 3, true], [3, 4, true], [4, 4, true], [1, 5, true], [1, 2, true], [3, 4, true], [3, 4, true], [2, 5, true], ".", " ", [4, 4, false], [2, 3, true], [1, 5, true], " ", [1, 3, true], [3, 1, true], [1, 1, true], [4, 3, true], [4, 3, true], " ", [1, 3, true], [2, 3, true], [1, 1, true], [3, 3, true], [2, 2, true], [1, 5, true], [4, 3, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [1, 1, true], [4, 2, true], [4, 2, true], [1, 1, true], [3, 3, true], [2, 2, true], [1, 5, true], [3, 2, true], [1, 5, true], [3, 3, true], [4, 4, true], " ", [3, 4, true], [2, 1, true], " ", [3, 1, true], [1, 5, true], [4, 4, true], [4, 4, true], [1, 5, true], [4, 2, true], [4, 3, true], " ", [1, 1, true], [3, 3, true], [1, 4, true], " ", [1, 3, true], [2, 3, true], [1, 5, true], [1, 3, true], [2, 5, true], [4, 3, true], " ", [5, 2, true], [2, 3, true], [1, 5, true], [4, 4, true], [2, 3, true], [1, 5, true], [4, 2, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [3, 4, true], [4, 2, true], [2, 4, true], [2, 2, true], [2, 4, true], [3, 3, true], [1, 1, true], [3, 1, true], " ", [4, 4, true], [1, 5, true], [5, 3, true], [4, 4, true], " ", [1, 3, true], [1, 1, true], [3, 3, true], " ", [1, 2, true], [1, 5, true], " ", [4, 2, true], [1, 5, true], [1, 3, true], [3, 4, true], [5, 1, true], [1, 5, true], [4, 2, true], [1, 5, true], [1, 4, true], ".", " ", [1, 5, false], [1, 1, true], [1, 3, true], [2, 3, true], " ", [4, 3, true], [3, 2, true], [1, 1, true], [3, 1, true], [3, 1, true], " ", [1, 5, true], [5, 3, true], [3, 5, true], [1, 5, true], [4, 2, true], [2, 4, true], [3, 2, true], [1, 5, true], [3, 3, true], [4, 4, true], " ", [3, 5, true], [4, 2, true], [3, 4, true], [5, 1, true], [2, 4, true], [1, 4, true], [1, 5, true], [4, 3, true], " ", [1, 5, true], [5, 1, true], [2, 4, true], [1, 4, true], [1, 5, true], [3, 3, true], [1, 3, true], [1, 5, true], " ", [1, 1, true], [1, 2, true], [3, 4, true], [4, 5, true], [4, 4, true], " ", [1, 1, true], " ", [3, 5, true], [4, 2, true], [3, 4, true], [3, 5, true], [1, 5, true], [4, 2, true], [4, 4, true], [5, 4, true], " ", [3, 4, true], [2, 1, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [3, 2, true], [3, 4, true], [1, 4, true], [1, 5, true], [3, 1, true], ".", " ", [4, 4, false], [2, 3, true], [1, 5, true], " ", [4, 2, true], [1, 5, true], [4, 3, true], [4, 5, true], [3, 1, true], [4, 4, true], [4, 3, true], " ", [2, 1, true], [4, 2, true], [3, 4, true], [3, 2, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [3, 5, true], [4, 2, true], [1, 5, true], [5, 1, true], [2, 4, true], [3, 4, true], [4, 5, true], [4, 3, true], " ", [1, 5, true], [5, 3, true], [1, 5, true], [4, 2, true], [1, 3, true], [2, 4, true], [4, 3, true], [1, 5, true], " ", [1, 1, true], [4, 2, true], [1, 5, true], " ", [1, 3, true], [3, 4, true], [3, 2, true], [3, 5, true], [1, 1, true], [4, 2, true], [1, 5, true], [1, 4, true], " ", [5, 2, true], [2, 4, true], [4, 4, true], [2, 3, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [3, 4, true], [4, 5, true], [4, 4, true], [3, 5, true], [4, 5, true], [4, 4, true], " ", [3, 4, true], [2, 1, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [3, 3, true], [1, 5, true], [5, 2, true], " ", [1, 5, true], [5, 3, true], [1, 5, true], [4, 2, true], [1, 3, true], [2, 4, true], [4, 3, true], [1, 5, true], ".", " ", [4, 4, false], [2, 3, true], [1, 5, true], " ", [2, 1, true], [2, 4, true], [1, 3, true], [4, 4, true], [2, 4, true], [3, 4, true], [3, 3, true], [1, 1, true], [3, 1, true], " ", [4, 4, true], [1, 5, true], [1, 1, true], [3, 2, true], " ", [3, 4, true], [1, 2, true], [4, 3, true], [1, 5, true], [4, 2, true], [5, 1, true], [1, 5, true], [4, 3, true], " ", [5, 2, true], [2, 3, true], [2, 4, true], [1, 3, true], [2, 3, true], " ", [3, 1, true], [1, 5, true], [4, 4, true], [4, 4, true], [1, 5, true], [4, 2, true], [4, 3, true], " ", [3, 4, true], [1, 3, true], [1, 3, true], [4, 5, true], [4, 2, true], " ", [3, 2, true], [3, 4, true], [4, 3, true], [4, 4, true], " ", [3, 4, true], [2, 1, true], [4, 4, true], [1, 5, true], [3, 3, true], " ", [2, 4, true], [3, 3, true], " ", [1, 1, true], " ", [3, 1, true], [3, 4, true], [3, 3, true], [2, 2, true], " ", [3, 5, true], [1, 1, true], [4, 3, true], [4, 3, true], [1, 1, true], [2, 2, true], [1, 5, true], ".", " ", [4, 4, false], [2, 3, true], [1, 5, true], " ", [2, 4, true], [3, 3, true], [4, 3, true], [4, 4, true], [4, 2, true], [4, 5, true], [1, 3, true], [4, 4, true], [3, 4, true], [4, 2, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], [3, 3, true], " ", [1, 1, true], [4, 3, true], [2, 5, true], [4, 3, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [4, 4, true], [1, 5, true], [1, 1, true], [3, 2, true], [4, 3, true], " ", [4, 4, true], [3, 4, true], " ", [1, 3, true], [3, 4, true], [3, 2, true], [3, 5, true], [1, 1, true], [4, 2, true], [1, 5, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [1, 4, true], [1, 5, true], [1, 3, true], [3, 4, true], [1, 4, true], [1, 5, true], [1, 4, true], " ", [3, 3, true], [3, 4, true], [4, 4, true], [1, 5, true], [4, 3, true], " ", [5, 2, true], [2, 4, true], [4, 4, true], [2, 3, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [3, 4, true], [4, 2, true], [2, 4, true], [2, 2, true], [2, 4, true], [3, 3, true], [1, 1, true], [3, 1, true], [4, 3, true], ".", " ", [4, 4, false], [2, 3, true], [1, 5, true], " ", [4, 3, true], [4, 4, true], [4, 5, true], [1, 4, true], [5, 4, true], " ", [2, 2, true], [4, 2, true], [3, 4, true], [4, 5, true], [3, 5, true], " ", [1, 4, true], [2, 4, true], [4, 3, true], [1, 3, true], [4, 5, true], [4, 3, true], [4, 3, true], [1, 5, true], [4, 3, true], " ", [5, 2, true], [2, 3, true], [1, 1, true], [4, 4, true], " ", [1, 1, true], [3, 3, true], " ", [3, 4, true], [1, 2, true], [4, 3, true], [1, 5, true], [4, 2, true], [5, 1, true], [1, 5, true], [4, 2, true], " ", [1, 3, true], [3, 4, true], [4, 5, true], [3, 1, true], [1, 4, true], " ", [3, 1, true], [1, 5, true], [1, 1, true], [4, 2, true], [3, 3, true], " ", [2, 1, true], [4, 2, true], [3, 4, true], [3, 2, true], " ", [1, 1, true], " ", [3, 5, true], [1, 1, true], [4, 4, true], [4, 4, true], [1, 5, true], [4, 2, true], [3, 3, true], " ", [2, 4, true], [3, 3, true], " ", [1, 1, true], " ", [3, 2, true], [1, 5, true], [4, 3, true], [4, 3, true], [1, 1, true], [2, 2, true], [1, 5, true], ".", [1, 1, false], [4, 4, true], " ", [3, 3, true], [3, 4, true], [3, 4, true], [3, 3, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [4, 3, true], [4, 4, true], [4, 5, true], [1, 4, true], [5, 4, true], " ", [2, 2, true], [4, 2, true], [3, 4, true], [4, 5, true], [3, 5, true], " ", [4, 2, true], [1, 5, true], [1, 3, true], [3, 4, true], [4, 2, true], [1, 4, true], [4, 3, true], " ", [2, 4, true], [4, 4, true], [4, 3, true], " ", [3, 4, true], [1, 2, true], [4, 3, true], [1, 5, true], [4, 2, true], [5, 1, true], [1, 1, true], [4, 4, true], [2, 4, true], [3, 4, true], [3, 3, true], [4, 3, true], " ", [2, 4, true], [3, 3, true], " ", [1, 1, true], " ", [4, 3, true], [2, 3, true], [1, 1, true], [4, 2, true], [1, 5, true], [1, 4, true], " ", [3, 3, true], [3, 4, true], [4, 4, true], [1, 5, true], [1, 2, true], [3, 4, true], [3, 4, true], [2, 5, true], ".", " ", [4, 4, false], [2, 3, true], [1, 5, true], " ", [1, 3, true], [3, 1, true], [1, 1, true], [4, 3, true], [4, 3, true], " ", [1, 3, true], [2, 3, true], [1, 1, true], [3, 3, true], [2, 2, true], [1, 5, true], [4, 3, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [1, 1, true], [4, 2, true], [4, 2, true], [1, 1, true], [3, 3, true], [2, 2, true], [1, 5, true], [3, 2, true], [1, 5, true], [3, 3, true], [4, 4, true], " ", [3, 4, true], [2, 1, true], " ", [3, 1, true], [1, 5, true], [4, 4, true], [4, 4, true], [1, 5, true], [4, 2, true], [4, 3, true], " ", [1, 1, true], [3, 3, true], [1, 4, true], " ", [1, 3, true], [2, 3, true], [1, 5, true], [1, 3, true], [2, 5, true], [4, 3, true], " ", [5, 2, true], [2, 3, true], [1, 5, true], [4, 4, true], [2, 3, true], [1, 5, true], [4, 2, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [3, 4, true], [4, 2, true], [2, 4, true], [2, 2, true], [2, 4, true], [3, 3, true], [1, 1, true], [3, 1, true], " ", [4, 4, true], [1, 5, true], [5, 3, true], [4, 4, true], " ", [1, 3, true], [1, 1, true], [3, 3, true], " ", [1, 2, true], [1, 5, true], " ", [4, 2, true], [1, 5, true], [1, 3, true], [3, 4, true], [5, 1, true], [1, 5, true], [4, 2, true], [1, 5, true], [1, 4, true], ".", " ", [1, 5, false], [1, 1, true], [1, 3, true], [2, 3, true], " ", [4, 3, true], [3, 2, true], [1, 1, true], [3, 1, true], [3, 1, true], " ", [1, 5, true], [5, 3, true], [3, 5, true], [1, 5, true], [4, 2, true], [2, 4, true], [3, 2, true], [1, 5, true], [3, 3, true], [4, 4, true], " ", [3, 5, true], [4, 2, true], [3, 4, true], [5, 1, true], [2, 4, true], [1, 4, true], [1, 5, true], [4, 3, true], " ", [1, 5, true], [5, 1, true], [2, 4, true], [1, 4, true], [1, 5, true], [3, 3, true], [1, 3, true], [1, 5, true], " ", [1, 1, true], [1, 2, true], [3, 4, true], [4, 5, true], [4, 4, true], " ", [1, 1, true], " ", [3, 5, true], [4, 2, true], [3, 4, true], [3, 5, true], [1, 5, true], [4, 2, true], [4, 4, true], [5, 4, true], " ", [3, 4, true], [2, 1, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [3, 2, true], [3, 4, true], [1, 4, true], [1, 5, true], [3, 1, true], ".", " ", [4, 4, false], [2, 3, true], [1, 5, true], " ", [4, 2, true], [1, 5, true], [4, 3, true], [4, 5, true], [3, 1, true], [4, 4, true], [4, 3, true], " ", [2, 1, true], [4, 2, true], [3, 4, true], [3, 2, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [3, 5, true], [4, 2, true], [1, 5, true], [5, 1, true], [2, 4, true], [3, 4, true], [4, 5, true], [4, 3, true], " ", [1, 5, true], [5, 3, true], [1, 5, true], [4, 2, true], [1, 3, true], [2, 4, true], [4, 3, true], [1, 5, true], " ", [1, 1, true], [4, 2, true], [1, 5, true], " ", [1, 3, true], [3, 4, true], [3, 2, true], [3, 5, true], [1, 1, true], [4, 2, true], [1, 5, true], [1, 4, true], " ", [5, 2, true], [2, 4, true], [4, 4, true], [2, 3, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [3, 4, true], [4, 5, true], [4, 4, true], [3, 5, true], [4, 5, true], [4, 4, true], " ", [3, 4, true], [2, 1, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [3, 3, true], [1, 5, true], [5, 2, true], " ", [1, 5, true], [5, 3, true], [1, 5, true], [4, 2, true], [1, 3, true], [2, 4, true], [4, 3, true], [1, 5, true], ".", " ", [4, 4, false], [2, 3, true], [1, 5, true], " ", [2, 1, true], [2, 4, true], [1, 3, true], [4, 4, true], [2, 4, true], [3, 4, true], [3, 3, true], [1, 1, true], [3, 1, true], " ", [4, 4, true], [1, 5, true], [1, 1, true], [3, 2, true], " ", [3, 4, true], [1, 2, true], [4, 3, true], [1, 5, true], [4, 2, true], [5, 1, true], [1, 5, true], [4, 3, true], " ", [5, 2, true], [2, 3, true], [2, 4, true], [1, 3, true], [2, 3, true], " ", [3, 1, true], [1, 5, true], [4, 4, true], [4, 4, true], [1, 5, true], [4, 2, true], [4, 3, true], " ", [3, 4, true], [1, 3, true], [1, 3, true], [4, 5, true], [4, 2, true], " ", [3, 2, true], [3, 4, true], [4, 3, true], [4, 4, true], " ", [3, 4, true], [2, 1, true], [4, 4, true], [1, 5, true], [3, 3, true], " ", [2, 4, true], [3, 3, true], " ", [1, 1, true], " ", [3, 1, true], [3, 4, true], [3, 3, true], [2, 2, true], " ", [3, 5, true], [1, 1, true], [4, 3, true], [4, 3, true], [1, 1, true], [2, 2, true], [1, 5, true], ".", " ", [4, 4, false], [2, 3, true], [1, 5, true], " ", [2, 4, true], [3, 3, true], [4, 3, true], [4, 4, true], [4, 2, true], [4, 5, true], [1, 3, true], [4, 4, true], [3, 4, true], [4, 2, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], [3, 3, true], " ", [1, 1, true], [4, 3, true], [2, 5, true], [4, 3, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [4, 4, true], [1, 5, true], [1, 1, true], [3, 2, true], [4, 3, true], " ", [4, 4, true], [3, 4, true], " ", [1, 3, true], [3, 4, true], [3, 2, true], [3, 5, true], [1, 1, true], [4, 2, true], [1, 5, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [1, 4, true], [1, 5, true], [1, 3, true], [3, 4, true], [1, 4, true], [1, 5, true], [1, 4, true], " ", [3, 3, true], [3, 4, true], [4, 4, true], [1, 5, true], [4, 3, true], " ", [5, 2, true], [2, 4, true], [4, 4, true], [2, 3, true], " ", [4, 4, true], [2, 3, true], [1, 5, true], " ", [3, 4, true], [4, 2, true], [2, 4, true], [2, 2, true], [2, 4, true], [3, 3, true], [1, 1, true], [3, 1, true], [4, 3, true], ".", " ", [4, 4, false], [2, 3, true], [1, 5, true], " ", [4, 3, true], [4, 4, true], [4, 5, true], [1, 4, true], [5, 4, true], " ", [2, 2, true], [4, 2, true], [3, 4, true], [4, 5, true], [3, 5, true], " ", [1, 4, true], [2, 4, true], [4, 3, true], [1, 3, true], [4, 5, true], [4, 3, true], [4, 3, true], [1, 5, true], [4, 3, true], " ", [5, 2, true], [2, 3, true], [1, 1, true], [4, 4, true], " ", [1, 1, true], [3, 3, true], " ", [3, 4, true], [1, 2, true], [4, 3, true], [1, 5, true], [4, 2, true], [5, 1, true], [1, 5, true], [4, 2, true], " ", [1, 3, true], [3, 4, true], [4, 5, true], [3, 1, true], [1, 4, true], " ", [3, 1, true], [1, 5, true], [1, 1, true], [4, 2, true], [3, 3, true], " ", [2, 1, true], [4, 2, true], [3, 4, true], [3, 2, true], " ", [1, 1, true], " ", [3, 5, true], [1, 1, true], [4, 4, true], [4, 4, true], [1, 5, true], [4, 2, true], [3, 3, true], " ", [2, 4, true], [3, 3, true], " ", [1, 1, true], " ", [3, 2, true], [1, 5, true], [4, 3, true], [4, 3, true], [1, 1, true], [2, 2, true], [1, 5, true], "."] | At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message.At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message. | ok |
| long | vigenere | At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message.At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message. | {'key': 'LAB'} | Lt ozoo ehf dtvoy hcova rfnosos jes pmsfcvbeipys jy a tsaspd oztfmopv. Tip cmlst nhbygfd tip ascaorenpnu zf mptuprt lne nhfnkt hhfehfc tip ostgjyam eeye cby bf cedzvfcee. Pads snllm pxqprjxeoe pszvjoet pvjoeone bmove a qcoqpruj og ehf xoepl. Use spsvwtt qrpx tip pspvjzut pxfccjde bce dzmqlrfo wjeh use pftqft pq tip nfh eyprdtsf. Ehf qideipyam eebx ocdesget hhjnh mptuprt zcdfr nzsu zfupn jy a mznh aatdahp. Tip iodtsfcuzr useo lsld tip tflmt eo dzmqlrf ehf oedzdfo npeet hius tip ostgjyamd. Tip sufdz rrpfp etsdfstps xsau ln pmsfcvfc cpfle webcn gcon l pbetfcn jy a npstlgf.Lt ozoo ehf dtvoy hcova rfnosos jes pmsfcvbeipys jy a tsaspd oztfmopv. Tip cmlst nhbygfd tip ascaorenpnu zf mptuprt lne nhfnkt hhfehfc tip ostgjyam eeye cby bf cedzvfcee. Pads snllm pxqprjxeoe pszvjoet pvjoeone bmove a qcoqpruj og ehf xoepl. Use spsvwtt qrpx tip pspvjzut pxfccjde bce dzmqlrfo wjeh use pftqft pq tip nfh eyprdtsf. Ehf qideipyam eebx ocdesget hhjnh mptuprt zcdfr nzsu zfupn jy a mznh aatdahp. Tip iodtsfcuzr useo lsld tip tflmt eo dzmqlrf ehf oedzdfo npeet hius tip ostgjyamd. Tip sufdz rrpfp etsdfstps xsau ln pmsfcvfc cpfle webcn gcon l pbetfcn jy a npstlgf. | At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message.At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message. | ok |
| long | permutation | At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message.At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message. | {'key': [2, 0, 3, 1]} |  Antno oet husdtgyr po ucroesr dsi tsoebartvnison  isah eadro tnoeob kT. hceslsah acensgh etr ragaennmtef  otltese rda necch kwsthhe etr hoegriiln axttea nce  bcroervee dE.ha caslmelx rpienmter opdveiesv eind caeubto  papreoyr t otf hmeeoldT.h ree lstufsr  otm hpevrieso ueerxsceir eao mcrpeawdi  tth hoepuutotf h ete wnx eeirsc eT. hfetiicaolne atomb rsve ewschhie tlrtsec co umrto stoefinn   lago nspsaea.gh eTn siutcrrt oetnhs katsh tee sa m tcopoam rte hdeoedc endeosti twthh oer iingsa.lh eTt us dgyurpoi sdscsu ewsth a aonebrsrv euclolde na rofmr  pataet rinan  smseea.g Antno oet husdtgyr po ucroesr dsi tsoebartvnison  isah eadro tnoeob kT. hceslsah acensgh etr ragaennmtef  otltese rda necch kwsthhe etr hoegriiln axttea nce  bcroervee dE.ha caslmelx rpienmter opdveiesv eind caeubto  papreoyr t otf hmeeoldT.h ree lstufsr  otm hpevrieso ueerxsceir eao mcrpeawdi  tth hoepuutotf h ete wnx eeirsc eT. hfetiicaolne atomb rsve ewschhie tlrtsec co umrto stoefinn   lago nspsaea.gh eTn siutcrrt oetnhs katsh tee sa m tcopoam rte hdeoedc endeosti twthh oer iingsa.lh eTt us dgyurpoi sdscsu ewsth a aonebrsrv euclolde na rofmr  pataet rinan  smseea.g | At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message.At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message. | ok |
| long | rotor | At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message.At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message. | {'offset': 2, 'wiring': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'} | Ky qkut coo uudgh leldf timqyfo lyx kkcgvwiuvyxf so w urfbon wggnckun. Coo lfjpb clakkoc aig erncqohigsv yi pegjrha gan migmsy gpudrgv vhl xsclsowm didw lex dn eupbxnawv. Hkfb itwmi idyguywnqx cvtcinlt eymjjkho ffqqp j sxovhvch sm une vvjjs. Cri bovangf vwui coo tthlcvcv yaoamfvl jnn zkmunvon jvcm jlj xedxxw xg zxn qug mynalote. Gbr zrhdpwvkt zbct kkcgvwwz muccl nycdibz xmezx tkwx tpvwx vw s upoq fnckehl. Zxn knwxbweasy cmku aarb loo tljwf nk pbstdbl qua zrixxon qqtlo aqnj drg iaegvwsui. Bli blxms drvol qscfwcult zmhw ak bgcnjblr jryst lgqar iyyv h mavcoaq fp e vbfxbim.Nd hysr cmk ibdxu qbqqh rbdowtc pdc ykteoddbrbac jv k sukxrq jbcnjyse. Cmk ynwub goepdfy ypu xvbqhjlwexj pz sidlnjv exe dpupnw xkwuneo jlj xzkqjvkt zbbn lxt rn awmxlaarq. Ygwj kpktn bblulasnha yyyymjja icphopmf kioed j jvstlych vk bli vrhoo. Pub xrmylcb xbsw cmk mhynkrxz grfndkmh jbn eyqzkokj grcr loo xazson kn xzn hwj hfaaymai. Djn hrmzlrqbo xgqr ykteodrv oqkgo bgpzbxx kpsev ryzq yljro rw n uwvh hjyfhoh. Xzn irzqskcwlu criq evno gkr xhjsb vy mxqwhej vqo nngxffe uoxhc dlvh une qaskrwnuk. Wel ogoma ivtwz notjkfija drfa ep ylynezhv fibqv pesau zubv f retpfnu kn x igbcigh. | At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message.At noon the study group records its observations in a shared notebook. The class changes the arrangement of letters and checks whether the original text can be recovered. Each small experiment provides evidence about a property of the model. The results from the previous exercise are compared with the output of the new exercise. The fictional team observes which letters occur most often in a long passage. The instructor then asks the teams to compare the decoded notes with the originals. The study group discusses what an observer could learn from a pattern in a message. | ok |

## Криптоанализ

### short · 13 символов

- **original** — E 2 (20.0%), N 2 (20.0%), O 2 (20.0%), T 2 (20.0%), A 1 (10.0%), M 1 (10.0%)

- **caesar** — H 2 (20.0%), Q 2 (20.0%), R 2 (20.0%), W 2 (20.0%), D 1 (10.0%), P 1 (10.0%)

- **atbash** — G 2 (20.0%), L 2 (20.0%), M 2 (20.0%), V 2 (20.0%), N 1 (10.0%), Z 1 (10.0%)

- **vigenere** — E 2 (20.0%), Y 2 (20.0%), A 1 (10.0%), F 1 (10.0%), O 1 (10.0%), P 1 (10.0%), U 1 (10.0%), X 1 (10.0%)

| Сдвиг | Расшифровка | Баллы |
| --- | --- | --- |
| 3 | Meet at noon. | 3 |
| 0 | Phhw dw qrrq. | 0 |
| 1 | Oggv cv pqqp. | 0 |
| 2 | Nffu bu oppo. | 0 |
| 4 | Ldds zs mnnm. | 0 |
| 5 | Kccr yr lmml. | 0 |
| 6 | Jbbq xq kllk. | 0 |
| 7 | Iaap wp jkkj. | 0 |
| 8 | Hzzo vo ijji. | 0 |
| 9 | Gyyn un hiih. | 0 |
| 10 | Fxxm tm ghhg. | 0 |
| 11 | Ewwl sl fggf. | 0 |
| 12 | Dvvk rk effe. | 0 |
| 13 | Cuuj qj deed. | 0 |
| 14 | Btti pi cddc. | 0 |
| 15 | Assh oh bccb. | 0 |
| 16 | Zrrg ng abba. | 0 |
| 17 | Yqqf mf zaaz. | 0 |
| 18 | Xppe le yzzy. | 0 |
| 19 | Wood kd xyyx. | 0 |
| 20 | Vnnc jc wxxw. | 0 |
| 21 | Ummb ib vwwv. | 0 |
| 22 | Tlla ha uvvu. | 0 |
| 23 | Skkz gz tuut. | 0 |
| 24 | Rjjy fy stts. | 0 |
| 25 | Qiix ex rssr. | 0 |

### medium · 170 символов

- **original** — E 22 (15.9%), T 17 (12.3%), R 13 (9.4%), O 10 (7.2%), S 10 (7.2%), A 9 (6.5%), D 8 (5.8%), H 8 (5.8%), G 6 (4.3%), N 5 (3.6%), U 5 (3.6%), C 4 (2.9%), I 4 (2.9%), L 4 (2.9%), M 4 (2.9%), P 4 (2.9%), Y 2 (1.4%), B 1 (0.7%), W 1 (0.7%), X 1 (0.7%)

- **caesar** — H 22 (15.9%), W 17 (12.3%), U 13 (9.4%), R 10 (7.2%), V 10 (7.2%), D 9 (6.5%), G 8 (5.8%), K 8 (5.8%), J 6 (4.3%), Q 5 (3.6%), X 5 (3.6%), F 4 (2.9%), L 4 (2.9%), O 4 (2.9%), P 4 (2.9%), S 4 (2.9%), B 2 (1.4%), A 1 (0.7%), E 1 (0.7%), Z 1 (0.7%)

- **atbash** — V 22 (15.9%), G 17 (12.3%), I 13 (9.4%), H 10 (7.2%), L 10 (7.2%), Z 9 (6.5%), S 8 (5.8%), W 8 (5.8%), T 6 (4.3%), F 5 (3.6%), M 5 (3.6%), K 4 (2.9%), N 4 (2.9%), O 4 (2.9%), R 4 (2.9%), X 4 (2.9%), B 2 (1.4%), C 1 (0.7%), D 1 (0.7%), Y 1 (0.7%)

- **vigenere** — O 14 (10.1%), T 12 (8.7%), P 11 (8.0%), S 11 (8.0%), E 10 (7.2%), F 8 (5.8%), U 8 (5.8%), C 7 (5.1%), H 7 (5.1%), A 6 (4.3%), L 6 (4.3%), N 5 (3.6%), R 5 (3.6%), V 5 (3.6%), D 4 (2.9%), I 4 (2.9%), M 4 (2.9%), W 2 (1.4%), X 2 (1.4%), Y 2 (1.4%), Z 2 (1.4%), B 1 (0.7%), G 1 (0.7%), J 1 (0.7%)

### long · 1152 символов

- **original** — E 146 (15.4%), T 100 (10.5%), O 76 (8.0%), S 76 (8.0%), R 72 (7.6%), A 66 (7.0%), H 54 (5.7%), N 52 (5.5%), I 44 (4.6%), C 42 (4.4%), D 30 (3.2%), L 26 (2.7%), U 26 (2.7%), M 24 (2.5%), P 24 (2.5%), G 18 (1.9%), F 14 (1.5%), V 14 (1.5%), B 12 (1.3%), W 12 (1.3%), X 8 (0.8%), K 6 (0.6%), Y 6 (0.6%)

- **caesar** — H 146 (15.4%), W 100 (10.5%), R 76 (8.0%), V 76 (8.0%), U 72 (7.6%), D 66 (7.0%), K 54 (5.7%), Q 52 (5.5%), L 44 (4.6%), F 42 (4.4%), G 30 (3.2%), O 26 (2.7%), X 26 (2.7%), P 24 (2.5%), S 24 (2.5%), J 18 (1.9%), I 14 (1.5%), Y 14 (1.5%), E 12 (1.3%), Z 12 (1.3%), A 8 (0.8%), B 6 (0.6%), N 6 (0.6%)

- **atbash** — V 146 (15.4%), G 100 (10.5%), H 76 (8.0%), L 76 (8.0%), I 72 (7.6%), Z 66 (7.0%), S 54 (5.7%), M 52 (5.5%), R 44 (4.6%), X 42 (4.4%), W 30 (3.2%), F 26 (2.7%), O 26 (2.7%), K 24 (2.5%), N 24 (2.5%), T 18 (1.9%), E 14 (1.5%), U 14 (1.5%), D 12 (1.3%), Y 12 (1.3%), C 8 (0.8%), B 6 (0.6%), P 6 (0.6%)

- **vigenere** — P 88 (9.3%), E 84 (8.9%), T 76 (8.0%), F 68 (7.2%), S 66 (7.0%), O 56 (5.9%), C 42 (4.4%), D 40 (4.2%), N 40 (4.2%), H 36 (3.8%), A 32 (3.4%), L 30 (3.2%), M 30 (3.2%), Z 30 (3.2%), I 28 (3.0%), J 28 (3.0%), R 28 (3.0%), U 28 (3.0%), Y 24 (2.5%), V 22 (2.3%), B 18 (1.9%), Q 18 (1.9%), G 14 (1.5%), X 14 (1.5%), W 6 (0.6%), K 2 (0.2%)

Пространства ключей для выбранных размеров — {"caesar": 26, "vigenere": 17576, "permutation": 24}

Цезарь и Атбаш перемещают частоты между буквами. У Виженера распределение меняется, но сдвиги повторяются с периодом ключа. На коротком тексте выводы особенно зависят от словаря. Пространство ключей не учитывает статистические закономерности.

## Стеганография

[
  {
    "plain": "Meet at noon.",
    "hidden_ciphertext": "Phhw dw qrrq.",
    "after_deciphering": "Meet at noon.",
    "header_flip": "Длина сообщения повреждена.",
    "payload_flip": "Leet at noon.",
    "payload_changed": true,
    "changed_pixels": 54
  },
  {
    "algorithm": "cardano",
    "operation": "encrypt",
    "source_message": "КОД 42",
    "result": "КОД4· 2·········",
    "key_or_params": {
      "length": 6
    },
    "status": "ok",
    "explanation": ""
  },
  {
    "algorithm": "cardano",
    "operation": "decrypt",
    "source_message": "КОД4· 2·········",
    "result": "КОД 42",
    "key_or_params": {
      "length": 6
    },
    "status": "ok",
    "explanation": ""
  }
]

## Хеш и AES-GCM

[
  {
    "algorithm": "sha256",
    "operation": "digest",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.",
    "result": "1df2a677a75b2d7903b7bf838e2a2137e8e783fdf551a4a86f800b3dc33f5cf0",
    "key_or_params": {},
    "status": "ok",
    "explanation": ""
  },
  {
    "algorithm": "sha256",
    "operation": "verify",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.",
    "result": "1df2a677a75b2d7903b7bf838e2a2137e8e783fdf551a4a86f800b3dc33f5cf0",
    "key_or_params": {},
    "status": "ok",
    "explanation": "Хеш совпал."
  },
  {
    "algorithm": "sha256",
    "operation": "verify",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.!",
    "result": "50c62e968b14e5d9fbe059f3b912c5c5cb43051841e8a0d364ccf58df4039973",
    "key_or_params": {},
    "status": "error",
    "explanation": "Хеш изменился."
  },
  {
    "algorithm": "aes_gcm",
    "operation": "encrypt",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.",
    "result": "1513e8e30348b3e7d8dcd51a94caea8a7bb952b6b6f0b85052a3f221162a404d4a908ffeb6fbf6271fb361b151d91beed6ead5968f8174be33536510b94cb2e1fae5cea0e4760dd9ca58aa6a367832a316727893e1ad36e63ca10ef09b0e05b5600cfc2f23f36c9d540c9bca46501dde15565338f2937f28784f12",
    "key_or_params": {
      "nonce": "1513e8e30348b3e7d8dcd51a",
      "tag_bytes": 16
    },
    "status": "ok",
    "explanation": ""
  },
  {
    "algorithm": "aes_gcm",
    "operation": "decrypt",
    "source_message": "1513e8e30348b3e7d8dcd51a94caea8a7bb952b6b6f0b85052a3f221162a404d4a908ffeb6fbf6271fb361b151d91beed6ead5968f8174be33536510b94cb2e1fae5cea0e4760dd9ca58aa6a367832a316727893e1ad36e63ca10ef09b0e05b5600cfc2f23f36c9d540c9bca46501dde15565338f2937f28784f12",
    "result": "Учебная записка. Макет лабораторного стенда принят.",
    "key_or_params": {},
    "status": "ok",
    "explanation": ""
  },
  {
    "algorithm": "aes_gcm",
    "operation": "decrypt",
    "source_message": "1513e8e30348b3e7d8dcd51a94caea8a7bb952b6b6f0b85052a3f221162a404d4a908ffeb6fbf6271fb361b151d91beed6ead5968f8174be33536510b94cb2e1fae5cea0e4760dd9ca58aa6a367832a316727893e1ad36e63ca10ef09b0e05b5600cfc2f23f36c9d540c9bca46501dde15565338f2937f28784f13",
    "result": "",
    "key_or_params": {},
    "status": "error",
    "explanation": "Проверка аутентичности AES-GCM не пройдена."
  }
]

## Подпись

[
  {
    "algorithm": "ecdsa",
    "operation": "sign",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.",
    "result": "{\"digest\": \"1df2a677a75b2d7903b7bf838e2a2137e8e783fdf551a4a86f800b3dc33f5cf0\", \"der\": \"304402203ea073a489b1352acd786ce9a56bb7201e459972f986df94e4018ca6f3280e3e02206856c14280b88e2d36ba860fb31d3f8194d0a75bae28aa7e94801da30354682b\"}",
    "key_or_params": {},
    "status": "ok",
    "explanation": ""
  },
  {
    "algorithm": "ecdsa",
    "operation": "verify",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.",
    "result": "действительна",
    "key_or_params": {},
    "status": "ok",
    "explanation": "действительна"
  },
  {
    "algorithm": "ecdsa",
    "operation": "verify",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.!",
    "result": "документ изменён",
    "key_or_params": {},
    "status": "error",
    "explanation": "документ изменён"
  },
  {
    "algorithm": "ecdsa",
    "operation": "verify",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.",
    "result": "недействительна",
    "key_or_params": {},
    "status": "error",
    "explanation": "недействительна"
  },
  {
    "algorithm": "ecdsa",
    "operation": "verify",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.",
    "result": "недействительна",
    "key_or_params": {},
    "status": "error",
    "explanation": "недействительна"
  },
  {
    "algorithm": "certificate",
    "operation": "inspect",
    "source_message": "relay.example.test",
    "result": "{\"subject\": \"relay.example.test\", \"issuer\": \"CryptoLab Demo CA\", \"valid_from\": \"2026-01-01\", \"valid_until\": \"2027-01-01\", \"serial\": \"DEMO-005\", \"status\": \"active\", \"purpose\": \"server\"}",
    "key_or_params": {},
    "status": "ok",
    "explanation": "Условная проверка карточки пройдена."
  }
]

### Виды электронной подписи

| Вид | Механизм | Ключи | Сертификат | Проверка | Признание |
| --- | --- | --- | --- | --- | --- |
| ПЭП | Коды, пароли или иные средства подтверждения | не требуется по определению | не требуется | определение подписанта по правилам системы | в случаях, установленных применимыми актами или соглашением |
| УНЭП | Криптографическое преобразование | ключ подписи и ключ проверки | квалифицированный сертификат не обязателен | определение подписанта и обнаружение изменений | в случаях, установленных применимыми актами или соглашением |
| УКЭП | Усиленная подпись с дополнительными требованиями | ключ проверки указан в квалифицированном сертификате | квалифицированный | подпись, сертификат и применимые ограничения | общий режим равнозначности собственноручной подписи с предусмотренными законом исключениями |

## Модель TLS

[
  {
    "algorithm": "tls_model",
    "operation": "simulate",
    "source_message": "Meet at noon.",
    "result": "Meet at noon.",
    "key_or_params": {
      "stages": [
        "Условная проверка карточки",
        "X25519",
        "HKDF-SHA256",
        "AES-GCM"
      ],
      "packet": "ee4f0fa3f58c138c7ec65a2a827971b71c5a0f4a9239f95b606ee26d03f67afa0027bcec3a01d9e7a8"
    },
    "status": "ok",
    "explanation": "TLS-модель не совместима с реальным протоколом. Учебная карточка не связывает сервер с обменом ключами."
  }
]

## Инциденты

[
  {
    "algorithm": "incidents",
    "operation": "compare",
    "source_message": "",
    "result": "[\n  {\n    \"name\": \"WannaCry\",\n    \"year\": 2017,\n    \"type\": \"Шифровальщик с самораспространением\",\n    \"encryption\": \"Блокирование доступа и требование выкупа\",\n    \"processes\": \"Рабочие станции и доступность служб\",\n    \"consequences\": \"Массовые сбои в нескольких странах\",\n    \"scope\": \"Международный масштаб, качественная оценка\",\n    \"mitigation\": \"Обновления, отключение устаревших протоколов, сегментация и резервные копии\",\n    \"source\": \"https://www.cisa.gov/sites/default/files/FactSheets/NCCIC%20ICS_FactSheet_WannaCry_Ransomware_S508C.pdf\"\n  },\n  {\n    \"name\": \"NotPetya\",\n    \"year\": 2017,\n    \"type\": \"Деструктивное ПО под видом вымогательства\",\n    \"encryption\": \"Данные и системы выводились из строя, восстановление через выкуп не было надёжным\",\n    \"processes\": \"Бизнес-системы и логистика\",\n    \"consequences\": \"Сбои в Украине и за её пределами\",\n    \"scope\": \"Международный масштаб, качественная оценка\",\n    \"mitigation\": \"Сегментация, проверка цепочки поставок и отработка восстановления\",\n    \"source\": \"https://www.cisa.gov/sites/default/files/publications/AA22-110A_Joint_CSA_Russian_State-Sponsored_and_Criminal_Cyber_Threats_to_Critical_Infrastructure_4_20_22_Final.pdf\"\n  },\n  {\n    \"name\": \"Colonial Pipeline\",\n    \"year\": 2021,\n    \"type\": \"Вымогательство DarkSide в корпоративной ИТ-сети\",\n    \"encryption\": \"Шифрование использовалось для давления на организацию\",\n    \"processes\": \"Корпоративные системы и эксплуатация трубопровода\",\n    \"consequences\": \"Временная остановка операций компании\",\n    \"scope\": \"Компания и региональные поставки США, качественная оценка\",\n    \"mitigation\": \"Многофакторная аутентификация, разделение ИТ и операционной сети, резервное восстановление\",\n    \"source\": \"https://www.cisa.gov/sites/default/files/publications/AA21-131A_Darkside_Ransomware.pdf\"\n  }\n]",
    "key_or_params": {},
    "status": "ok",
    "explanation": ""
  },
  {
    "algorithm": "network_log",
    "operation": "inspect",
    "source_message": "20",
    "result": "[\n  {\n    \"time\": \"2026-11-23T09:00:00+07:00\",\n    \"destination\": \"192.0.2.10\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 450,\n    \"process\": \"lab_sync\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:01:00+07:00\",\n    \"destination\": \"192.0.2.10\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 605,\n    \"process\": \"lab_sync\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:02:00+07:00\",\n    \"destination\": \"192.0.2.10\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 760,\n    \"process\": \"lab_sync\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:03:00+07:00\",\n    \"destination\": \"192.0.2.10\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 915,\n    \"process\": \"lab_sync\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:04:00+07:00\",\n    \"destination\": \"198.51.100.21\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 1070,\n    \"process\": \"lab_browser\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\",\n      \"неизвестный узел\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:05:00+07:00\",\n    \"destination\": \"198.51.100.22\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 1225,\n    \"process\": \"lab_browser\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\",\n      \"неизвестный узел\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:06:00+07:00\",\n    \"destination\": \"198.51.100.20\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 1380,\n    \"process\": \"lab_browser\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:07:00+07:00\",\n    \"destination\": \"198.51.100.21\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 1535,\n    \"process\": \"lab_browser\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\",\n      \"неизвестный узел\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:08:00+07:00\",\n    \"destination\": \"198.51.100.22\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 1690,\n    \"process\": \"lab_browser\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\",\n      \"неизвестный узел\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:09:00+07:00\",\n    \"destination\": \"198.51.100.20\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 1845,\n    \"process\": \"lab_browser\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:10:00+07:00\",\n    \"destination\": \"198.51.100.21\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 2000,\n    \"process\": \"lab_browser\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\",\n      \"неизвестный узел\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:11:00+07:00\",\n    \"destination\": \"198.51.100.22\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 2155,\n    \"process\": \"lab_browser\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\",\n      \"неизвестный узел\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:12:00+07:00\",\n    \"destination\": \"198.51.100.20\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 2310,\n    \"process\": \"lab_browser\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:13:00+07:00\",\n    \"destination\": \"198.51.100.21\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 2465,\n    \"process\": \"lab_browser\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\",\n      \"неизвестный узел\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:14:00+07:00\",\n    \"destination\": \"198.51.100.22\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 2620,\n    \"process\": \"lab_browser\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\",\n      \"неизвестный узел\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:15:00+07:00\",\n    \"destination\": \"198.51.100.20\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 2775,\n    \"process\": \"lab_browser\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:16:00+07:00\",\n    \"destination\": \"198.51.100.21\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 2930,\n    \"process\": \"lab_browser\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\",\n      \"неизвестный узел\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:17:00+07:00\",\n    \"destination\": \"198.51.100.22\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 3085,\n    \"process\": \"lab_browser\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\",\n      \"неизвестный узел\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:18:00+07:00\",\n    \"destination\": \"198.51.100.20\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 3240,\n    \"process\": \"lab_browser\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"повторяющиеся соединения\"\n    ]\n  },\n  {\n    \"time\": \"2026-11-23T09:19:00+07:00\",\n    \"destination\": \"203.0.113.99\",\n    \"protocol\": \"HTTPS\",\n    \"bytes_out\": 1500000,\n    \"process\": \"lab_export\",\n    \"check\": \"учебная запись\",\n    \"flags\": [\n      \"большой исходящий объём\",\n      \"новый процесс\",\n      \"неизвестный узел\"\n    ]\n  }\n]",
    "key_or_params": {},
    "status": "ok",
    "explanation": "Признаки требуют проверки. HTTPS сам по себе не признак атаки."
  }
]

## Тесты

{
  "exit_code": 0,
  "cases": [
    {
      "input_expected": "test_caesar[russian_shift_3_round_trip]",
      "actual": "пройден"
    },
    {
      "input_expected": "test_caesar[latin_case_round_trip]",
      "actual": "пройден"
    },
    {
      "input_expected": "test_caesar[shift_26_identity]",
      "actual": "пройден"
    },
    {
      "input_expected": "test_caesar[shift_67_modulo_33]",
      "actual": "пройден"
    },
    {
      "input_expected": "test_caesar[negative_shift_round_trip]",
      "actual": "пройден"
    },
    {
      "input_expected": "test_caesar_known_vector",
      "actual": "пройден"
    },
    {
      "input_expected": "test_atbash_twice_original",
      "actual": "пройден"
    },
    {
      "input_expected": "test_polybius[latin_J_merges_into_I]",
      "actual": "пройден"
    },
    {
      "input_expected": "test_polybius[russian_full_alphabet]",
      "actual": "пройден"
    },
    {
      "input_expected": "test_vigenere_repeated_letters_and_round_trip",
      "actual": "пройден"
    },
    {
      "input_expected": "test_permutation_partial_block_round_trip",
      "actual": "пройден"
    },
    {
      "input_expected": "test_rotor_round_trip",
      "actual": "пройден"
    },
    {
      "input_expected": "test_normalize_and_restore_russian_format",
      "actual": "пройден"
    },
    {
      "input_expected": "test_caesar_26_candidates_correct_key_present",
      "actual": "пройден"
    },
    {
      "input_expected": "test_frequency_A3_B1",
      "actual": "пройден"
    },
    {
      "input_expected": "test_alphabet_26_key_3_block_4",
      "actual": "пройден"
    },
    {
      "input_expected": "test_large_https_flagged_with_unknown_process_and_host",
      "actual": "пройден"
    },
    {
      "input_expected": "test_sha256_abc_vector_and_changed_document",
      "actual": "пройден"
    },
    {
      "input_expected": "test_aes_gcm_nonce_fresh_and_message_round_trip",
      "actual": "пройден"
    },
    {
      "input_expected": "test_aes_gcm_changed_tag_error_no_plaintext",
      "actual": "пройден"
    },
    {
      "input_expected": "test_tls_good_card_and_wrong_subject",
      "actual": "пройден"
    },
    {
      "input_expected": "test_original_signature_valid",
      "actual": "пройден"
    },
    {
      "input_expected": "test_changed_document_detected",
      "actual": "пройден"
    },
    {
      "input_expected": "test_wrong_public_key_invalid",
      "actual": "пройден"
    },
    {
      "input_expected": "test_damaged_der_signature_invalid",
      "actual": "пройден"
    },
    {
      "input_expected": "test_damaged_public_key_wrong_format",
      "actual": "пройден"
    },
    {
      "input_expected": "test_missing_document_insufficient",
      "actual": "пройден"
    },
    {
      "input_expected": "test_lsb_utf8_round_trip",
      "actual": "пройден"
    },
    {
      "input_expected": "test_lsb_39_pixels_rejects_one_byte",
      "actual": "пройден"
    },
    {
      "input_expected": "test_lsb_header_flip_rejected",
      "actual": "пройден"
    },
    {
      "input_expected": "test_lsb_payload_flip_silently_changes_text",
      "actual": "пройден"
    },
    {
      "input_expected": "test_cardano_round_trip_with_padding",
      "actual": "пройден"
    },
    {
      "input_expected": "test_cardano_overlapping_mask_rejected",
      "actual": "пройден"
    },
    {
      "input_expected": "test_caesar_invalid_inputs_error[empty]",
      "actual": "пройден"
    },
    {
      "input_expected": "test_caesar_invalid_inputs_error[unsupported_emoji]",
      "actual": "пройден"
    },
    {
      "input_expected": "test_caesar_invalid_inputs_error[string_shift]",
      "actual": "пройден"
    },
    {
      "input_expected": "test_caesar_invalid_inputs_error[bool_shift]",
      "actual": "пройден"
    },
    {
      "input_expected": "test_caesar_invalid_inputs_error[mixed_alphabets]",
      "actual": "пройден"
    },
    {
      "input_expected": "test_polybius_unsupported_letter_error",
      "actual": "пройден"
    },
    {
      "input_expected": "test_empty_vigenere_key_error",
      "actual": "пройден"
    },
    {
      "input_expected": "test_permutation_duplicate_indices_error",
      "actual": "пройден"
    },
    {
      "input_expected": "test_missing_input_dataset_controlled",
      "actual": "пройден"
    },
    {
      "input_expected": "test_corrupt_json_dataset_controlled",
      "actual": "пройден"
    }
  ],
  "pytest": "...........................................                              [100%]\n- generated xml file: tests.xml -\n43 passed in 0.24s\n"
}

## Проверочные сценарии

[
  {
    "id": "caesar_round_trip",
    "expected": "original_text",
    "actual": "original_text",
    "ok": true
  },
  {
    "id": "aes_modified_packet",
    "expected": "error",
    "actual": "error",
    "ok": true
  },
  {
    "id": "signature_modified_document",
    "expected": "документ изменён",
    "actual": "документ изменён",
    "ok": true
  }
]

## Контрольные дефекты

[
  {
    "defect": "Нецелое значение сдвига",
    "detected": true,
    "after_repair": true
  },
  {
    "defect": "Изменение подписанного документа",
    "detected": "документ изменён",
    "after_repair": "действительна"
  },
  {
    "defect": "Отсутствующий входной набор",
    "detected": "Набор messages.json недоступен или повреждён.",
    "after_repair": "Загружено сообщений: 9"
  }
]

## Выводы

Форма распределения частот сохраняется при Цезаре и Атбаше. Повтор ключа Виженера создаёт периодичность. Краткий текст даёт меньше наблюдений. Перестановка и решётка сохраняют состав символов, Полибий раскрывает повторы координат, а учебный ротор остаётся предсказуемой периодической моделью. LSB скрывает наличие сообщения, сохраняя уязвимость к изменению носителя. SHA-256 выявляет изменения при сравнении с доверенным хешем. AES-GCM обеспечивает конфиденциальность и аутентичность при корректном управлении ключами и nonce. ECDSA проверяет происхождение и целостность по открытому ключу. Доверие к открытому ключу проверяется отдельно. Учебная модель, не для реальной защиты.
