from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random

active_users = set()

def track_users(update, context):
    user = update.message.from_user
    display_name = f"@{user.username}" if user.username else user.first_name
    active_users.add((user.id, display_name))

def ship(update, context):
    try:
        names = ' '.join(context.args).split('+')
        if len(names) != 2:
            update.message.reply_text("Örnek: /ship Emre + Elif 😅")
            return
        name1 = names[0].strip()
        name2 = names[1].strip()
        score = random.randint(0, 100)
        msg = f"💘 {name1} ve {name2} %{score} uyumlu!\n\n"
        if score <= 20:
            msg += "🙃 Bence siz arkadaş kalın..."
        elif score <= 40:
            msg += "🤔 Bidaha düşünün derim..."
        elif score <= 60:
            msg += "😲 Ayyy siz çaya çıkın!"
        elif score <= 80:
            msg += "💃 Seda ablan size kurban olsun!"
        else:
            msg += "🔥 Seda abla stüdyoyu yaktı!"
        update.message.reply_text(msg)
    except:
        update.message.reply_text("Bi gariplik oldu 🤯")

def shipme(update, context):
    user = update.message.from_user
    user_id = user.id
    user_name = f"@{user.username}" if user.username else user.first_name
    candidates = [u for u in active_users if u[0] != user_id]
    if not candidates:
        update.message.reply_text("Kimse konuşmadı... Tek tabancasın 😅")
        return
    partner = random.choice(candidates)
    partner_name = partner[1]
    score = random.randint(0, 100)
    msg = f"🔮 {user_name} ve {partner_name} %{score} uyumlu çıktı!\n\n"
    if score <= 20:
        msg += "🙃 Bence siz arkadaş kalın..."
    elif score <= 40:
        msg += "🤔 Bidaha düşünün derim..."
    elif score <= 60:
        msg += "😲 Ayyy siz çaya çıkın!"
    elif score <= 80:
        msg += "💃 Seda ablan size kurban olsun!"
    else:
        msg += "🔥 Seda abla stüdyoyu yaktı!"
    update.message.reply_text(msg)

def adana(update, context):
    score = random.randint(50, 100)
    msg = f"🌶️ Bugün %{score} Adanalısın!\n"
    if score > 85:
        msg += "🌞 Sıcaktan değil, karizmadan yanıyorsun!"
    elif score > 70:
        msg += "🍢 Kebaplar seni görse sahiplenir."
    else:
        msg += "💥 Hafif Adana havası var üstünde."
    update.message.reply_text(msg)

def urfa(update, context):
    score = random.randint(50, 100)
    msg = f"🌶️ Bugün %{score} Urfalısın!\n"
    if score > 85:
        msg += "🔥 Lahmacunla doğmuşsun resmen!"
    elif score > 70:
        msg += "🧿 Şanlıurfa seni çağırıyor."
    else:
        msg += "📿 Hafif acı, ama yeterli."
    update.message.reply_text(msg)
def rona(update, context):
    user = update.message.from_user.first_name

    cumleler = [
        "Ben Ronayım. Sessizliğim bile asildir.",
        "Gürültü bana göre değil; ben asaletle konuşurum.",
        "Tahtım yok belki ama duruşum yeter.",
        "Ben kraliçeyim; gösterişli değilim ama derinim.",
        "Gözlerim konuşur, kelimelere gerek bırakmam.",
        "Benim gülüşüm, sessiz bir devrimdir.",
        "Asalet, adımı söylediğinizde bile hissedilir.",
        "Sakinliğim zayıflık değil, seçilmiş bir güçtür.",
        "İz bırakmam ama varlığım unutulmaz.",
        "Sözle değil, tavırla hükmederim.",
        "Duruşumla susarım, ama her şey anlaşılır.",
        "Zarafet benimle yürür, ben onunla değil.",
        "Ben Ronayım. Kraliçe olmayı seçmedim, doğuştan öyleyim.",
        "Sesimi yükseltmem, çünkü sessizliğim yankı yapar.",
        "İhtişam benim tarzım değil, asaletim yetiyor zaten."
    ]

    from random import choice
    secilen = choice(cumleler)
    mesaj = f"👑 Rona dedi ki:\n\n“{secilen}”"
    update.message.reply_text(mesaj)

