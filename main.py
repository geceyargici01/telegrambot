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
    mesaj = f"👑 {user} dedi ki:\n\n“{secilen}”"
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
    mesaj = f"💫 {user} dedi ki:\n\n{secilen}"
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
    user = update.message.from_user.first_name

    gif_listesi = [
        "https://media.tenor.com/qxk1XWY5R7MAAAAC/hug-anime.gif",
        "https://media.tenor.com/YPD8UppSboQAAAAC/anime-hug-cute.gif",
        "https://media.tenor.com/yV1ejJi7txYAAAAC/anime-couple-hug.gif",
        "https://media.tenor.com/KmznKUPV3EQAAAAC/anime-love.gif",
        "https://media.tenor.com/ovVgWmbmK50AAAAd/hug-anime-love.gif",
        "https://media.tenor.com/iqxH3eW1edkAAAAC/jujutsu-kaisen-hug.gif"
    ]

    secilen_gif = random.choice(gif_listesi)
    mesaj = f"🤗 {user}, bu sarılma senin için. Hem sıcak, hem içten. 🩵"
    context.bot.send_animation(chat_id=update.effective_chat.id, animation=secilen_gif, caption=mesaj)

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
        ("Kıvanç Tatlıtuğ", "https://i.imgur.com/xnFHhls.jpg"),
        ("Barış Arduç", "https://i.imgur.com/lR4Cby3.jpg"),
        ("Kenan İmirzalioğlu", "https://i.imgur.com/0hYkEpT.jpg"),
        ("Tarkan", "https://i.imgur.com/fO3UcSG.jpg"),
        ("Murat Boz", "https://i.imgur.com/m1LEsPv.jpg"),
        ("Haluk Bilginer", "https://i.imgur.com/jDYuwSP.jpg"),
        ("Engin Akyürek", "https://i.imgur.com/fDpH3wG.jpg"),
        ("Çağatay Ulusoy", "https://i.imgur.com/G4Lo0XP.jpg"),
        ("Nejat İşler", "https://i.imgur.com/V7RFMqB.jpg"),
        ("Halit Ergenç", "https://i.imgur.com/gKKfPiX.jpg"),
        ("Brad Pitt", "https://i.imgur.com/H1n4ew5.jpg"),
        ("Ryan Gosling", "https://i.imgur.com/sTfAYO4.jpg"),
        ("Johnny Depp", "https://i.imgur.com/WfnidOY.jpg"),
        ("Tom Hardy", "https://i.imgur.com/UYkVo6J.jpg"),
        ("Leonardo DiCaprio", "https://i.imgur.com/WrZDRqM.jpg"),
        ("Elvis Presley", "https://i.imgur.com/Oo1Xzt6.jpg"),
        ("Keanu Reeves", "https://i.imgur.com/lqKX5GZ.jpg"),
        ("Zeki Müren", "https://i.imgur.com/q0rGMRB.jpg"),
        ("Cem Yılmaz", "https://i.imgur.com/NdKhGxY.jpg"),
        ("Recep İvedik", "https://i.imgur.com/fTW1uU2.jpg"),
        ("Serenay Sarıkaya", "https://i.imgur.com/wEnF9PG.jpg"),
        ("Beren Saat", "https://i.imgur.com/I3Cm0c7.jpg"),
        ("Demet Özdemir", "https://i.imgur.com/dOwEDZz.jpg"),
        ("Tuba Büyüküstün", "https://i.imgur.com/hIDqqRo.jpg"),
        ("Sıla", "https://i.imgur.com/GikEvna.jpg"),
        ("Hande Erçel", "https://i.imgur.com/4lRLb4S.jpg"),
        ("Hazal Kaya", "https://i.imgur.com/Q5NHRT0.jpg"),
        ("Bensu Soral", "https://i.imgur.com/Vh3dco9.jpg"),
        ("Aslı Enver", "https://i.imgur.com/lhB5Z8m.jpg"),
        ("Elçin Sangu", "https://i.imgur.com/bBzH49P.jpg"),
        ("Ebru Gündeş", "https://i.imgur.com/nRMpMdP.jpg"),
        ("Ajda Pekkan", "https://i.imgur.com/dQreQ57.jpg"),
        ("Seda Sayan", "https://i.imgur.com/YUOB3jh.jpg"),
        ("Sezen Aksu", "https://i.imgur.com/xGlmZfP.jpg"),
        ("Angelina Jolie", "https://i.imgur.com/K3n9Ptn.jpg"),
        ("Scarlett Johansson", "https://i.imgur.com/hY2lj6a.jpg"),
        ("Margot Robbie", "https://i.imgur.com/UmoRld5.jpg"),
        ("Emma Watson", "https://i.imgur.com/t0VYlDZ.jpg"),
        ("Gal Gadot", "https://i.imgur.com/3PTs96P.jpg"),
        ("Megan Fox", "https://i.imgur.com/1iqGrOf.jpg"),
        ("Zendaya", "https://i.imgur.com/LikR9Q9.jpg"),
        ("Anne Hathaway", "https://i.imgur.com/9K3Bq8Z.jpg"),
        ("Natalie Portman", "https://i.imgur.com/jYuZskt.jpg"),
        ("Ariana Grande", "https://i.imgur.com/SEWhEvX.jpg"),
        ("Billie Eilish", "https://i.imgur.com/2lU2N2E.jpg"),
        ("Dua Lipa", "https://i.imgur.com/lVR3sAw.jpg"),
        ("Lady Gaga", "https://i.imgur.com/VO3BYY5.jpg"),
        ("Beyoncé", "https://i.imgur.com/l8V9M4y.jpg"),
        ("Rihanna", "https://i.imgur.com/65Ar2Bb.jpg")
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
    dp.add_handler(CommandHandler("sarıl", sarıl))
    dp.add_handler(CommandHandler("askitirafi", askitirafi))
    dp.add_handler(CommandHandler("kimebenziyorum", kimebenziyorum))
    dp.add_handler(CommandHandler("dovusmuzik", dovusmuzik,))
    
    print("✅ Cipiti polling başlattı!")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    start_bot()
