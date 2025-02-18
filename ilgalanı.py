import json
from data_structures import HashTable,Set,Stack,myList
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        if not self.head:
            self.head = Node(key, value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(key, value)

    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next   
        return None 

    def update(self, key, value):
        current = self.head
        while current and current.key != key:
            current = current.next
        if current:
            current.value = value



# Kategoriler ve kelimeler
kelimeler = LinkedList()
kelimeler.insert("spor", ["voleybol", "kupa","takım","lig","futbol","forma","kale","maç","madalya","final","saha","klüp","basketbol","Galatasaray","şampiyonu"])
kelimeler.insert("sanat", ["resim", "heykel","rol","oyuncu","filmin","ödülü","sinema","video","dizi","yönetmenliğini",""])
kelimeler.insert("muzik", ["nota", "akor","müzik","albüm","şarkının","ses","klip","rock"])
kelimeler.insert("tarih", ["dönem", "roma","mücadele","tarihten","cumhuriyeti","paşa","yıllar","bizans","imparatorluğu","sovyetler","müze"])
kelimeler.insert("coğrafya", ["ilçenin", "istanbul","Avrupa","doğu","tarım","ankara","dünyanın","kuzey","güney","bölgede","iklimi","Anadolu","karadeniz","nehri","orman","bölge","akdeniz"])
kelimeler.insert("siyaset", ["halk", "devlet","ulusal","belediye","askeri","üyesi","yönetim","parti","milletvekili","bağımsız","bakanlığı","başkan","siyasal"])
kelimeler.insert("eğitim", ["fakültesi", "eğitim","hukuk","mezun","lise","enstitü","üniversite","öğrenci","akademik","mühendisliği","lisans","eğitim",])
kelimeler.insert("bilim",["bilim","bilimsel","elektrik","bilgisayar","enerji","fiziksel","uzay"])
kelimeler.insert("biyoloji",["tür","sağlık","bitki","canlı","tıp","tedavi","hayvan"])
kelimeler.insert("ekonomi",["ekonomik","ticaret","ticari","sanayi","para","hayvancılık","turizm","üretim"])
kelimeler.insert("edebiyat",["ingilizce","türkçe","dil","fransızca", "kitap", "söz","edebiyat","yazar","roman"])
kelimeler.insert("din",["islam","yahudi","müslüman","cami","kilise","hristiyan"])
kelimeler.insert("sosyoloji",["genç","çocuk","erkek","kadın","kız","insan","sosyal","yerleşim","evli","göç","geleneksel","nüfus","kültürel","doğum","gençlik"])
kelimeler.insert("ülke",["azerbaycan","fransa","rusya","çin","iran"])
kelimeler.insert("etnik",["alman","fransız","rus","amerikan","yunan","arap","kökenli","italyan","ermeni"])

ilgi = HashTable()
# Kullanıcıların ilgi alanlarını saklamak için hashtable'lar
spor = HashTable()
sanat = HashTable()
cografya = HashTable()
muzik = HashTable()
tarih = HashTable()
siyaset = HashTable()
egitim = HashTable()
bilim = HashTable()
biyoloji = HashTable()
ekonomi = HashTable()
edebiyat = HashTable()
din = HashTable()
sosyoloji = HashTable()
ülke = HashTable()
etnik = HashTable()

ilgi.__setitem__("spor", spor)
ilgi.__setitem__("sanat", sanat)
ilgi.__setitem__("cografya", cografya)
ilgi.__setitem__("muzik", muzik)
ilgi.__setitem__("tarih", tarih)
ilgi.__setitem__("siyaset", siyaset)
ilgi.__setitem__("egitim", egitim)
ilgi.__setitem__("bilim", bilim)
ilgi.__setitem__("biyoloji", biyoloji)
ilgi.__setitem__("ekonomi", ekonomi)
ilgi.__setitem__("edebiyat", edebiyat)
ilgi.__setitem__("din", din)
ilgi.__setitem__("sosyoloji", sosyoloji)
ilgi.__setitem__("ülke", ülke)
ilgi.__setitem__("etnik", etnik)


def interests(user, metin):
    kelime_sayilari = LinkedList()
    for data in metin.__iter__():
     for kelime in data.split():
            current = kelimeler.head
            while current:
                if kelime in current.value:
                    count = kelime_sayilari.find(current.key)
                    if count is None:
                        kelime_sayilari.insert(current.key, 1)
                    else:
                        kelime_sayilari.update(current.key, count + 1)
                current = current.next

    current = kelime_sayilari.head
    if current is not None:
        max_kategori = current.key
        max_deger = current.value
        while current:
            if current.value > max_deger:
                max_kategori = current.key
                max_deger = current.value
            current = current.next
    else:
        max_kategori = None

    # Kullanıcının ilgi alanlarını hashtable'a ekle
    if max_kategori is not None:
       if max_kategori == "spor":
        spor.__setitem__(user.person.username, metin)
       elif max_kategori == "sanat":
        sanat.__setitem__(user.person.username, metin)
       elif max_kategori == "muzik":
        muzik.__setitem__(user.person.username, metin)
       elif max_kategori == "tarih":
        tarih.__setitem__(user.person.username, metin)
       elif max_kategori == "egitim":
        egitim.__setitem__(user.person.username, metin)
       elif max_kategori == "cografya":
        cografya.__setitem__(user.person.username, metin)
       elif max_kategori == "siyaset":
        siyaset.__setitem__(user.person.username, metin)
       elif max_kategori == "bilim":
        bilim.__setitem__(user.person.username, metin)
       elif max_kategori == "biyoloji":
        biyoloji.__setitem__(user.person.username, metin)
       elif max_kategori == "ekonomi":
        ekonomi.__setitem__(user.person.username, metin)
       elif max_kategori == "edebiyat":
        edebiyat.__setitem__(user.person.username, metin)
       elif max_kategori == "din":
        din.__setitem__(user.person.username, metin)
       elif max_kategori == "sosyoloji":
        sosyoloji.__setitem__(user.person.username, metin)
       elif max_kategori == "ülke":
        ülke.__setitem__(user.person.username, metin)
       elif max_kategori == "etnik":
        etnik.__setitem__(user.person.username, metin)
        # Sonuçları bir JSON dosyasına yaz
    with open('katagoriler.json', 'a') as f:
        json.dump({user.person.username: {"gercek_ad": user.person.name, "kategori": max_kategori, "frekans": max_deger}}, f)
        f.write('\n')
         

        

def same_users():
    with open('kisiler.json', 'w',encoding='utf-8') as file:
        for category, hashtable in ilgi.get_items():
            users = [username[0] for username in hashtable.get_items()]
            file.write(f'Kategori: {category}, Kullanicilar: {users}\n')

def find_category(username):
    if spor.__getitem__(username) is not None:
            return "spor"
    elif sanat.__getitem__(username) is not None:
            return "sanat"
    elif muzik.__getitem__(username) is not None:
            return "muzik"
    elif tarih.__getitem__(username) is not None:
            return "tarih"
    elif egitim.__getitem__(username) is not None:
            return "egitim"
    elif cografya.__getitem__(username) is not None:
            return "cografya"
    elif siyaset.__getitem__(username) is not None:
            return "siyaset"
    elif bilim.__getitem__(username) is not None:
            return "bilim"
    elif biyoloji.__getitem__(username) is not None:
            return "biyoloji"
    elif ekonomi.__getitem__(username) is not None:
            return "ekonomi"
    elif edebiyat.__getitem__(username) is not None:
            return "edebiyat"
    elif din.__getitem__(username) is not None:
            return "din"
    elif sosyoloji.__getitem__(username) is not None:
            return "sosyoloji"
    elif etnik.__getitem__(username) is not None:
            return "etnik"
          
           
def dfs(graph, start, sentence_list,table):
    visited = Set()
    stack = Stack()
    found_sentences = HashTable()

    stack.push(start)
    i = 0
    while not stack.isEmpty():
        i = i + 1
        print(f"i = {i}") 
        current_vertex = table.__getitem__(stack.pop().person.username)

        if not visited.contains(current_vertex.person.username):
            visited.add(current_vertex.person.username)

            # Kullanıcının hangi kategoriye ait olduğunu bulduk
            category = find_category(current_vertex.person.username)
            if category:
                # Kullanıcının ait olduğu kategorinin kelimelerini aldık
                words_to_find = kelimeler.find(category)
                tweets_found = myList()  # Her kullanıcı için yeni bir bağlı liste oluşturduk

                sentence = sentence_list.__getitem__(current_vertex.person.username) 
                if sentence is None: 
                    sentence=[]

                for tweet in sentence:
                    words = tweet.split()
                    word_found = any(word in words_to_find for word in words)
                    if word_found:
                        tweets_found.insert(tweet)

                found_sentences.__setitem__(current_vertex.person.username, tweets_found)

        for neighbour in graph.getVertex(current_vertex.person.username).connections.get_items():
            if not visited.contains(neighbour):
                visited.add(neighbour)
                stack.push(neighbour)

    return found_sentences


   