def esma(update, context):
    user = update.message.from_user.first_name

    cumleler = [
        "Cazibem o kadar güçlü ki, tavus kuşları bile kıskanıyor.",
        "Gülüşüm var ya, elektrik faturalarını düşürür.",
        "Aynaya bakınca bile 'Vay be' diyorum, o derece.",
        "Tatlılık seviyem şeker krizine sebep olabilir.",
        "Bir bakışımla kahveler köpürür.",
        "Güzelliğime bakıp aynalar selfie çekiyor.",
        "Çekiciliğim, mıknatısları kendine çekiyor.",
        "Girdiğim ortama ben değil, ışıltım giriyor önce.",
        "Cazibemle sokak lambaları gündüz de yanıyor.",
        "Öyle tatlıyım ki arılar bile etrafımda dönüyor.",
        "Duruşum bile podyumdan ilham alıyor.",
        "Gözlerimde GPS var, çünkü insanlar yolunu kaybediyor.",
        "Kendime baktığımda bile 'Aman tanrım' diyorum.",
        "Etrafta bu kadar kalp atışı varsa, nedeni benim.",
        "Kendime gülümseyince çiçekler utanıyor.",
        "Işığım var ama güneş panellerine ihtiyaç bırakmam.",
        "Cazibem öyle bir seviye ki, ay bile tutuluyor.",
        "Bir ben var benden içeri, o bile bana hayran.",
        "Güzelliğimden Google bile beni aratıyor.",
        "Tatlılığım fazla dozda alınınca bağımlılık yapar."
    ]

    from random import choice
    secilen = choice(cumleler)
    mesaj = f"💫 Esma dedi ki:\n\n{secilen}"
    update.message.reply_text(mesaj)

