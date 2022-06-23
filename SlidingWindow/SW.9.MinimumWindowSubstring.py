def smallestWindow(s, p):
    # code here
    minlength = 999999999999999
    index = None
    mapping = dict()
    for i in p:
        if i not in mapping:
            mapping[i] = 1
        else:
            mapping[i] += 1
    count = len(mapping)
    i = 0
    for j in range(len(s)):
        if s[j] in mapping:
            mapping[s[j]] -= 1
            if mapping[s[j]] == 0:
                count -= 1
        while count == 0:
            if j - i + 1 < minlength:
                minlength = j - i + 1
                index = i
            if s[i] in mapping:
                mapping[s[i]] += 1
                if mapping[s[i]] == 1:
                    count += 1
            i += 1
    if index is not None:
        return s[index:(index + minlength)]
    return -1
s = "caeibcjgfadihdddjadbgbeijhjdgbeadiijeaiagjbfhhhhefagcbjgceiidhfhjgbdhbbegehbehgdacbdgefijeehbefididfbfadgjhgccbebccgacijibcfjfhcgfbgacgbefeffiebhfaagfijfjgjgbjhidbacjgfaiaiidfjggfgdeadhdaaeibgdbhdiiehdedgedagfbdjabaehbbbiedajdecehcidbfgdiffjhdaaeaibbbejgiiijehcggccbfbhdjebehahjheadiadchjifhdedbccaigdfdchabiceeidjafbfachhfdbaejaggggehhjaegbjahaeicchbefcjgjbjcgjjabdheacahcegfcbcjafajajcbfaacfjbcfaeihfccjfdjegaidjaefiiaidjjgjfdafigegacfdeiecejcbfbdgbidjficbciigfjibgaggihedifcjhihbdfegcfbfjiiigdajfdceafjdhaeejabbhfdgebfbhibfhhgfjiijafceihieeefcgfajighfbbgajebijfhjcficibeaaaigaijddfabicjbabedhjbciccbficbhehihhgahbfhhhijcjjihghgdgeafcdhchjehhhaiieajdhaihjigijebdahhbgebhadcigafficgeeigabfecibcg"
p = "dbjdiegjgebihaicgbgbbfcfbfbbbhfgcjhhehfcdjfcddfiibceehjhfeadcfbifbcgihbffjgejbidgieifjgceehcedidfdcjgidhgfgfibechgggibfbjjgfghihjeicgjjhce"
print(smallestWindow(s, p))