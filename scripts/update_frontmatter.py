#!/usr/bin/env python3
"""Update front matter for all why/ articles across 12 languages:
1. Fix dates to 2026-02-24
2. Localize tags per language
3. Add author + authorLink
"""
import os, re

BASE = "/mnt/c/Users/mail/git/dabel5/content"
TODAY = "2026-02-24T12:00:00+09:00"
AUTHOR_LINK = "https://parkjunwoo.com/1/about"

LANGS = ["en","ko","zh","es","ar","pt","id","ru","ja","fr","de","he"]

FILES = [
    "eml5-bootstrap.md",
    "mirror-thermal-runaway.md",
    "1986da.md",
    "mining-transport.md",
    "dyson-swarm-at-l5.md",
    "power-transmission-local.md",
    "why-turbines.md",
    "heat-flow.md",
    "climate-control.md",
]

# Tags per file, per language
# Order: en, ko, zh, es, ar, pt, id, ru, ja, fr, de, he
TAGS = {
    "eml5-bootstrap.md": {
        "en": ["dyson-swarm", "EML5", "bootstrap", "lagrange-point"],
        "ko": ["다이슨-스웜", "EML5", "부트스트랩", "라그랑주점"],
        "zh": ["戴森群", "EML5", "引导启动", "拉格朗日点"],
        "es": ["enjambre-dyson", "EML5", "arranque", "punto-lagrange"],
        "ar": ["سرب-دايسون", "EML5", "تمهيد", "نقطة-لاغرانج"],
        "pt": ["enxame-dyson", "EML5", "bootstrap", "ponto-lagrange"],
        "id": ["swarm-dyson", "EML5", "bootstrap", "titik-lagrange"],
        "ru": ["рой-дайсона", "EML5", "начальная-загрузка", "точка-лагранжа"],
        "ja": ["ダイソンスウォーム", "EML5", "ブートストラップ", "ラグランジュ点"],
        "fr": ["essaim-dyson", "EML5", "amorçage", "point-lagrange"],
        "de": ["dyson-schwarm", "EML5", "bootstrap", "lagrange-punkt"],
        "he": ["נחיל-דייסון", "EML5", "אתחול", "נקודת-לגראנז'"],
    },
    "mirror-thermal-runaway.md": {
        "en": ["dyson-swarm", "mercury", "thermal-runaway", "mirror"],
        "ko": ["다이슨-스웜", "수성", "열폭주", "거울"],
        "zh": ["戴森群", "水星", "热失控", "反射镜"],
        "es": ["enjambre-dyson", "mercurio", "desbordamiento-térmico", "espejo"],
        "ar": ["سرب-دايسون", "عطارد", "انفلات-حراري", "مرآة"],
        "pt": ["enxame-dyson", "mercúrio", "fuga-térmica", "espelho"],
        "id": ["swarm-dyson", "merkurius", "pelarian-termal", "cermin"],
        "ru": ["рой-дайсона", "меркурий", "тепловой-разгон", "зеркало"],
        "ja": ["ダイソンスウォーム", "水星", "熱暴走", "ミラー"],
        "fr": ["essaim-dyson", "mercure", "emballement-thermique", "miroir"],
        "de": ["dyson-schwarm", "merkur", "thermisches-durchgehen", "spiegel"],
        "he": ["נחיל-דייסון", "כוכב-חמה", "בריחה-תרמית", "מראה"],
    },
    "1986da.md": {
        "en": ["asteroid", "1986-DA", "mining", "resources"],
        "ko": ["소행성", "1986-DA", "채굴", "자원"],
        "zh": ["小行星", "1986-DA", "采矿", "资源"],
        "es": ["asteroide", "1986-DA", "minería", "recursos"],
        "ar": ["كويكب", "1986-DA", "تعدين", "موارد"],
        "pt": ["asteroide", "1986-DA", "mineração", "recursos"],
        "id": ["asteroid", "1986-DA", "penambangan", "sumber-daya"],
        "ru": ["астероид", "1986-DA", "добыча", "ресурсы"],
        "ja": ["小惑星", "1986-DA", "採掘", "資源"],
        "fr": ["astéroïde", "1986-DA", "exploitation-minière", "ressources"],
        "de": ["asteroid", "1986-DA", "bergbau", "ressourcen"],
        "he": ["אסטרואיד", "1986-DA", "כרייה", "משאבים"],
    },
    "mining-transport.md": {
        "en": ["asteroid-mining", "transport", "SMR", "NTP"],
        "ko": ["소행성-채굴", "수송", "SMR", "NTP"],
        "zh": ["小行星采矿", "运输", "SMR", "NTP"],
        "es": ["minería-asteroide", "transporte", "SMR", "NTP"],
        "ar": ["تعدين-كويكب", "نقل", "SMR", "NTP"],
        "pt": ["mineração-asteroide", "transporte", "SMR", "NTP"],
        "id": ["penambangan-asteroid", "transportasi", "SMR", "NTP"],
        "ru": ["добыча-астероидов", "транспорт", "SMR", "NTP"],
        "ja": ["小惑星採掘", "輸送", "SMR", "NTP"],
        "fr": ["exploitation-astéroïde", "transport", "SMR", "NTP"],
        "de": ["asteroidenbergbau", "transport", "SMR", "NTP"],
        "he": ["כריית-אסטרואיד", "תחבורה", "SMR", "NTP"],
    },
    "dyson-swarm-at-l5.md": {
        "en": ["dyson-swarm", "SEL5", "self-replication", "scaling"],
        "ko": ["다이슨-스웜", "SEL5", "자기복제", "스케일링"],
        "zh": ["戴森群", "SEL5", "自我复制", "规模扩展"],
        "es": ["enjambre-dyson", "SEL5", "autorreplicación", "escalado"],
        "ar": ["سرب-دايسون", "SEL5", "تكاثر-ذاتي", "توسيع"],
        "pt": ["enxame-dyson", "SEL5", "autorreplicação", "escalamento"],
        "id": ["swarm-dyson", "SEL5", "replikasi-diri", "penskalaan"],
        "ru": ["рой-дайсона", "SEL5", "саморепликация", "масштабирование"],
        "ja": ["ダイソンスウォーム", "SEL5", "自己複製", "スケーリング"],
        "fr": ["essaim-dyson", "SEL5", "autoréplication", "mise-à-échelle"],
        "de": ["dyson-schwarm", "SEL5", "selbstreplikation", "skalierung"],
        "he": ["נחיל-דייסון", "SEL5", "שכפול-עצמי", "הרחבה"],
    },
    "power-transmission-local.md": {
        "en": ["power-transmission", "wireless-power", "local-consumption"],
        "ko": ["에너지-전송", "무선-전력", "현지-소비"],
        "zh": ["电力传输", "无线电力", "本地消费"],
        "es": ["transmisión-energía", "energía-inalámbrica", "consumo-local"],
        "ar": ["نقل-طاقة", "طاقة-لاسلكية", "استهلاك-محلي"],
        "pt": ["transmissão-energia", "energia-sem-fio", "consumo-local"],
        "id": ["transmisi-daya", "daya-nirkabel", "konsumsi-lokal"],
        "ru": ["передача-энергии", "беспроводная-энергия", "местное-потребление"],
        "ja": ["送電", "無線電力", "現地消費"],
        "fr": ["transmission-énergie", "énergie-sans-fil", "consommation-locale"],
        "de": ["energieübertragung", "drahtlose-energie", "lokalverbrauch"],
        "he": ["שידור-אנרגיה", "אנרגיה-אלחוטית", "צריכה-מקומית"],
    },
    "why-turbines.md": {
        "en": ["solar-thermal", "turbine", "self-replication", "photovoltaic"],
        "ko": ["태양열", "터빈", "자기복제", "태양광-패널"],
        "zh": ["太阳能热", "涡轮机", "自我复制", "光伏"],
        "es": ["solar-térmico", "turbina", "autorreplicación", "fotovoltaica"],
        "ar": ["حرارة-شمسية", "توربين", "تكاثر-ذاتي", "كهروضوئي"],
        "pt": ["solar-térmico", "turbina", "autorreplicação", "fotovoltaico"],
        "id": ["panas-matahari", "turbin", "replikasi-diri", "fotovoltaik"],
        "ru": ["солнечная-тепловая", "турбина", "саморепликация", "фотоэлектрика"],
        "ja": ["太陽熱", "タービン", "自己複製", "太陽光発電"],
        "fr": ["solaire-thermique", "turbine", "autoréplication", "photovoltaïque"],
        "de": ["solarthermie", "turbine", "selbstreplikation", "photovoltaik"],
        "he": ["תרמו-סולארי", "טורבינה", "שכפול-עצמי", "פוטו-וולטאי"],
    },
    "heat-flow.md": {
        "en": ["thermal-management", "radiator", "heat-cascade"],
        "ko": ["열관리", "방열기", "열-캐스케이드"],
        "zh": ["热管理", "散热器", "热级联"],
        "es": ["gestión-térmica", "radiador", "cascada-térmica"],
        "ar": ["إدارة-حرارية", "مشعاع", "تتالي-حراري"],
        "pt": ["gestão-térmica", "radiador", "cascata-térmica"],
        "id": ["manajemen-termal", "radiator", "kaskade-panas"],
        "ru": ["теплоуправление", "радиатор", "тепловой-каскад"],
        "ja": ["熱管理", "ラジエーター", "熱カスケード"],
        "fr": ["gestion-thermique", "radiateur", "cascade-thermique"],
        "de": ["wärmemanagement", "radiator", "wärme-kaskade"],
        "he": ["ניהול-תרמי", "רדיאטור", "מפל-חום"],
    },
    "climate-control.md": {
        "en": ["climate-control", "SEL1", "geoengineering", "DABEL5"],
        "ko": ["기후-제어", "SEL1", "지구공학", "DABEL5"],
        "zh": ["气候控制", "SEL1", "地球工程", "DABEL5"],
        "es": ["control-climático", "SEL1", "geoingeniería", "DABEL5"],
        "ar": ["تحكم-مناخي", "SEL1", "هندسة-جيولوجية", "DABEL5"],
        "pt": ["controle-climático", "SEL1", "geoengenharia", "DABEL5"],
        "id": ["kontrol-iklim", "SEL1", "geoengineering", "DABEL5"],
        "ru": ["климат-контроль", "SEL1", "геоинженерия", "DABEL5"],
        "ja": ["気候制御", "SEL1", "ジオエンジニアリング", "DABEL5"],
        "fr": ["contrôle-climatique", "SEL1", "géo-ingénierie", "DABEL5"],
        "de": ["klimasteuerung", "SEL1", "geoengineering", "DABEL5"],
        "he": ["בקרת-אקלים", "SEL1", "הנדסה-גיאולוגית", "DABEL5"],
    },
}

def format_tags(tags):
    return "[" + ", ".join(f'"{t}"' for t in tags) + "]"

def update_file(filepath, lang, filename):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Fix date
    content = re.sub(
        r'date: \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}',
        f'date: {TODAY}',
        content
    )

    # 2. Update tags
    if filename in TAGS and lang in TAGS[filename]:
        new_tags = format_tags(TAGS[filename][lang])
        content = re.sub(r'tags: \[.*?\]', f'tags: {new_tags}', content)

    # 3. Add author (after summary line, before closing ---)
    author_name = "박준우" if lang == "ko" else "PARK JUN WOO"
    if "author:" not in content:
        content = re.sub(
            r'(summary: ".*?")\n---',
            f'\\1\nauthor: "{author_name}"\nauthorLink: "{AUTHOR_LINK}"\n---',
            content,
            flags=re.DOTALL
        )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

count = 0
for lang in LANGS:
    for filename in FILES:
        filepath = os.path.join(BASE, lang, "why", filename)
        if os.path.exists(filepath):
            update_file(filepath, lang, filename)
            count += 1
            print(f"  [{lang}] {filename}")

print(f"\nUpdated {count} files")