def yargi(update, context):
    user = update.message.from_user
    username = f"@{user.username}" if user.username else user.first_name

    geceupuzun_cumleler = [
        # İlk 12
        "Ben ki gecelerin yargıcı, hükümdarlara taç giydiren gölgelerin sultanıyım.",
        "Sessizliğin hüküm sürdüğü yerde ben konuştum, gece sustu.",
        "Sözüm kılıçtan keskindir; suskunluğum bile hüküm gibidir.",
        "Adaletin kalemiyle yazdım bu geceyi, satır arası sizsiniz.",
        "Yargım sadece size değil, size benzeyenlere de ders olacak.",
        "Tahtsız kral olur, ama benim hükmüm tahtsız kalmaz.",
        "Gece bana ait, siz sadece karanlığın misafirisiniz.",
        "Ben yargıya vardım. Uygun gördüm.",
        "Adalet istiyorsan beni çağırma, çünkü ben yargıyı çoktan verdim.",
        "Gece sustuysa bilin ki konuşan benimdir.",
        "Yıldızlar bile izinsiz doğamazken, senin ne cür’etle bana lafın düşer?",
        "Taht değil, yargıdan hüküm giydiririm. O yüzden kral değilim, yargıcım.",
        # Yeni 12
        "Ben gecenin gövdesine hükmedenim, gölgem bile susmaz.",
        "Tahtı olmayan bir yargıcım ama sözümle imparatorluk çöker.",
        "Adalet geceden sorulursa, ben cevap olurum.",
        "Ben ki geceyi adaletle yontan bıçak gibiyim.",
        "Gecenin kalbinde ben varım, karar verildi.",
        "Her hüküm bir geceyle başlar, her son beni anlatır.",
        "Benim karar defterim yıldızlarla yazılıdır.",
        "Ben susuyorsam, gece seni cezalandırıyordur.",
        "Ben ışık değilim, ama karanlıkta yön gösteririm.",
        "Söz bana geldiğinde, sükunet bile saygı duruşuna geçer.",
        "Tahta oturmadım ama yüreklerde hüküm sürdüm.",
        "Ben sadece karar vermem, zamanı mühürlerim."
    ]

    banabulasmayin_cumleler = [
        # İlk 12
        "Benim yargıcım ne derse o. Şimdi sıra size geldi.",
        "Konu sizseniz, hüküm çoktan verildi bile.",
        "Ben sizi dinledim. Artık hüküm vakti.",
        "Kısa ve net: Hakkınızı veriyorum.",
        "Ben susarsam, yargı devreye girer.",
        "Savunmanız alınmadan hüküm verildi.",
        "Ben değil, vicdanım konuştu: Suçlusun.",
        "Cümle kurmuyorum, hüküm kuruyorum.",
        "Yargı süreci tamamlandı. Artık geri dönüş yok.",
        "Ben sana değer vermedim, karar verdim.",
        "Sen sustun, ben karara vardım.",
        "Bugünlük bu kadar hoşgörü yeter. Şimdi sıra adalette.",
        # Yeni 12
        "Yargım sessizdir, ama etkisi yüksek voltajlıdır.",
        "Sen savunma yapmadan ben hükmü yazmıştım zaten.",
        "Sakin görünmem, sert kararlarımı örtmek içindir.",
        "Ben duygusal yargıç değilim, gerçekçiyim.",
        "Bana laf yetiştirmek istiyorsan önce vicdanını kontrol et.",
        "Düşünmeni istedim, ama ben karar verirken sen konuşuyordun.",
        "Yargıç modum açık, kırıcı olursa sistemsel.",
        "Sessizliğim onay değil, cezadır.",
        "Sen daha 'Merhaba' demeden hüküm hazırdı.",
        "Bu dava çoktan arşive kaldırıldı. Geçmiş olsun.",
        "Ben seni kırmak istemem, ama yargım keskindir.",
        "Kimse üstüme alınmasın ama kararım nettir: Hakkı verildi."
    ]

    if username == "@geceupuzun":
        mesaj = random.choice(geceupuzun_cumleler)
        update.message.reply_text(f"👑 {username} konuştu:\n\n{mesaj}")
    elif username == "@banabulasmayin":
        mesaj = random.choice(banabulasmayin_cumleler)
        update.message.reply_text(f"⚖️ {username} kararını verdi:\n\n{mesaj}")
    else:
        update.message.reply_text("⚠️ Sizin ne haddinize yargı vermek? Hüküm yalnızca gece yargıcı ve hakimine aittir. Haddinizi bilin.")

def kimdir(update, context):
    if not context.args:
        update.message.reply_text("Kimi sormak istiyorsun? Kullanıcı adını /kimdir @kullanici gibi yaz 😅")
        return

    kisi = context.args[0]
    if not kisi.startswith("@"):
        kisi = "@" + kisi

    mesajlar = [
        "{}... O sadece bir kullanıcı adı değil, o bir EFSANE.",
        "{} gördüğümde aklıma yıldızlar geliyor, ama yıldızlar onun kadar parlamıyor.",
        "{} kim mi? Çayın demi, sohbetin neşesi.",
        "{} geldiğinde Telegram bile gülümsüyor.",
        "{} bir gülüş atar, sinyal sistemi çöker.",
        "{} yokken grup, sanki müziksiz kafe gibi.",
        "{} anlatılmaz, yaşanır. Ama dikkatli yaşa, etkisi kalıcı.",
        "{} ile sohbet etmek, WiFi çekince hissettiren şeydir.",
        "{} sadece bir insan değil, belki de bir devlet sırrı.",
        "{} susar, ama o sessizlik bile manifesto gibi okunur.",
        "{}’e laf atan, modem fişini çeker gibi olur: her şey durur.",
        "{}’ün adını anmak bile 0.3 volt elektrik verir.",
        "{} geldi mi gruba kalite gelir. Kahkahasıyla çay bile kaynar.",
        "{}... Ay tutulsa da, o her zaman parlar.",
        "{} grupta olmasa eksiklik hissedilir, WiFi gibi.",
        "{} varsa bir yerde, espri de vardır, zeka da.",
        "{} bir gün yok olsun, grup 'offline' kalır.",
        "{} Telegram'ın Premium'u gibi: herkes istiyor ama nadir bulunur.",
        "{}... Eğer o bir film olsaydı, IMDb’si 9.8 olurdu.",
        "{} yazınca kalplerin şarjı doluyor.",
        "{} yeri geldi mi şiir gibi konuşur, yeri geldi mi direkt kernel panic.",
        "{} sensörsüz espri yapar ama etkisi sensörlü bomba gibi.",
        "{} öyle bir profil ki... açıklamasını yazsak karakter yetmez.",
        "{}’e bakan iki kere bakar. Üçüncüsünde gönül kayar.",
        "{} gülse, ekran aydınlanır.",
        "{} zaman zaman çılgın, zaman zaman filozof. 2’si 1 arada.",
        "{}... Ne desen az, ne yaşasan doymazsın.",
        "{} geldi mi grup yeşerir, gitse kuru kalır.",
        "{} = Grupta kahkaha garantisi.",
        "{} için tanım gerekmez, zaten tanıtan bir enerjisi var."
    ]

    from random import choice
    secilen = choice(mesajlar).format(kisi)
    update.message.reply_text(secilen)

def kamyoncu(update, context):
    user = update.message.from_user.first_name
    sozler = [
        "Yollar bitmez, biz biteriz.",
        "Gönül yükü ağırdır, her dorsede taşınmaz.",
        "Sevdiğim yollarda frene gerek yok.",
        "Sinyal verdikçe hatırladım seni.",
        "Rampada aşk olmaz, fren patlar.",
        "Aşkın yolu virajlı, direksiyonu sağlam tut.",
        "Korna çaldım, kalbini duydum.",
        "Gönül şoförsüzse her yol kazadır.",
        "Yüküm ağır, gönlüm boş.",
        "Yar aşkına gaza bastım, tutan olmadı.",
        "Yolda kaldım ama seni beklerken.",
        "Her lastik izinde bir aşk hikayesi saklı.",
        "Farı açık bıraktım, sen sanıp gel diye.",
        "Yolun sonu aşk olsun, viraj da sensin.",
        "Dorse gibi ağır sözlerin var, ama ben yükümü seviyorum.",
        "Takograf yalan söylemez, ben de.",
        "Süspansiyon gibi kalbim; sarsıntıda kırılır.",
        "Vites düşürdüm seni görünce.",
        "Yol ver gideyim, gönül ver kalayım.",
        "Aşk bir kamyon gibi gelir, kaçamazsın.",
        "Farlarımda ışığın, radyomda sesin var.",
        "Yollar viraj dolu, kalbim kadar.",
        "Park ettiğim kalbime çekmece misin be kızım?",
        "Mazot ateş pahası, aşkın bedeli yok.",
        "Lastik gibi döndüm durdum, sen hep aynı kaldın.",
        "Yolda kaldım, gönlünü ararken.",
        "Her mola seni düşünmek için.",
        "Yol bitmez, hasret bitmez.",
        "Gittikçe senin gibi yollar çıkıyor karşıma.",
        "Egzoz dumanı gibi dağıldım aşkından.",
        "Takla attım aşkında, şanzıman kırıldı.",
        "Korna çaldım, kalbin tınlamadı.",
        "Yol vermezsen aşkı sollayamam.",
        "Radyoda ismin, kalbimde cismin çalıyor.",
        "Gönül konvoyun en arkasında ben varım.",
        "Sinyalini bana verdin sandım.",
        "Sen tırı vurdun, ben gönlümü.",
        "Mazotum bitti ama aşkım devam ediyor.",
        "Fren tutmaz artık bu yokuşta.",
        "Yüküm aşksa, kantar tartmaz beni.",
        "Hız sınırını aştım, çünkü aklımdasın.",
        "Kalkış rampası gibisin; görünce zorlanıyorum.",
        "Korna değil kalbim öttü seni görünce.",
        "Dorse boş ama kalp dolu.",
        "Kamyoncu derler, yürek taşırız biz.",
        "Yol arkadaşım yoksa radyo sen ol.",
        "Park halindeyim ama seni bekliyorum.",
        "Kavşakta seni gördüm, yolum değişti.",
        "Sevdam tek yön, dönüşü yok."
    ]

    secilen = random.choice(sozler)
    mesaj = f"🚚 {user} dedi ki:\n\n“{secilen}”"
    update.message.reply_text(mesaj)

def saril(update, context):
    saril_resimleri = [
        "https://i.ibb.co/HHFrfqg/anime-hug1.jpg",
        "https://i.ibb.co/m0hFSTc/anime-hug2.jpg",
        "https://i.ibb.co/VvJ2KpC/anime-hug3.jpg",
        "https://i.ibb.co/58QwzKd/anime-hug4.jpg",
        "https://i.ibb.co/Z1vxtCV/anime-hug5.jpg"
    ]
    secilen_resim = random.choice(saril_resimleri)
    mesaj = "🤗 İçten bir sarılma yolluyorum... hem de sessizce sarmalayan cinsten."
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=secilen_resim)
    context.bot.send_message(chat_id=update.effective_chat.id, text=mesaj)


def askitirafi(update, context):
    user = update.message.from_user.first_name
    itiraflar = [
        "Gözlerini her gördüğümde, zaman duruyor sanıyorum.",
        "Kalbim senin ses tonuna ayarlanmış bir radyo gibi çalıyor.",
        "Sen gökyüzündeki en parlak yıldız değil, o yıldızlara anlam katan gecesin.",
        "Bir tebessümünle düştüm, bir kelimenle kayboldum.",
        "Sensizlik, sanki çayı şekersiz içmek gibi. Alışılır belki ama keyif vermez.",
        "Sen konuşunca içimdeki her şey susuyor.",
        "Aklıma geldikçe gülümsüyorum, yüzüm seni biliyor.",
        "Seninle yan yana yürümek, en uzun yolu bile kısaltır.",
        "Gözlerin kelimelerin anlatamayacağı kadar güzel şeyler söylüyor.",
        "Sana alışmak değil, seni solumak gibi bir şey bu.",
        "Seni sevdiğimi söylesem klasik olur, ama sensiz uyuyamadığımı bilsen?",
        "Seni görünce bluetooth kulaklığımı kaybettim ama aşkı buldum.",
        "Kalbim sana koşarken ayağı takıldı, şimdi hem seviyorum hem topallıyorum.",
        "Sen gelince ben Google'da 'aşk nasıl unutulur?' diye aramayı bıraktım.",
        "Aşka inanmam diyordum, meğer yokluğu senmiş.",
        "Senin yüzünden çayımı şekerli içmeye başladım. Düşün artık etki seviyesini.",
        "Seni sevmek Adana sıcağında koşmak gibi, terli ama mutluyum.",
        "Gözlerini görünce beynim '404 not found' veriyor.",
        "Sen yanımdan geçince sinirim bile sakinleşiyor.",
        "Senle konuşurken mantıklı cümle kuramıyorum. Ki ben paragraf canavarıydım.",
        "Beni seversen seni de seveceğim, yoksa ikimiz de üzülürüz. Mantıklı düşün."
    ]

    secilen = random.choice(itiraflar)
    mesaj = f"📝 {user}, işte bugünkü aşk itirafın:\n\n\"{secilen}\""
    update.message.reply_text(mesaj)

def kimebenziyorum(update, context):
    user = update.message.from_user.first_name

    unlu_listesi = [
         ("Kıvanç Tatlıtuğ", "https://i.ibb.co/wS2kpyZ/kivanc.jpg"),
    ("Barış Arduç", "https://i.ibb.co/N3CN4zC/baris-arduc.jpg"),
    ("Kenan İmirzalioğlu", "https://i.ibb.co/fS6n7W9/kenan.jpg"),
    ("Tarkan", "https://i.ibb.co/LS3QTvx/tarkan.jpg"),
    ("Murat Boz", "https://i.ibb.co/PWdsFrW/murat-boz.jpg"),
    ("Haluk Bilginer", "https://i.ibb.co/PFvMzCg/haluk.jpg"),
    ("Engin Akyürek", "https://i.ibb.co/7NkMhC1/engin-akyurek.jpg"),
    ("Çağatay Ulusoy", "https://i.ibb.co/vmQrcVR/cagatay.jpg"),
    ("Nejat İşler", "https://i.ibb.co/hLBknFT/nejat.jpg"),
    ("Halit Ergenç", "https://i.ibb.co/k9YmVnr/halit.jpg"),
    ("Brad Pitt", "https://i.ibb.co/mFrnWxR/bradpitt.jpg"),
    ("Ryan Gosling", "https://i.ibb.co/TbNPtRP/ryangosling.jpg"),
    ("Johnny Depp", "https://i.ibb.co/6Bt0rZy/johnnydepp.jpg"),
    ("Tom Hardy", "https://i.ibb.co/8XrPxw4/tomhardy.jpg"),
    ("Leonardo DiCaprio", "https://i.ibb.co/j3vztXy/leo.jpg"),
    ("Elvis Presley", "https://i.ibb.co/Vt9WTzM/elvis.jpg"),
    ("Keanu Reeves", "https://i.ibb.co/vZT8cV7/keanu.jpg"),
    ("Zeki Müren", "https://i.ibb.co/1ncbD2z/zeki.jpg"),
    ("Cem Yılmaz", "https://i.ibb.co/Jm3kQbH/cemyilmaz.jpg"),
    ("Recep İvedik", "https://i.ibb.co/gjD5SgQ/recep.jpg"),
         ("Serenay Sarıkaya", "https://i.ibb.co/9Z4Gp9n/serenay.jpg"),
    ("Beren Saat", "https://i.ibb.co/k8xMN6G/beren.jpg"),
    ("Demet Özdemir", "https://i.ibb.co/tKHxrMJ/demet.jpg"),
    ("Tuba Büyüküstün", "https://i.ibb.co/WvWzjqk/tuba.jpg"),
    ("Sıla", "https://i.ibb.co/qp4bVdK/sila.jpg"),
    ("Hande Erçel", "https://i.ibb.co/N9WfzRW/hande.jpg"),
    ("Hazal Kaya", "https://i.ibb.co/LN5HPTh/hazal.jpg"),
    ("Bensu Soral", "https://i.ibb.co/Dkx8Sw9/bensu.jpg"),
    ("Aslı Enver", "https://i.ibb.co/yFt9zyX/asli.jpg"),
    ("Elçin Sangu", "https://i.ibb.co/Z1tz0YB/elcin.jpg"),
    ("Ebru Gündeş", "https://i.ibb.co/VVCFsZz/ebru.jpg"),
    ("Ajda Pekkan", "https://i.ibb.co/KK8XY4P/ajda.jpg"),
    ("Seda Sayan", "https://i.ibb.co/f1MR7Rf/seda.jpg"),
    ("Sezen Aksu", "https://i.ibb.co/sFhysFr/sezen.jpg"),
    ("Angelina Jolie", "https://i.ibb.co/jbKxWdy/jolie.jpg"),
    ("Scarlett Johansson", "https://i.ibb.co/VSkMBZT/scarlett.jpg"),
    ("Margot Robbie", "https://i.ibb.co/xXGLgzD/margot.jpg"),
    ("Emma Watson", "https://i.ibb.co/fpLHTfJ/emma.jpg"),
    ("Gal Gadot", "https://i.ibb.co/0Gbvmf6/gal.jpg"),
    ("Megan Fox", "https://i.ibb.co/NV9nW6B/megan.jpg"),
    ("Zendaya", "https://i.ibb.co/ZMgJ5Tp/zendaya.jpg"),
    ("Anne Hathaway", "https://i.ibb.co/5vN8Ms5/anne.jpg"),
    ("Natalie Portman", "https://i.ibb.co/5xy3mhC/natalie.jpg"),
    ("Ariana Grande", "https://i.ibb.co/2nhTRJW/ariana.jpg"),
    ("Billie Eilish", "https://i.ibb.co/ZfTZLNC/billie.jpg"),
    ("Dua Lipa", "https://i.ibb.co/V92pJ6q/dua.jpg"),
    ("Lady Gaga", "https://i.ibb.co/nzC9rPC/gaga.jpg"),
    ("Beyoncé", "https://i.ibb.co/XYpTVgD/beyonce.jpg"),
    ("Rihanna", "https://i.ibb.co/nzyKTLT/rihanna.jpg")
    ]

    secilen = random.choice(unlu_listesi)
    isim, foto_url = secilen

    caption = f"📸 {user}, sen bana bayağı {isim} havası veriyorsun 😎"
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=foto_url, caption=caption)

def dovusmuzik(update, context):
    user = update.message.from_user
    if user.username not in ["geceupuzun", "banabulasmayin"]:
        update.message.reply_text("⛔ Bu hizmet yalnızca iki özel isme aittir. Lütfen haddinizi bilin.")
        return

    mesajlar = [
        "💋 Bu parça gecelere özel...",
        "🔥 Ruhlar yakınlaşırken çalan şarkı bu olmalı.",
        "🌙 Bu müzikle kalp atışları hızlanır...",
        "🥊 Dövüşmek için güzel bir gece!",
        "💢 Dövüşmenin tam sırası!",
        "💥 Güzel dövüşler şimdi başlar...",
        "⚖️ Dövüşerek yargılama zamanı!"
    ]

    muzikler = [
        ("Slightly Hung Over – Beautiful", "https://www.youtube.com/watch?v=dm7Z6a1FqBg"),
        ("Cigarettes After Sex – Apocalypse", "https://www.youtube.com/watch?v=ay0zX9jHcw8"),
        ("Lana Del Rey – Young and Beautiful", "https://www.youtube.com/watch?v=o_1aF54DO60"),
        ("The xx – Intro", "https://www.youtube.com/watch?v=-_3mNCaJgNM"),
        ("Massive Attack – Paradise Circus", "https://www.youtube.com/watch?v=jEgX64n3T7g"),
        ("Rhye – Open", "https://www.youtube.com/watch?v=sng_CdAAw8M"),
        ("ZHU – Faded", "https://www.youtube.com/watch?v=3_JjM3z0DuE"),
        ("Banks – Waiting Game", "https://www.youtube.com/watch?v=ZDLaKfFf-Oo"),
        ("London Grammar – Hey Now", "https://www.youtube.com/watch?v=nMEHJPuggHQ"),
        ("The Weeknd – Wicked Games", "https://www.youtube.com/watch?v=o5fQtnUjTHQ"),
        ("FKA twigs – Two Weeks", "https://www.youtube.com/watch?v=3yDP9MKVhZc"),
        ("Chet Faker – Talk Is Cheap", "https://www.youtube.com/watch?v=aP_-P_BS6KY"),
        ("Hooverphonic – Mad About You", "https://www.youtube.com/watch?v=-rx5LQjO0nQ"),
        ("James Blake – Retrograde", "https://www.youtube.com/watch?v=6p6PcFFUm5I"),
        ("Arctic Monkeys – Do I Wanna Know?", "https://www.youtube.com/watch?v=bpOSxM0rNPM"),
        ("Snoh Aalegra – I Want You Around", "https://www.youtube.com/watch?v=PC8LSnJdRfQ"),
        ("Kadebostany – Castle in the Snow", "https://www.youtube.com/watch?v=1BLLH39YkZs"),
        ("Portishead – Glory Box", "https://www.youtube.com/watch?v=EkHTsc9PU2A"),
        ("Daughter – Youth", "https://www.youtube.com/watch?v=VEpMj-tqixs"),
        ("Morcheeba – Enjoy the Ride", "https://www.youtube.com/watch?v=t3INU16pt70"),
        ("Bonobo – Cirrus", "https://www.youtube.com/watch?v=WF34N4gJAKE"),
        ("Alina Baraz & Galimatias – Fantasy", "https://www.youtube.com/watch?v=2bZC85iPzTA"),
        ("SOHN – Artifice", "https://www.youtube.com/watch?v=ZMESU5jvFyc"),
        ("Milky Chance – Stolen Dance", "https://www.youtube.com/watch?v=iX-QaNzd-0Y"),
        ("Mazzy Star – Fade Into You", "https://www.youtube.com/watch?v=ImKY6TZEyrI"),
        ("The Neighbourhood – Sweater Weather", "https://www.youtube.com/watch?v=GCdwKhTtNNw"),
        ("Angus & Julia Stone – Big Jet Plane", "https://www.youtube.com/watch?v=yFTvbcNhEgc"),
        ("José González – Heartbeats", "https://www.youtube.com/watch?v=s4_4abCWw-w"),
        ("Flume – Never Be Like You", "https://www.youtube.com/watch?v=Ly7uj0JwgKg"),
        ("Sade – No Ordinary Love", "https://www.youtube.com/watch?v=_WcWHZc8s2I"),
        ("Gotye – Somebody That I Used To Know", "https://www.youtube.com/watch?v=8UVNT4wvIGY"),
        ("ODESZA – A Moment Apart", "https://www.youtube.com/watch?v=rn9AQoI7mYU"),
        ("The Weeknd – Earned It", "https://www.youtube.com/watch?v=waU75jdUnYw"),
        ("Yuna – Lullabies", "https://www.youtube.com/watch?v=9rQzT9ZFXe4"),
        ("Tame Impala – The Less I Know The Better", "https://www.youtube.com/watch?v=sBzrzS1Ag_g")
    ]

    replik = random.choice(mesajlar)
    sarki = random.choice(muzikler)
    update.message.reply_text(f"{replik}\n🎵 {sarki[0]}\n{sarki[1]}")

def tokat(update, context):
    user = update.message.from_user.first_name
    tokatlar = [
        "Şabalağı ense köküne yapıştırdın 😤",
        "Öyle bi vurdunki yani anası ağladı 🥵",
        "Süleyman'ın Soner'e vurduğu yumruk gibi 🧠",
        "Sümük gibi yapıştı 😮‍💨",
        "Mike Tyson görse 'o nasıl tokat la' derdi 🥊",
        "Ya kebapçı ya tornacı, telafisi yok bu tokadın 🌶️",
        "Ağzının şölüğü aktı la herifin 🤧",
        "Yüzü morardı, rengine filtre takıldı 🟣",
        "O nası tokat la, kız gibi 😅",
        "Sinek daha fazla hasar verirdi 😂",
        "Gece Yargıcının kendine vurduğu darbe kadar ağırdı 🧩",
        "Vurma artık vurma! Polisi arıcam! 🚓",
        "Vay hırto iyi oldu sana 😤"
    ]
    hasar = random.randint(10, 100)
    secilen = random.choice(tokatlar)
    mesaj = f"🖐️ {user} tokadı çaktı!\n💥 {secilen}\n🩸 Hasar: {hasar} puan"
    update.message.reply_text(mesaj)

def start_bot():
    print("🚨 Cipiti debug: BOT BAŞLIYOR...")
    TOKEN = '7755024967:AAHZpLa1vvVkZ0yM-ke9s4Iznupoylctgek'
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, track_users))
    dp.add_handler(CommandHandler("ship", ship))
    dp.add_handler(CommandHandler("shipme", shipme))
    dp.add_handler(CommandHandler("adana", adana))
    dp.add_handler(CommandHandler("urfa", urfa))
    dp.add_handler(CommandHandler("tokat", tokat))
    dp.add_handler(CommandHandler("rona", rona))
    dp.add_handler(CommandHandler("esma", esma))
    dp.add_handler(CommandHandler("yargi", yargi))
    dp.add_handler(CommandHandler("kimdir", kimdir))
    dp.add_handler(CommandHandler("kamyoncu", kamyoncu))
    dp.add_handler(CommandHandler("saril", saril))
    dp.add_handler(CommandHandler("askitirafi", askitirafi))
    dp.add_handler(CommandHandler("kimebenziyorum", kimebenziyorum))
    dp.add_handler(CommandHandler("dovusmuzik", dovusmuzik,))
    
    print("✅ Cipiti polling başlattı!")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    start_bot()
